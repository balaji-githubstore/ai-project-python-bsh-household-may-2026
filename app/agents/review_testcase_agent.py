from app.services.prompt_loader import load_prompt,review_testcase_prompt_loader
from app.services.ollama_services import llm


def review_testcase_agent(ticket):
    # prompt template build
    prompt = review_testcase_prompt_loader()

    # create chain
    chain = prompt | llm

    agent_prompt = load_prompt(".github/agents/tc-review.agent.md")
    response=chain.invoke({
        "agent_prompt": agent_prompt,
        "user_task": ticket,
    })
    return response

