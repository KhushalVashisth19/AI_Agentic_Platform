from abc import ABC, abstractmethod

class WorkflowFetcher(ABC):
    def fetch_workflow(self, workflow_id : str) -> dict:
        pass

class InMemoryWorkflowFetcher(WorkflowFetcher):
    sample_DB = {
        "wf_123" : {"id":"wf_123", "steps":["TaskA", "TaskB"]},
        "wf_456" : {"id":"wf_456", "steps":["TaskC", "TaskD"]}
    }
    def fetch_workflow(self, workflow_id:str) -> dict:
        return self.sample_DB.get(workflow_id)      