import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import json
import os

class MCPClient:

    def get_jira_ticket_content(self, issue_id):
        return asyncio.run(self._ticket_content(issue_id))

    async def _ticket_content(self, issue_id):
        server = StdioServerParameters(
            command="uvx",
            args=["mcp-atlassian"],
            env={
                "JIRA_URL": os.getenv("JIRA_URL"),
                "JIRA_USERNAME": os.getenv("JIRA_EMAIL"),
                "JIRA_API_TOKEN": os.getenv("JIRA_TOKEN")
            }
        )
        # connect to mcp server, start the mcp process
        async with stdio_client(server) as (read, write):

            # list the jira tools, functions
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(
                    "jira_get_issue",
                    {"issue_key": issue_id}
                )
                result = json.loads(result.content[0].text)
                ticket_content = f"""
                Summary: {result["summary"]}
                Description: {result["description"]}
            """
        return ticket_content
    


# client=MCPClient()
# result=client.get_jira_ticket_content("KAN-5")
# print(result)