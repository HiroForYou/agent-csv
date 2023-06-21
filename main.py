from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

from agent import getAgentResponse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    user: str
    question: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {
        "message": "This is /path endpoint, use a post request to transform the text to uppercase"
    }


@app.post("/agentResponse")
async def agent_post(query: Query):
    response = getAgentResponse(question=query.question, user=query.user)
    return {"response": response}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {
        "message": f"This is /path/{path_id} endpoint, use post request to retrieve result"
    }
