from fastapi import FastAPI,Body
from ollama import Client

app = FastAPI()
client = Client(
    host="http://localhost:11434/"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/contactus")
def contact_us():
    return {
        "name": "Technopradyumn",
        "email": "technopradyumn@gmail.com", 
        "message": "Thank you for contacting us!",
        "success": True
    }

@app.post("/chat")
def chat(
        message: str = Body(...,description="The message to send to the model.")
):
   response = client.chat(model="gemma:2b", messages=[
    
    {"role": "user", "content": message}
                                            
   ])

   return {"response": response.message.content}