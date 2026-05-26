from app.workflows.workflow_langgraph import app

print("Starting agentic AI Workflows")

result=app.invoke({})

print("Final Result\n")

print(result)