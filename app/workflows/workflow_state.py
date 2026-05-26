from typing import TypedDict

class WorkflowState(TypedDict):
    ticket:str
    requirement:str
    rules: str
    script: str
    reviewed_testcase: str
