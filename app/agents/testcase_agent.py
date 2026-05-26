from app.services.prompt_loader import generate_testcase_prompt_loader, load_prompt
from app.services.ollama_services import llm


def generate_testcase_agent(requirment):
    # prompt template build
    prompt = generate_testcase_prompt_loader()

    # create chain
    chain = prompt | llm

    agent_prompt = load_prompt(".github/agents/create-testcase.agent.md")
    response=chain.invoke({
        "agent_prompt": agent_prompt,
        "user_task": requirment,
    })

    response=str(response).replace("```csv","").replace("```","")
    return response


# print(generate_testcase_agent("login testcase for facebook"))