from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.core.router import AgentRouter
from app.workflows.workflow_engine import WorkflowEngine

app = FastAPI()

router = AgentRouter()
workflow_engine = WorkflowEngine(router)

class WorkflowItem(BaseModel):
    agent: str
    task: str

class WorkflowRequest(BaseModel):
    workflow: List[WorkflowItem]

@app.get("/")
async def root():
    return {"status": "running"}

@app.post("/workflow")
async def workflow(data: WorkflowRequest):

    result = await workflow_engine.run([
        {
            "agent": item.agent,
            "task": item.task
        }
        for item in data.workflow
    ])

    return {
        "success": True,
        "data": result
    }