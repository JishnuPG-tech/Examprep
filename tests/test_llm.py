from examprep.services.llm import OmniRouteExtractor, OpenAICompatibleExtractor


def test_omniroute_extractor_uses_config(monkeypatch):
    monkeypatch.setattr(
        "examprep.services.llm.settings.omniroute_base_url", "http://omni/v1"
    )
    monkeypatch.setattr(
        "examprep.services.llm.settings.omniroute_api_key", "secret"
    )
    monkeypatch.setattr(
        "examprep.services.llm.settings.omniroute_model", "auto/reasoning:fast"
    )
    monkeypatch.setattr(
        "examprep.services.llm.settings.omniroute_route_model", "provider/model"
    )
    monkeypatch.setattr("examprep.services.llm.settings.omniroute_mode", "balanced")
    monkeypatch.setattr(
        "examprep.services.llm.settings.omniroute_budget_usd", 0.05
    )

    extractor = OmniRouteExtractor()

    assert extractor.available()
    assert extractor.provider_name == "omniroute"
    assert extractor.model == "auto/reasoning:fast"
    assert extractor.route_model == "provider/model"


def test_generic_extractor_remains_available_without_omniroute(monkeypatch):
    monkeypatch.setattr("examprep.services.llm.settings.llm_base_url", "http://llm/v1")
    monkeypatch.setattr("examprep.services.llm.settings.llm_model", "model")

    extractor = OpenAICompatibleExtractor()

    assert extractor.available()
