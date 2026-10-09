import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()


class GeminiClient:

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    MODEL = "gemini-3.6-flash"

    @classmethod
    def generate(cls, prompt: str) -> str:
        try:
            response = cls.client.models.generate_content(
                model=cls.MODEL,
                contents=prompt,
            )

            return response.text

        except ServerError:
            raise Exception(
                "Gemini API is temporarily unavailable. Please try again in a few moments."
            )