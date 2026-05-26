from app.workflows.workflow_state import WorkflowState
from langgraph.graph import StateGraph
from app.services.jira_services import MCPClient
from app.agents.analyze_agent import analyze_requirment_agent
from app.rag.retriever import retrieve_rules
from app.agents.testcase_agent import generate_testcase_agent
from app.agents.review_testcase_agent import review_testcase_agent

workflow = StateGraph(WorkflowState)
issue_id = "KAN-5"

"""
jira mcp --> get ticket --> ticket state
analyze requirement --> agent --> requirment state
based on analyze --> fetch rag policies --> rules
generate testcase--> ticket, analyzed requirement
"""

# Step 1


def fetch_ticket(state):
    client = MCPClient()
    ticket = client.get_jira_ticket_content(issue_id)
    return {
        "ticket": ticket
    }


# Step 2
def analyze_requirement(state):
    requirement = analyze_requirment_agent(state["ticket"])
    return {
        "requirement": requirement
    }

# Step 3


def retrieve_internal_polices(state):
    rules = retrieve_rules(state["requirement"])
    return {
        "rules": rules
    }


def generate_testcase(state):
    script = generate_testcase_agent(state["ticket"])

    with open(f"app/data/generated_scripts/new_tc1.csv", "w", encoding="UTF-8") as file:
        file.write(script)

    return {
        "script": script
    }


def review_testcase(state):
    reviewed_testcase = review_testcase_agent(state["script"])
    with open(f"app/data/generated_scripts/tc1_review.txt", "w", encoding="UTF-8") as file:
            file.write(reviewed_testcase)
    return {
            "reviewed_testcase": reviewed_testcase
        }


# review_testcase
# generate_python_script
# review code 
workflow.add_node("fetch_ticket",fetch_ticket)
workflow.add_node("analyze_requirement",analyze_requirement)
workflow.add_node("retrieve_internal_polices",retrieve_internal_polices)
workflow.add_node("generate_testcase",generate_testcase)
workflow.add_node("review_testcase",review_testcase)

workflow.set_entry_point("fetch_ticket")
workflow.add_edge("fetch_ticket","analyze_requirement")
workflow.add_edge("analyze_requirement","retrieve_internal_polices")
workflow.add_edge("analyze_requirement","generate_testcase")
workflow.add_edge("generate_testcase","review_testcase")

workflow.set_finish_point("review_testcase")


app=workflow.compile()