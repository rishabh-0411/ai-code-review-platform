import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClient:

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    @classmethod
    def generate(cls, prompt: str):

        response = cls.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text