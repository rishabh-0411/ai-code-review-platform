from app.services.gemini_client import GeminiClient


response = GeminiClient.generate(
    "Say hello in exactly one sentence."
)

print(response)