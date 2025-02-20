import logging
from abc import ABC, abstractmethod

logging.basicConfig(level = logging.INFO)
class WorkflowExecutor(ABC):
    @abstractmethod
    def execute(self, workflow_id:str, workflow_data:dict) ->None:
        pass

class InMemoryWorkflowExecutor(WorkflowExecutor):
    def execute(self, workflow_id:str, workflow_data:dict)->None:
        logging.info(f"Executing workflow {workflow_id} : {workflow_data}")