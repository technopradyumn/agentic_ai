from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from openai import OpenAI


load_dotenv()


def process_query(query:str):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
    )

    vector_db = QdrantVectorStore.from_existing_collection(
        url="http://localhost:6333",
        collection_name="learning-rag",
        embedding=embeddings,
    )

    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"), 
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    print(f"Searching Chunks: {query}")
    search_result = vector_db.similarity_search(query=query)
    content = "\n\n".join([f"Page Content: {result.page_content} \n Page Number: {result.metadata['page_label']}\nFIle Location: {result.metadata['source']}" for result in search_result
    ])
    SYSTEM_PROMPT = """ 
    You are a helpful AI Assistant who answers user query based on the available context retreaved from a PDF file along with page_content and page_number. 

    You should only ans the user based on the following context and navigate the user to open the right page number to know more.

    Context: 
    {context}
    """

    response = client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.format(context=content)},
            {"role": "user", "content": query}
        ]
    )
    
    print(f"--->: {response.choices[0].message.content}")

    return response.choices[0].message.content
    
    

