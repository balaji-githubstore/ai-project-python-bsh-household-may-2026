from app.services.prompt_loader import load_prompt,analyze_prompt_loader
from app.services.ollama_services import llm


def analyze_requirment_agent(ticket):
    # prompt template build
    prompt = analyze_prompt_loader()

    # create chain
    chain = prompt | llm

    agent_prompt = load_prompt(".github/agents/jira-analysis.agent.md")
    response=chain.invoke({
        "agent_prompt": agent_prompt,
        "user_task": ticket,
    })
    return response


# print(analyze_requirment_agent("""
# Feature: Recharge Plan Display
# Scenario: Load recharge plans for the selected circle
# Given a user selects a telecom circle
# When the recharge plans screen is opened
# Then the system shall display recharge plans applicable to the selected circle
# """))
