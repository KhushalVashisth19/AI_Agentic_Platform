import logging
import asyncio
from fetcher import InMemoryWorkflowFetcher
from executor import InMemoryWorkflowExecutor
from services import WorkflowExecutionManager

async def test_workflow_execution():
    fetcher = InMemoryWorkflowFetcher()
    executor = InMemoryWorkflowExecutor()
    wem = WorkflowExecutionManager(fetcher, executor)

    workflow_id = "wf_456"   #Example
    print("Evaluating workflow...")
    response = await wem.execute_workflow(workflow_id) 
    assert response == {"status": "Workflow executed", "workflow_id": workflow_id}
    logging.info(response)

if __name__ == "__main__":
    asyncio.run(test_workflow_execution())
