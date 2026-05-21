from google import genai
import ollama


def get_gemini_llm_gap_analysis(model, jira_user_story, reterived_docs):
    prompt = f"""
    You are a QA requirement validator. 
    BDD scenario: {jira_user_story["description"]}
    Reterived telecom standard: {reterived_docs}
    Identify: 
        1. covered requirements
        2. missing requirements
        3. edge cases
        4. non-functional gaps
    """

    client = genai.Client(api_key="******")

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={"temperature": 0.8}
    )

    return response.text


def get_ollama_llm_gap_analyis(model, jira_user_story, reterived_docs):
    prompt = f"""
    You are a QA requirement validator. 
    BDD scenario: {jira_user_story["description"]}
    Reterived telecom standard: {reterived_docs}
    Identify: 
        1. covered requirements
        2. missing requirements
        3. edge cases
        4. non-functional gaps
    """
    response = ollama.chat(model=model,
                           messages=[
                               {
                                   "role": "user",
                                   "content": prompt
                               }
                           ]
                           )

    return response["message"]["content"]
