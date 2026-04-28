from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


file_path = Path(__file__).parent / "nodejs.pdf"

#  Load This File
loader = PyPDFLoader(file_path = file_path)
doc = loader.load()

# print(doc[5])

#  Split This doc into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=400
    )
chunks = text_splitter.split_documents(documents=doc)

#  Vector Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning-rag",
)

print("Indexing of the document is completed......")