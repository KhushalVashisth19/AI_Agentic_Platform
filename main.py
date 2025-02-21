from fastapi import FastAPI, HTTPException, Depends
from fetcher import InMemoryWorkflowFetcher  
from executor import InMemoryWorkflowExecutor  
from services import WorkflowExecutionManager  
import asyncio
import httpx

app = FastAPI() 

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}

def get_workflow_execution_manager():
    fetcher = InMemoryWorkflowFetcher()
    executor = InMemoryWorkflowExecutor()
    return WorkflowExecutionManager(fetcher, executor)

@app.post("/execute/{workflow_id}")  
async def execute_workflow(workflow_id: str, wem:WorkflowExecutionManager = Depends(get_workflow_execution_manager)): #Inject dependency
    try:
        response =  await wem.execute_workflow(workflow_id)
        return response
    except ValueError as e:  
        raise HTTPException(status_code=404, detail=str(e))  
    
