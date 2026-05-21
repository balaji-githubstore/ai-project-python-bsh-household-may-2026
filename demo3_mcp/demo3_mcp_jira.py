"""
pip install mcp

-- code to get the mcp-atlassian tools like get_issue, add_comments

"""
import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import json

class MCPClient:

    def run(self):
        asyncio.run(self._run())

    async def _run(self):
        server = StdioServerParameters(
            command="uvx",
            args=["mcp-atlassian"],
            env={
                "JIRA_URL": "https://dbalacloud.atlassian.net/",
                "JIRA_USERNAME": "dbala.cloud@gmail.com",
                "JIRA_API_TOKEN": "****"
                }
        )
        # connect to mcp server, start the mcp process
        async with stdio_client(server) as (read,write):

            # list the jira tools, functions 
            async with ClientSession(read,write) as session:
                await session.initialize()
                result= await session.call_tool(
                     "jira_get_issue",
                     {"issue_key":"KAN-5"}
                     )
                print(result.content[0].text)
                print("*"*50)   

client=MCPClient()
client.run()

