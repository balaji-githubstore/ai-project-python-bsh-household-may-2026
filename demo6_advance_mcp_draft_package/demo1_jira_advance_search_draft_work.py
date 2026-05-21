"""
mcp jira query - ticket triage dashboard

features: 
1. fetch jira tickets assigned to current user
2. check local automation script exists or not
3. if script missing --> auto create draft script 

tech:
- JIRA MCP
- Async python 
- local filesystem automation 
"""

import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import json
from pathlib import Path


class MCPClient:

    def __init__(self):
        self.server = StdioServerParameters(
            command="uvx",
            args=["mcp-atlassian"],
            env={
                "JIRA_URL": "https://dbalacloud.atlassian.net/",
                "JIRA_USERNAME": "dbala.cloud@gmail.com",
                "JIRA_API_TOKEN": "*****"
            }
        )
        self.script_folder = Path("./automation_scripts")
        self.script_folder.mkdir(exist_ok=True)

    def assigned_to_me_dashboard(self):
        return asyncio.run(self._assigned_to_me_dashboard())

    async def _assigned_to_me_dashboard(self):
        dashboard = []

        async with stdio_client(self.server) as (read, write):

            # list the jira tools, functions
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(
                    "jira_search",
                    {
                        "jql": "assignee = currentUser() AND status != Done ORDER BY priority DESC"}
                )
                result = json.loads(result.content[0].text)

                issues = result["issues"]

                print(f"Total assigned to me:{len(issues)}")

                for issue in issues:
                    key = issue["key"]
                    summary = issue["summary"]
                    status = issue["status"]["name"]
                    priority = issue["priority"]["name"]

                    print(f"Ticket: {key}")
                    print(f"Summary: {summary}")
                    print(f"Status: {status}")
                    print(f"Priority: {priority}")

                    """
                    check if automation script exists 
                    """
                    script_name = f"{key}.py"
                    script_path = self.script_folder / script_name

                    if script_path.exists():
                        print(f"Automation: Existing scripts found")

                        dashboard.append(
                            {
                                "ticket": key,
                                "summary": summary,
                                "script_status": "Exists"
                            })
                    else:
                        print(f"Automation: No scripts found")
                        print(f"Action: creating automation draft")

                        # create a file with name - {script_name}
                        self._create_draft_script(
                            ticket_id=key,
                            summary=summary,
                            path=script_path
                        )
                        dashboard.append(
                            {
                                "ticket": key,
                                "summary": summary,
                                "script_status": "Draft Created"
                            })
                return dashboard

    def _create_draft_script(self, ticket_id, summary, path):
        """
        create draft selenium python framework
        """
        template = f'''
""" Auto generated draft {summary}"""
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_{str(ticket_id).replace("-", "_")}
    def test_scenario(self):
        print("test")
        # todo - implement automation steps {ticket_id}
'''

        with open(path, "w", encoding="utf-8") as f:
            f.write(template)

        print(f"draft created")


client = MCPClient()
dashboard = client.assigned_to_me_dashboard()
print("\n")
print("="*60)
print("Final Tirage Dashboard")
for item in dashboard:
    print(item["ticket"])
    print(item["summary"])
    print(item["script_status"])
    print("="*60)
