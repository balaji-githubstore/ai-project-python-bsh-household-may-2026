from pathlib import Path
from langchain_core.prompts import PromptTemplate

def load_prompt(file_path: str):
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def analyze_prompt_loader():
    prompt_template = """
    {agent_prompt}

    Analyze the Jira ticket.

    Task:
    {user_task}

    Generate:
    1. Functional requirements
    2. Edge cases
    3. Validation rules
    4. Test scenarios
    """
    prompt = PromptTemplate(
        input_variables=["agent_prompt", "user_task"],
        template=prompt_template
    )
    return prompt


def generate_testcase_prompt_loader():
    prompt_template = """
    You are an expert QA automation engineer. 

    Follow these project instructions strictly:

    {agent_prompt}

    Task:
    {user_task}
    """

    prompt = PromptTemplate(
        input_variables=["agent_prompt", "user_task"],
        template=prompt_template
    )
    return prompt

def generate_test_script_prompt_loader():
    prompt_template = """
    {agent_prompt}

    Requirements:
    {requirements}

    Internal Rules:
    {rules}

    Generate Selenium Python automation code.
    """

    prompt = PromptTemplate(
        input_variables=[
            "agent_prompt",
            "requirements",
            "rules"
        ],
        template=prompt_template
    )
    return prompt

def pr_review_prompt_loader():
    prompt_template = """
    {agent_rules}

    RAG_Rules:
    {rules}

    Code:
    {code}

    Check:
    1. Assertions
    2. Logging
    3. Naming standards
    4. Selenium best practices
    5. Exception handling

    Generate:
    - Compliance score
    - Issues found
    - Improvements
    """

    prompt = PromptTemplate(
        input_variables=[
            "agent_rules",
            "rules",
            "code"
        ],
        template=prompt_template
    )
    return prompt

def review_testcase_prompt_loader():
    prompt_template = """
    You are an expert QA automation engineer. 

    Follow these project instructions strictly:

    {agent_prompt}

    Task:
    {user_task}
    """

    prompt = PromptTemplate(
        input_variables=["agent_prompt", "user_task"],
        template=prompt_template
    )
    return prompt