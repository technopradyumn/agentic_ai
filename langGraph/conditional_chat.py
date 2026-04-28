from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Optional , Literal
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
import os


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"), 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]

def chatbot(state: State):

    response = client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who answers user query."},
            {"role": "user", "content": state.get("user_query")}
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def evaluate_response(state: State)-> Literal["chatbot_gemini", "endnode"]:
    if True:
        return "endnode"
    return "chatbot_gemini"



def chat_gemini(state: State):
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": state.get("User query") }
        ]
    )

    state["llm_output"] = response.choices[0].message.content
    return state

def endnode(state: State):
    return state

graph_build = StateGraph(State)

graph_build.add_node("chatbot", chatbot)
graph_build.add_node("chatbot_gemini", chat_gemini)
graph_build.add_node("endnode", endnode)


graph_build.add_edge(START, "chatbot")
graph_build.add_conditional_edges("chatbot", evaluate_response)

graph_build.add_edge("chatbot_gemini", "endnode")
graph_build.add_edge("endnode",END)

graph = graph_build.compile()

update_state = graph.invoke(State({"user_query":"What is  2 + 5?"}))

print(update_state)