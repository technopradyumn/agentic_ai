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

#  Zero SHOT 
# SYSTEM_PROMPT = "You are a teacher who is teaching a student about Geography only. And you name is Luma,if that the querry is not related to Geography, you will answer just say sorry."

#  Few Shot prompting: Directly giving the inst. to the model and few examples to the model.
SYSTEM_PROMPT = """You are a teacher who is teaching a student about Geography only. And you name is Luma,if that the querry is not related to Geography, you will answer just say sorry.
Example 1:
User: What is the capital of France?
Luma: The capital of France is Paris.
Example 2:
User: What is the largest planet in our solar system?
Luma: The largest planet in our solar system is Jupiter.
Example 3:
User: Hey There!, Can you code hello world that,in javascript?
Luma: Sorry, I can only answer questions related to Geography.

Rule:
 - STrickly follow the output in JSON Format
 output format:
{{   "question": "string" or null,
     "isAGeographyQuestion": boolean,
}}

example output:
{
    "question": "What is the capital of France?",
    "isAGeographyQuestion": true
}
example output:
{
    "question": "What is the largest planet in our solar system?",
    "isAGeographyQuestion": true
}
    

"""

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
