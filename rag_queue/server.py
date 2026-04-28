from fastapi import FastAPI, Query
from .queues.worker import process_query
from .client.rq_client import queue
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Server is up and running!"}


@app.post("/chat")
def chat(
        query: str = Query(..., description="The chat query of the user")
):
    job = queue.enqueue(process_query, query)
    return {"job_id": job.id, "status": "Your query is being processed. Please check back later with the job ID to get the response."}

@app.get("/result")
def get_result(
    job_id: str = Query(..., description="The job ID returned when the query was submitted")
):
    job = queue.fetch_job(job_id = job_id)
    result = job.return_value
    return {"status": job.get_status(), "result": result}
    

