from dotenv import load_dotenv
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("\nChatbot received:", state)
    return {"messages": ["Hi, This is a chatbot!"]}

def samplenode(state: State):
    print("\nSample node received:", state)
    return {"messages": ["This is a sample node!"]}

graph_build = StateGraph(State)

graph_build.add_node("chatbot", chatbot)
graph_build.add_node("samplenode", samplenode)

graph_build.add_edge(START, "chatbot")
graph_build.add_edge("chatbot", "samplenode")
graph_build.add_edge("samplenode", END)

graph = graph_build.compile()

update_state = graph.invoke({"messages": ["Hi, My name is Pradyumn"]})

print(update_state)