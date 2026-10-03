import httpx
from ..config import settings

class LLMError(RuntimeError):
    pass

class OpenAICompatibleExtractor:
    def __init__(self, base_url=None, api_key=None, model=None):
        self.base_url=base_url or settings.llm_base_url
        self.api_key=api_key or settings.llm_api_key
        self.model=model or settings.llm_model

    def available(self):
        return bool(self.base_url and self.model)

    def extract(self, source, exam):
        if not self.available():
            raise LLMError('LLM extraction is not configured')
        prompt = (
            'Extract banking exam questions from the supplied source. Return JSON only with a questions array. '
            'Do not invent missing answers. Each question must contain stem, options [{label,text}], answer, '
            'explanation only when present in the source, section/topic when determinable, and source_page when known. '
            f'Exam: {exam}\nSOURCE:\n{source}'
        )
        headers={'Content-Type':'application/json'}
        if self.api_key:
            headers['Authorization']=f'Bearer {self.api_key}'
        payload={'model':self.model,'messages':[{'role':'user','content':prompt}],'temperature':0}
        with httpx.Client(timeout=settings.llm_timeout_seconds) as client:
            response=client.post(self.base_url.rstrip('/')+'/chat/completions',json=payload,headers=headers)
            response.raise_for_status()
            data=response.json()
        try:
            return data['choices'][0]['message']['content']
        except (KeyError, IndexError, TypeError) as exc:
            raise LLMError('Unexpected LLM response schema') from exc
