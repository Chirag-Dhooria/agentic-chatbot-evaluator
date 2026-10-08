from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import get_settings
from app.llm.provider import LLMProvider


class GeminiProvider:
    def __init__(
        self,
        model: str = "gemini-2.5-flash",
    ) -> None:
        settings = get_settings()

        self.model = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=settings.gemini_api_key,
            temperature=0.2,
        )

    def structured_output(self, schema):
        return self.model.with_structured_output(schema)


def get_gemini_provider() -> LLMProvider:
    return GeminiProvider()