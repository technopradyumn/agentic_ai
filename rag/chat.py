from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from openai import OpenAI
from dotenv import load_dotenv
from google import genai
import requests

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
)

vector_db = QdrantVectorStore.from_existing_collection(
    collection_name="learning-rag",
    embedding=embeddings,
    url="http://localhost:6333",
)

#  Take the user input

user_query = input("Enter your query: ")

# Releavent chunks from vector DB
search_result = vector_db.similarity_search(query=user_query)

content = "\n\n".join([f"Page Content: {result.page_content} \n Page Number: {result.metadata['page_label']}\nFIle Location: {result.metadata['source']}" for result in search_result
                       ])



SYSTEM_PROMPT = """ 
You are a helpful AI Assistant who answers user query based on the available context retreaved from a PDF file along with page_content and page_number. 

You should only ans the user based on the following context and navigate the user to open the right page number to know more.

Context: 
{context}
"""

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT.format(context=content)},
        {"role": "user", "content": user_query}
    ])

print(f"--->: {response.choices[0].message.content}")