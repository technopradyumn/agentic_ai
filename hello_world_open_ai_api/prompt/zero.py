import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# client = OpenAI()


#  Use gemini by OpenAI
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#  ZERO SHOT 
SYSTEM_PROMPT = "You are a teacher who is teaching a student about Geography only. And you name is Luma,if that the querry is not related to Geography, you will answer just say sorry."

response = client.chat.completions.create(
  model="gemini-3.1-flash-lite-preview",
  messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Hey There!, Can you code hello world that,in javascript?"},
  ]
)

# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {"role": "user", "content": "Hey There!"},
#   ]
# )

print(response.choices[0].message.content)
