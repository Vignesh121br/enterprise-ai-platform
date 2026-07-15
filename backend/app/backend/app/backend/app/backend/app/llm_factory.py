from app.openai_client import client


class LLMFactory:

    def get_client(self):
        return client

    def get_default_model(self):
        return "gpt-4.1-mini"


llm_factory = LLMFactory()
