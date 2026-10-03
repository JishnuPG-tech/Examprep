from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import httpx

from ..config import settings


class LLMError(RuntimeError):
    pass


@dataclass(frozen=True)
class ModelInvocation:
    provider: str
    base_url: str
    model: str
    route_model: str | None = None


class OpenAICompatibleExtractor:
    provider_name = "openai-compatible"

    def __init__(
        self,
        base_url=None,
        api_key=None,
        model=None,
        *,
        provider_name=None,
        route_model=None,
        mode=None,
        budget_usd=None,
        timeout_seconds=None,
    ):
        self.base_url = base_url or settings.llm_base_url
        self.api_key = api_key or settings.llm_api_key
        self.model = model or settings.llm_model
        self.provider_name = provider_name or self.provider_name
        self.route_model = route_model
        self.mode = mode
        self.budget_usd = budget_usd
        self.timeout_seconds = timeout_seconds or settings.llm_timeout_seconds

    def available(self):
        return bool(self.base_url and self.model)

    def invocation(self):
        if not self.available():
            raise LLMError("LLM extraction is not configured")
        return ModelInvocation(
            provider=self.provider_name,
            base_url=self.base_url or "",
            model=self.model or "",
            route_model=self.route_model,
        )

    def _headers(self):
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        if self.route_model:
            headers["X-Route-Model"] = self.route_model
        if self.mode:
            headers["X-OmniRoute-Mode"] = self.mode
        if self.budget_usd is not None:
            headers["X-OmniRoute-Budget"] = str(self.budget_usd)
        return headers

    def extract(self, source, exam):
        if not self.available():
            raise LLMError("LLM extraction is not configured")

        prompt = (
            "Extract banking exam questions from the supplied source. Return JSON only "
            "with a questions array. Preserve every mathematical symbol, operator, "
            "diagram/table/chart reference, option label, and meaningful layout cue. "
            "Do not invent missing answers. Each question must contain stem, options "
            "[{label,text}], answer, explanation only when present in the source, "
            "section/topic when determinable, and source_page when known. "
            f"Exam: {exam}\nSOURCE:\n{source}"
        )
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0,
        }

        try:
            with httpx.Client(timeout=self.timeout_seconds) as client:
                response = client.post(
                    self.base_url.rstrip("/") + "/chat/completions",
                    json=payload,
                    headers=self._headers(),
                )
                response.raise_for_status()
                data: dict[str, Any] = response.json()
        except httpx.HTTPError as exc:
            raise LLMError(f"{self.provider_name} request failed: {exc}") from exc

        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise LLMError("Unexpected LLM response schema") from exc


class OmniRouteExtractor(OpenAICompatibleExtractor):
    provider_name = "omniroute"

    def __init__(self):
        super().__init__(
            base_url=settings.omniroute_base_url,
            api_key=settings.omniroute_api_key,
            model=settings.omniroute_model,
            provider_name=self.provider_name,
            route_model=settings.omniroute_route_model,
            mode=settings.omniroute_mode,
            budget_usd=settings.omniroute_budget_usd,
            timeout_seconds=settings.omniroute_timeout_seconds,
        )


def build_extractor():
    if settings.omniroute_enabled:
        extractor = OmniRouteExtractor()
        if extractor.available():
            return extractor
        raise LLMError(
            "OMNIROUTE_ENABLED is true but OMNIROUTE_BASE_URL and "
            "OMNIROUTE_MODEL are not configured"
        )
    return OpenAICompatibleExtractor()
