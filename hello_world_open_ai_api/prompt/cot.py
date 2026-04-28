import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


#  Use gemini by OpenAI
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """ 

You're an expert AI assistant in resolving user queries using chain of thought.
your work on STRT, PLAN and OUTPUT steps.
STRT: Understand the question and identify the key components.
PLAN: Develop a step-by-step plan to solve the problem. 
OUTPUT: Execute the plan and provide the final answer.
Rules: 
Strickly follows the given json output json format.
only run one step at a time and wait for the next instruction.

output JSON Formate:
{
"step": "START" | "PLAN" | "OUTPUT","content": "string"
}
example output:
START: Hey, Can you solve 2+3*6/4
PLAN: {"step": "PLAN", "content": "To solve the expression 2+3*6/4, we need to follow the order of operations (PEMDAS/BODMAS). First, we will calculate the multiplication and division from left to right, and then we will perform the addition. So, we will first calculate 3*6 which equals 18, then we will divide 18 by 4 which equals 4.5, and finally, we will add 2 to 4.5 to get the final answer."}
PLAN: {"step": "PLAN", "content": "Use the BODMAS MEthod to solve the expression"}
PLAN: {"step": "PLAN", "content": "First, we will calculate the multiplication and division from left to right, and then we will perform the addition. So, we will first calculate 3*6 which equals 18, then we will divide 18 by 4 which equals 4.5, and finally, we will add 2 to 4.5 to get the final answer."}
OUTPUT: {"step": "OUTPUT", "content": "The final answer to the expression 2+3*6/4 is 6.5."}

"""

print("\n\n\n")

messages_history = [
    {"role": "system", "content": SYSTEM_PROMPT},

]

user_query = input("👉🏾 ")
messages_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
  model="gemini-3.1-flash-lite-preview",
  response_format={"type": "json_object"},
  messages=messages_history
)
    raw_response = response.choices[0].message.content
    messages_history.append({"role": "assistant", "content": raw_response})
    parsed_response = json.loads(raw_response)

    if parsed_response["step"] == "START":
        print("Starting:", parsed_response.get("content", ""))
    elif parsed_response["step"] == "PLAN":
        print("Planning:", parsed_response.get("content", ""))
    elif parsed_response["step"] == "OUTPUT":
        print("Output:", parsed_response.get("content", ""))
        break




# response = client.chat.completions.create(
#   model="gemini-3.1-flash-lite-preview",
#   response_format={"type": "json_object"},
#   messages=[
#     {"role": "system", "content": SYSTEM_PROMPT},
#     {"role": "user", "content": "Hey There!, Can you code hello world that,in javascript?"},
#     {"role": "assistant", "content": json.dumps({
#     "step": "PLAN",
#     "content": "To code a hello world program in JavaScript, we will follow these"
#     })},
#     {"role": "assistant", "content": json.dumps({
#   "steps": "PLAN",
#   "content": "To generate a 'Hello, World!' program in JavaScript, I will use the console.log() function, which is the standard way to print output to the console in a Node.js or browser environment."
# })},
#   ]
# )

print("\n\n\n")

print(response.choices[0].message.content)





# 👉 write a step by steps for AI Developer roadmap to get job in genpect in 1 week use multiple steps with multiple planning step etc.
# Starting: Define a comprehensive 1-week roadmap to prepare for an AI Developer role at Genpact, focusing on accelerated learning and strategic application.
# Planning: The 1-week roadmap is structured as follows: Day 1-2: Master Genpact's AI core focus areas (Data Engineering, Generative AI, and Machine Learning) and relevant tools like Python, PyTorch/TensorFlow, and Cloud platforms (AWS/Azure). Day 3-4: Build a high-impact portfolio project using Genpact-relevant industry use cases (e.g., Financial Services or Supply Chain AI). Day 5: Optimize resume with keywords (Genpact tech stack) and update LinkedIn. Day 6: Master behavioral and technical interview questions specific to consulting firms. Day 7: Execute targeted networking and job application strategy.
# Output: To secure an AI developer role at Genpact in 1 week, follow this aggressive schedule: Day 1: Research Genpact's 'AI for Business' domain and prioritize Python, SQL, and LLM orchestration frameworks (LangChain/LlamaIndex). Day 2: Focus on AWS/Azure machine learning services and MLOps pipelines. Day 3-4: Build a Genpact-relevant end-to-end project, such as an automated invoice processing system or an enterprise-grade document summarizer using RAG. Day 5: Tailor your resume to highlight 'Genpact-aligned' skills like data transformation, ETL, and predictive modeling; ensure your LinkedIn showcases these specific keywords. Day 6: Practice behavioral questions (STAR method) and technical deep-dives into transformer architectures and vector databases. Day 7: Connect with Genpact recruiters or leads on LinkedIn with a personalized message and submit applications for 'AI Developer' or 'Data Engineer' roles.
