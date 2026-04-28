# 🤖 Agentic AI - Advanced AI Agents Framework

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/badge/stars-AI%20Agents-brightgreen.svg?style=flat-square)](https://github.com/technopradyumn/agentic_ai)
[![Status](https://img.shields.io/badge/status-Active-success.svg?style=flat-square)](https://github.com/technopradyumn/agentic_ai)

**A comprehensive framework for building intelligent AI agents with LLMs, RAG, memory management, and multi-modal capabilities**

[🚀 Quick Start](#quick-start) • [📖 Documentation](#documentation) • [🏗️ Architecture](#architecture) • [🎯 Features](#features) • [📚 Examples](#examples)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [🎯 Features](#features)
- [🏗️ Project Architecture](#project-architecture)
- [📦 Installation](#installation)
- [🚀 Quick Start](#quick-start)
- [📚 Module Guide](#module-guide)
- [🔧 Configuration](#configuration)
- [💡 Advanced Usage](#advanced-usage)
- [🎨 Architecture Diagrams](#architecture-diagrams)
- [🐳 Docker Support](#docker-support)
- [🧪 Testing](#testing)
- [📝 License](#license)
- [🤝 Contributing](#contributing)

---

## Overview

**Agentic AI** is a comprehensive framework designed for building sophisticated AI agents that can reason, plan, and execute complex tasks. This project showcases multiple approaches to building intelligent systems using cutting-edge LLM technologies including OpenAI's GPT models, Google's Gemini, and open-source alternatives like Ollama.

### Key Problem Solved

Traditional applications are reactive - they respond to user input. **Agentic AI** empowers applications to be proactive, autonomous systems that can:
- 🧠 Reason about complex problems
- 🗂️ Retrieve and process information dynamically
- 💾 Maintain persistent memory and context
- 🎤 Handle multi-modal inputs (text, voice)
- ⚡ Process tasks asynchronously via queues
- 🔄 Execute conditional workflows

---

## 🎯 Features

### Core Capabilities

| Feature | Description | Module |
|---------|-------------|--------|
| **LLM Integration** | Support for OpenAI GPT, Google Gemini, Ollama | `hello_world_open_ai_api/` |
| **Agentic Workflows** | State-based graph execution with LangGraph | `langGraph/` |
| **RAG System** | Retrieval Augmented Generation with PDF support | `rag/` |
| **Memory Management** | Persistent agent memory and context handling | `mem_agent/` |
| **Async Task Queue** | Redis-based job queue for scalable processing | `rag_queue/` |
| **Voice Agents** | Voice input/output capabilities | `voice_agents/` |
| **CLI Agents** | Command-line interface for agent interactions | `cli_coding_agent/` |
| **Prompt Engineering** | Multiple prompt strategies (Zero-shot, Few-shot, CoT) | `hello_world_open_ai_api/prompt/` |
| **Local LLM Support** | Run models locally with Ollama | `ollama_project/` |
| **Conditional Logic** | Complex decision trees in agent workflows | `langGraph/conditional_chat.py` |

### Technology Stack

```
┌─────────────────────────────────────────┐
│         Frontend/Interface              │
│  (CLI, Voice, Web API, Chat Interface)  │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Agent Framework Layer               │
│  (LangGraph, LangChain, State Machine)  │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      LLM Integration Layer               │
│  (OpenAI, Gemini, Ollama, HuggingFace) │
└────────────────┬────────────────────────┘
                 │
┌────────────────▼────────────────────────┐
│      Data & Memory Layer                 │
│  (RAG, Vector DB, Redis, Memory Store)  │
└─────────────────────────────────────────┘
```

---

## 🏗️ Project Architecture

```
Agentic AI/
│
├── 📁 hello_world_open_ai_api/          # Basic LLM Integration
│   ├── main.py                          # OpenAI API examples
│   ├── new_gemini.py                    # Gemini API integration
│   ├── requirements.txt
│   └── prompt/                          # Prompt engineering strategies
│       ├── cot.py                       # Chain-of-Thought prompting
│       ├── few.py                       # Few-shot learning
│       ├── zero.py                      # Zero-shot prompting
│       ├── persona.py                   # Persona-based prompting
│       └── prompt_style                 # Prompt style templates
│
├── 📁 langGraph/                        # Agentic Workflows
│   ├── chat.py                          # Basic chat agent
│   ├── chat_checkpoint.py               # Persistent state management
│   ├── conditional_chat.py              # Conditional logic workflows
│   └── docker-compose.yml               # Containerization
│
├── 📁 rag/                              # Retrieval Augmented Generation
│   ├── index.py                         # Vector index creation
│   ├── chat.py                          # RAG chat system
│   ├── docker-compose.yml
│   └── *.pdf                            # Sample documents
│
├── 📁 rag_queue/                        # Async Task Queue
│   ├── server.py                        # Task server
│   ├── main.py                          # Queue consumer
│   ├── client/rq_client.py              # Client interface
│   ├── queues/worker.py                 # Worker processes
│   └── docker-compose.yml
│
├── 📁 mem_agent/                        # Memory Management
│   ├── mem.py                           # Memory agent implementation
│   └── docker-compose.yml
│
├── 📁 voice_agents/                     # Voice Capabilities
│   ├── main.py                          # Voice agent main
│   ├── codex.py                         # Voice synthesis
│   └── requirements.txt
│
├── 📁 ollama_project/                   # Local LLM Support
│   ├── server.py                        # Ollama integration
│   └── requirements.txt
│
├── 📁 hf_basics/                        # HuggingFace Integration
│   └── main.py
│
├── 📁 cli_coding_agent/                 # CLI Agent
│   ├── agent.py
│   └── main.py
│
├── requirements.txt                     # Root dependencies
├── main.py                              # Tokenization example
└── .gitignore                          # Sensitive file exclusions

```

---

## 📦 Installation

### Prerequisites

- **Python**: 3.8 or higher
- **pip**: Package manager
- **Docker** (optional): For containerized deployments
- **Redis** (optional): For queue-based systems
- **FFmpeg** (optional): For voice processing

### System Requirements

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.8 | 3.11+ |
| RAM | 4GB | 8GB+ |
| Storage | 2GB | 10GB+ |
| OS | Windows/Mac/Linux | Linux (Ubuntu 20.04+) |

### Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/technopradyumn/agentic_ai.git
cd agentic_ai

# Or navigate to local folder
cd "c:\Users\techn\Desktop\Learning\Python\Agentic AI"
```

### Step 2: Create Virtual Environment

```bash
# Using venv (Windows)
python -m venv venv
venv\Scripts\activate

# Using venv (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# Using conda (optional)
conda create -n agentic_ai python=3.10
conda activate agentic_ai
```

### Step 3: Install Dependencies

```bash
# Install all requirements
pip install -r requirements.txt

# For specific modules:

# OpenAI and Gemini integration
pip install openai langchain-google-genai python-dotenv

# LangGraph for workflows
pip install langgraph langchain

# RAG and vector search
pip install langchain-community chromadb pypdf

# Voice processing
pip install SpeechRecognition pyttsx3 pyaudio

# Async queues
pip install rq redis

# Data processing
pip install pandas numpy scikit-learn

# Local LLM support
pip install ollama

# Text tokenization
pip install tiktoken
```

### Step 4: Environment Setup

Create `.env` files in each module directory:

```bash
# Root level and each module
cat > .env << EOF
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
REDIS_URL=redis://localhost:6379
EOF
```

**To get API Keys:**

1. **OpenAI API Key**
   - Visit https://platform.openai.com/api-keys
   - Create new secret key
   - Copy and paste in `.env`

2. **Gemini API Key**
   - Visit https://makersuite.google.com/app/apikey
   - Create new API key
   - Enable Generative Language API

3. **HuggingFace Token**
   - Visit https://huggingface.co/settings/tokens
   - Create new token with read access

### Step 5: Verify Installation

```bash
# Test imports
python -c "import openai; print('✓ OpenAI installed')"
python -c "import langgraph; print('✓ LangGraph installed')"
python -c "import langchain; print('✓ LangChain installed')"

# Run basic test
python main.py
```

### Step 6: Docker Installation (Optional)

```bash
# Install Docker Desktop from https://www.docker.com/products/docker-desktop

# Build and run containers
docker-compose up -d

# Check services
docker-compose ps
```

---

## 🚀 Quick Start

### 1. Hello World with OpenAI

```python
# hello_world_open_ai_api/main.py
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How can I build AI agents?"},
    ]
)

print(response.choices[0].message.content)
```

**Run:**
```bash
cd hello_world_open_ai_api
python main.py
```

### 2. Simple Chat Agent with LangGraph

```python
# langGraph/chat.py - Basic workflow
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# Build graph
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

# Run
result = graph.invoke({"messages": ["Hi! Tell me about AI agents"]})
print(result["messages"][-1].content)
```

**Run:**
```bash
cd langGraph
python chat.py
```

### 3. RAG System (Retrieve-Augment-Generate)

```python
# rag/index.py - Create vector index
from langchain_community.document_loaders import PDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load PDF
loader = PDFLoader("document.pdf")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
chunks = splitter.split_documents(documents)

# Create embeddings and store
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = Chroma.from_documents(chunks, embeddings)

print(f"✓ Indexed {len(chunks)} chunks")
```

**Run:**
```bash
cd rag
python index.py
python chat.py
```

### 4. Async Task Queue

```python
# rag_queue/main.py - Process tasks asynchronously
from rq import Queue
from redis import Redis
from rag_queue.queues.worker import process_document

# Connect to Redis
redis_conn = Redis()
q = Queue(connection=redis_conn)

# Enqueue task
job = q.enqueue(process_document, "large_document.pdf")
print(f"Job ID: {job.id}")

# Check status
while not job.is_finished:
    print(f"Status: {job.get_status()}")
    time.sleep(1)

print(f"Result: {job.result}")
```

**Run with Docker:**
```bash
cd rag_queue
docker-compose up -d
python main.py
```

---

## 📚 Module Guide

### Module 1: Hello World OpenAI API

**Purpose:** Basic LLM integration and API usage

**Key Features:**
- Direct OpenAI API calls
- Gemini API integration
- Prompt engineering strategies
- Token counting

**Files:**
```
hello_world_open_ai_api/
├── main.py              # Basic API calls
├── new_gemini.py        # Gemini integration
├── requirements.txt
└── prompt/              # Prompt strategies
    ├── cot.py           # Chain-of-Thought
    ├── few.py           # Few-shot learning
    ├── zero.py          # Zero-shot
    └── persona.py       # Persona-based
```

**Example:**
```python
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Using Gemini through OpenAI SDK
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {"role": "system", "content": "You are an expert assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ]
)
print(response.choices[0].message.content)
```

---

### Module 2: LangGraph - Agentic Workflows

**Purpose:** Build complex agent workflows with state management

**Key Features:**
- State-based graph execution
- Node composition and edges
- Conditional routing
- Checkpoint management for persistence

**Architecture:**

```
┌──────────────────────────────────────┐
│        START (Initial State)         │
└──────────┬───────────────────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│   Router Node (Conditional Logic)    │
└──┬─────────────┬─────────────────┬──┘
   │             │                 │
   ▼             ▼                 ▼
┌─────────┐  ┌──────────┐  ┌──────────────┐
│ Chatbot │  │ Tool Use │  │ Info Retriev │
│  Node   │  │   Node   │  │     Node     │
└────┬────┘  └────┬─────┘  └──────┬───────┘
     │            │               │
     └────────────┴───────────────┘
           │
           ▼
┌──────────────────────────────────────┐
│   END (Return Final State)           │
└──────────────────────────────────────┘
```

**Files:**
```
langGraph/
├── chat.py                 # Simple sequential workflow
├── chat_checkpoint.py      # Persistent state
└── conditional_chat.py     # Complex routing logic
```

**Example:**
```python
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]

def process_node(state: State):
    # Your processing logic
    return {"messages": ["Response from node"]}

# Build graph
builder = StateGraph(State)
builder.add_node("processor", process_node)
builder.add_edge(START, "processor")
builder.add_edge("processor", END)

graph = builder.compile()
result = graph.invoke({"messages": ["Initial message"]})
```

---

### Module 3: RAG System

**Purpose:** Implement Retrieval Augmented Generation for document-based QA

**Workflow:**

```
User Query
    │
    ▼
┌──────────────────────┐
│ Vector Embedding     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Semantic Search      │
│ (Find similar docs)  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Retrieve Context     │
│ (Top K chunks)       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Generate Response    │
│ (with context)       │
└──────────┬───────────┘
           │
           ▼
Final Answer with Sources
```

**Files:**
```
rag/
├── index.py           # Build vector database
├── chat.py            # Query and retrieve
└── *.pdf              # Sample documents
```

**Example:**
```python
from langchain_community.document_loaders import PDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

# Load and index
loader = PDFLoader("document.pdf")
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
chunks = splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings()
vectorstore = Chroma.from_documents(chunks, embeddings)

# Query
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    chain_type="stuff"
)

answer = qa_chain.run("What is the main topic?")
print(answer)
```

---

### Module 4: Async Task Queue (RAG Queue)

**Purpose:** Process long-running tasks asynchronously using Redis

**Architecture:**

```
┌─────────────────┐
│  Task Producer  │
│   (main.py)     │
└────────┬────────┘
         │ enqueue
         ▼
    ┌─────────┐
    │  Redis  │
    │ Queue   │
    └────┬────┘
         │
    ┌────┴──────────┐
    ▼               ▼
┌────────┐      ┌────────┐
│Worker 1│      │Worker 2│
└────┬───┘      └────┬───┘
     │               │
     └───────┬───────┘
             ▼
    ┌──────────────────┐
    │ Task Processor   │
    │ (queues/worker) │
    └────────┬─────────┘
             │
             ▼
    ┌──────────────────┐
    │  Store Result    │
    │  (database/file) │
    └──────────────────┘
```

**Files:**
```
rag_queue/
├── main.py            # Producer/Consumer
├── server.py          # Task server
├── client/rq_client.py # Client interface
└── queues/worker.py   # Worker implementation
```

**Example:**
```python
from rq import Queue
from redis import Redis
import time

# Connect to Redis
redis_conn = Redis(host='localhost', port=6379)
queue = Queue(connection=redis_conn)

# Define task
def long_running_task(data):
    print(f"Processing: {data}")
    time.sleep(5)
    return f"Completed: {data}"

# Enqueue
job = queue.enqueue(long_running_task, "large dataset")
print(f"Job ID: {job.id}")

# Poll for result
while not job.is_finished:
    print(f"Status: {job.get_status()}")
    time.sleep(1)

print(f"Result: {job.result}")
```

---

### Module 5: Memory Agent

**Purpose:** Maintain persistent context and memory in agent interactions

**Memory Hierarchy:**

```
┌────────────────────────────────┐
│   Short-term Memory (Current)  │
│  - Current conversation        │
│  - Active context              │
└────────────────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  Medium-term Memory (Session)  │
│  - User preferences            │
│  - Conversation history        │
│  - Context windows             │
└────────────────────────────────┘
         │
         ▼
┌────────────────────────────────┐
│  Long-term Memory (Persistent) │
│  - Knowledge base              │
│  - User profile                │
│  - Past interactions           │
└────────────────────────────────┘
```

**Example:**
```python
from mem_agent.mem import MemoryAgent

agent = MemoryAgent()

# Store information
agent.remember("user_preference", "likes_concise_answers", True)
agent.remember("domain", "machine_learning", "expertise_level")

# Retrieve
preference = agent.recall("user_preference")
context = agent.get_context()

# Generate response with memory
response = agent.generate_response("Explain neural networks", context)
```

---

### Module 6: Voice Agents

**Purpose:** Enable voice input/output capabilities

**Processing Pipeline:**

```
┌──────────────┐
│Voice Input   │
└──────┬───────┘
       │
       ▼
┌──────────────────────┐
│Speech Recognition    │
│(audio → text)        │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│NLP Processing        │
│(understand intent)   │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│LLM Generation        │
│(generate response)   │
└──────┬───────────────┘
       │
       ▼
┌──────────────────────┐
│Text-to-Speech        │
│(text → audio)        │
└──────┬───────────────┘
       │
       ▼
┌──────────────┐
│Voice Output  │
└──────────────┘
```

**Example:**
```python
import speech_recognition as sr
import pyttsx3
from openai import OpenAI

# Speech to text
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio)

# Process with LLM
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": text}]
)

# Text to speech
engine = pyttsx3.init()
engine.say(response.choices[0].message.content)
engine.runAndWait()
```

---

### Module 7: Ollama - Local LLMs

**Purpose:** Run open-source LLMs locally without API keys

**Installation:**

```bash
# Download Ollama from https://ollama.ai

# Pull a model
ollama pull mistral
ollama pull llama2

# Run server
ollama serve

# In another terminal, test
curl http://localhost:11434/api/generate -d '{"model":"mistral","prompt":"Tell me about AI"}'
```

**Example:**
```python
import ollama

response = ollama.generate(
    model="mistral",
    prompt="Explain machine learning in simple terms"
)

print(response['response'])
```

---

## 🔧 Configuration

### Environment Variables

Create `.env` files with the following variables:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key
OPENAI_MODEL=gpt-4o-mini

# Gemini Configuration
GEMINI_API_KEY=your-gemini-key
GEMINI_MODEL=gemini-3-flash-preview

# HuggingFace Configuration
HUGGINGFACE_API_KEY=hf_your-token
HUGGINGFACE_MODEL=mistral-7b

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# Application Settings
LOG_LEVEL=INFO
DEBUG=False
MAX_TOKENS=2048
TEMPERATURE=0.7
TOP_P=0.9

# RAG Settings
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_DOCUMENTS=3

# Voice Settings
SPEECH_RECOGNITION_LANGUAGE=en-US
TTS_RATE=150
```

### Model Configuration

```python
# OpenAI Models
OPENAI_MODELS = {
    "gpt-4o": {"context": 128000, "cost": "high"},
    "gpt-4o-mini": {"context": 128000, "cost": "low"},
    "gpt-3.5-turbo": {"context": 4096, "cost": "low"}
}

# Gemini Models
GEMINI_MODELS = {
    "gemini-pro": {"context": 32000},
    "gemini-pro-vision": {"context": 32000},
    "gemini-3-flash": {"context": 1000000}
}

# Local Models (Ollama)
LOCAL_MODELS = {
    "mistral": {"params": 7, "speed": "fast"},
    "llama2": {"params": 7, "speed": "medium"},
    "neural-chat": {"params": 7, "speed": "fast"}
}
```

---

## 💡 Advanced Usage

### 1. Multi-Agent Collaboration

```python
from langgraph.graph import StateGraph

class MultiAgentState(TypedDict):
    task: str
    agents_output: dict
    final_decision: str

# Agent 1: Analysis
def analyst(state):
    # Analyze task
    return {"agents_output": {"analyst": "analysis result"}}

# Agent 2: Planning
def planner(state):
    # Create plan
    return {"agents_output": {**state["agents_output"], "planner": "plan"}}

# Agent 3: Execution
def executor(state):
    # Execute plan
    return {"agents_output": {**state["agents_output"], "executor": "result"}}

# Coordinator
def coordinator(state):
    outputs = state["agents_output"]
    decision = f"Final decision based on: {outputs}"
    return {"final_decision": decision}

# Build workflow
builder = StateGraph(MultiAgentState)
builder.add_node("analyst", analyst)
builder.add_node("planner", planner)
builder.add_node("executor", executor)
builder.add_node("coordinator", coordinator)

# Chain: Analyst → Planner → Executor → Coordinator
builder.add_edge(START, "analyst")
builder.add_edge("analyst", "planner")
builder.add_edge("planner", "executor")
builder.add_edge("executor", "coordinator")
builder.add_edge("coordinator", END)

graph = builder.compile()
result = graph.invoke({"task": "Build an AI system"})
```

### 2. Advanced RAG with Metadata Filtering

```python
from langchain_community.vectorstores import Chroma

# Create vectors with metadata
metadata_filtered_retriever = vectorstore.as_retriever(
    search_type="mmr",  # Maximum marginal relevance
    search_kwargs={
        "k": 5,
        "fetch_k": 20,
        "filter": {"source": "technical_docs"}
    }
)

# Advanced query
results = metadata_filtered_retriever.get_relevant_documents(
    "Query with specific filters"
)
```

### 3. Tool Use and Function Calling

```python
from langchain.agents import AgentExecutor, create_tool_use_agent
from langchain.tools import Tool

# Define tools
def search_web(query: str) -> str:
    """Search the web for information"""
    return f"Web results for: {query}"

def calculate(expression: str) -> str:
    """Evaluate mathematical expressions"""
    return str(eval(expression))

tools = [
    Tool(name="WebSearch", func=search_web, description="Search web"),
    Tool(name="Calculator", func=calculate, description="Calculate math")
]

# Create agent
agent = create_tool_use_agent(llm, tools)
executor = AgentExecutor.from_agent_and_tools(agent, tools)

# Run with tools
result = executor.run("What is 2+2 and search for latest AI news")
```

### 4. Streaming Responses

```python
from openai import OpenAI

client = OpenAI()

# Stream responses
with client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Write a poem"}],
    stream=True
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

### 5. Context Window Management

```python
from langchain.memory import ConversationBufferWindowMemory

# Keep only last 5 messages
memory = ConversationBufferWindowMemory(
    k=5,  # Keep 5 messages
    memory_key="chat_history",
    return_messages=True
)

# Use in chain
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
```

---

## 🎨 Architecture Diagrams

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        User Interface                         │
│              (CLI / Web / Voice / Mobile)                    │
└───────────────┬────────────────────────────┬─────────────────┘
                │                            │
┌───────────────▼────────────────────────────▼─────────────────┐
│                    Agent Orchestration                        │
│  (LangGraph - State, Routing, Workflow)                       │
└───────────────┬────────────────────────────┬─────────────────┘
                │                            │
      ┌─────────▼─────────┐      ┌──────────▼──────────┐
      │   Tool Layer      │      │   Memory Layer      │
      │  - Web Search     │      │  - Short-term       │
      │  - Code Exec      │      │  - Long-term        │
      │  - File I/O       │      │  - RAG Indexes      │
      └─────────┬─────────┘      └──────────┬──────────┘
                │                           │
      ┌─────────▼────────────────────────────▼─────────┐
      │           LLM Layer Integration                │
      │  ┌──────────┐ ┌──────────┐ ┌──────────┐       │
      │  │ OpenAI   │ │ Gemini   │ │ Ollama   │       │
      │  └──────────┘ └──────────┘ └──────────┘       │
      └─────────┬────────────────────────┬─────────────┘
                │                        │
      ┌─────────▼────────────────────────▼─────────┐
      │         Infrastructure Layer               │
      │  ┌────────────┐ ┌──────────┐ ┌──────────┐  │
      │  │ Redis      │ │ Vector DB│ │ Database │  │
      │  └────────────┘ └──────────┘ └──────────┘  │
      └──────────────────────────────────────────────┘
```

### Data Flow Diagram

```
Input
  │
  ▼
┌─────────────────┐
│ Preprocessing   │ (Tokenization, Encoding)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Context Retrieval│ (RAG, Memory)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ LLM Processing   │ (Generation)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Post-processing │ (Formatting, Validation)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Memory Update   │ (Store context)
└────────┬────────┘
         │
         ▼
Output (Text/Voice/Action)
```

---

## 🐳 Docker Support

### Docker Compose Services

```yaml
# docker-compose.yml
version: '3.8'
services:
  redis:
    image: redis:latest
    ports:
      - "6379:6379"
  
  chroma-db:
    image: chromadb/chroma:latest
    ports:
      - "8000:8000"
  
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
```

**Start Services:**

```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f service_name

# Stop all services
docker-compose down
```

---

## 🧪 Testing

### Unit Tests

```python
# test_agents.py
import pytest
from hello_world_open_ai_api.main import get_response

def test_basic_response():
    response = get_response("Hello")
    assert response is not None
    assert len(response) > 0

def test_specific_model():
    response = get_response("Test query", model="gpt-4o-mini")
    assert "model" in response or response is not None

# Run tests
pytest -v test_agents.py
```

### Integration Tests

```python
# test_integration.py
def test_rag_pipeline():
    # Load documents
    vectorstore = setup_vectorstore()
    
    # Query
    results = vectorstore.similarity_search("test query")
    
    # Assert
    assert len(results) > 0
    assert "content" in results[0]

# Run
pytest -v test_integration.py -s
```

---

## Performance Optimization

### 1. Caching Responses

```python
from functools import lru_cache
import hashlib

@lru_cache(maxsize=128)
def cached_completion(prompt: str) -> str:
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    ).choices[0].message.content
```

### 2. Batch Processing

```python
# Process multiple queries efficiently
from langchain_core.runnables import RunnableBatch

prompts = ["Query 1", "Query 2", "Query 3"]
batch_results = chain.batch(prompts, config={"max_concurrency": 5})
```

### 3. Token Optimization

```python
import tiktoken

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

# Optimize prompts
if count_tokens(prompt) > 4000:
    prompt = truncate_prompt(prompt, max_tokens=3000)
```

---

## 📊 Monitoring and Logging

```python
import logging
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agentic_ai.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Log agent activities
logger.info(f"Agent started: {agent_name}")
logger.info(f"Query: {user_query}")
logger.info(f"Response time: {response_time}ms")
logger.warning(f"Token limit approaching: {token_count}/{max_tokens}")
logger.error(f"API error: {error_message}")
```

---

## 🔒 Security Best Practices

1. **Never commit `.env` files** - Use `.gitignore`
2. **Rotate API keys regularly**
3. **Use environment-specific configurations**
4. **Validate user inputs** before processing
5. **Implement rate limiting** on API calls
6. **Use HTTPS** for API calls
7. **Enable audit logging** for sensitive operations

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 📚 Additional Resources

### Documentation & Guides
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com)
- [LangGraph Getting Started](https://langchain-ai.github.io/langgraph/)
- [Google Generative AI](https://ai.google.dev)

### Community & Support
- [OpenAI Community Forum](https://community.openai.com)
- [LangChain Discord](https://discord.gg/cU2adEKapD)
- [GitHub Issues](https://github.com/technopradyumn/agentic_ai/issues)

### Related Projects
- [Ollama](https://ollama.ai) - Run local LLMs
- [Langchain](https://langchain.com) - LLM Framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Agentic Workflows
- [ChromaDB](https://www.trychroma.com) - Vector Database

---

## 🙋 FAQ

**Q: Do I need paid API keys?**
A: OpenAI and Gemini require API keys (paid/free tier). Ollama is completely free and runs locally.

**Q: What are system requirements?**
A: Minimum 4GB RAM, Python 3.8+. For local LLMs (Ollama), 16GB+ RAM recommended.

**Q: How do I switch between different LLM providers?**
A: Use environment variables or configuration files. See [Configuration](#configuration) section.

**Q: Can I run this on Windows/Mac/Linux?**
A: Yes! All modules are cross-platform compatible.

**Q: How do I troubleshoot import errors?**
A: Ensure virtual environment is activated and all dependencies installed: `pip install -r requirements.txt`

**Q: What's the difference between RAG and fine-tuning?**
A: RAG retrieves external documents at query time (flexible, no training). Fine-tuning updates model weights (requires training data, more permanent).

---

<div align="center">

### ⭐ If you found this project helpful, please star it on GitHub!

**Built with ❤️ by [Pradyumn](https://github.com/technopradyumn)**

[![GitHub](https://img.shields.io/badge/GitHub-technopradyumn-blue?logo=github&style=flat-square)](https://github.com/technopradyumn)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pradyumn-blue?logo=linkedin&style=flat-square)](https://linkedin.com/in/pradyumn)

</div>
