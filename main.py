from fastapi import FastAPI, HTTPException  
from fetcher import InMemoryWorkflowFetcher  
from executor import InMemoryWorkflowExecutor  
from services import WorkflowExecutionManager  
import asyncio

app = FastAPI() 

fetcher = InMemoryWorkflowFetcher()
executor = InMemoryWorkflowExecutor()
wem = WorkflowExecutionManager(fetcher, executor)

@app.post("/execute/{workflow_id}")  
async def execute_workflow(workflow_id: str):
    try:
        response =  await wem.execute_workflow(workflow_id)
        return response
    except ValueError as e:  
        raise HTTPException(status_code=404, detail=str(e))  