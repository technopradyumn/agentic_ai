from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)