import os

from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents="confirm our connection with the phrase confirm",
)
print(response.text)
