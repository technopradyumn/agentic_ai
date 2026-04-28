from dotenv import load_dotenv
from mem0 import Memory
import os
import os
from openai import OpenAI
from dotenv import load_dotenv
from google import genai
import json

load_dotenv()


client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

config = {
    "version": "v1.1",
    "embedding": {
        "provider": "gemini",
        "config": {
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model": "gemini-embedding-2",
        },
    },
    "llm":{
        "provider": "gemini",
        "config": { 
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model": "gemini-3.1-flash-lite-preview",
        }
    },
    "grph_store": {
        "provider": "neo4j",
        "config": {
            "uri": os.getenv("NEO4J_CONNECTION_URI"),
            "username": os.getenv("NEO4J_USERNAME"),
            "password": os.getenv("NEO4J_PASSWORD"),
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
        },
    }
}

memort_client = Memory.from_config(config)

#  Take the user input

while True:

    user_query = input("> ")

    search_memory = memort_client.search(query=user_query, user_id="pradyumn")

    memories = [
        f"ID: {mem.get("id")}\nMemory: {mem.get("memory")}" 
        for mem in search_memory.get("results")
    ]

    SYSTEM_PROMPT = f"""
        Here is the context about the user:
        {json.dumps(memories)}
    """

    response = client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )
    ai_response = response.choices[0].message.content
    print("AI: ", ai_response)

    memort_client.add(
        user_id="pradyumn",
        messages=[
            {
                "role": "user",
                "content": user_query
            },
            {
                "role": "assistant",
                "content": ai_response
            }
        ]
    )

    print("Print that memory has been saved: ")