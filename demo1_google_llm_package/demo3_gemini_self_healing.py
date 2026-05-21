from selenium import webdriver
from selenium.webdriver.common.by import By
from google import genai
import json


def get_healed_locator(html,failed_locator):
    system_prompt="""
        You are a QA automation expert. 
        Rules:
        - always return only valid JSON
        - Do not include explanation or extra text
        - output must strictly follow this format: 
        {"new_locator":"<xpath>"}
        - xpath must be robust and unique 
    """
    user_prompt=f"""
        A selenium test is failed. 
        old xpath:
        {failed_locator}
        
        html:{html}
        suggest better xpath
    """
    client=genai.Client(api_key="*****")

    response=client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        {
            "role":"system",
            "parts":[{"text":system_prompt}]
        },
        {
             "role":"user",
            "parts":[{"text":user_prompt}]
        }
    ]
    )
    
    result=json.loads(response.text)
    return result["new_locator"]
    
    

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

login_locator="//button[normalize-space()='Submit']"

try:
    driver.find_element(By.XPATH,login_locator).click()
except:
    print("Old locator failed. try self healing using llm")
    html=driver.page_source
    new_locator=get_healed_locator(html=html,failed_locator=login_locator)
    driver.find_element(By.XPATH,new_locator).click()
    
    
    



