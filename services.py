import asyncio
import logging
from fetcher import WorkflowFetcher
from executor import WorkflowExecutor

logging.basicConfig(level = "INFO")
class WorkflowExecutionManager:
    def __init__(self, fetcher:WorkflowFetcher, executor:WorkflowExecutor):
        self.fetcher = fetcher #Injecting dependency
        self.executor = executor #Injecting dependency

    async def execute_workflow(self, workflow_id: str):
        await asyncio.sleep(2)
        workflow = self.fetcher.fetch_workflow(workflow_id)
        if not workflow:
            raise ValueError("Workflow not found")  
        self.executor.execute(workflow_id, workflow)
        return({"status": "Workflow executed", "workflow_id": workflow_id})

