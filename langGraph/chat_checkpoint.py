from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

from langgraph.checkpoint.mongodb import MongoDBSaver
from pymongo import MongoClient

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):

    print("\n===== CHAT HISTORY =====")

    for i, msg in enumerate(state["messages"], 1):
        print(f"{i}. {msg.type.upper()}: {msg.content}")

    print("========================")

    response = llm.invoke(state["messages"])

    return {"messages": [response]}

graph_build = StateGraph(State)

graph_build.add_node("chatbot", chatbot)
graph_build.add_edge(START, "chatbot")
graph_build.add_edge("chatbot", END)

graph = graph_build.compile()

def compile_graph_with_checkpointer(checkpointer):
    return graph_build.compile(checkpointer=checkpointer)

DB_URI = "mongodb://admin:admin@localhost:27017"

with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(
        checkpointer=checkpointer
    )

    config = {
        "configurable": {
            "thread_id": "pradyumn"
        }
    }

    for chunk in graph_with_checkpointer.stream(
        {"messages": ["Hi, What am I learning?"]},
        config=config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()