import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters
import json

class MCPClient:

    def run(self,issue_id):
        return asyncio.run(self._run(issue_id))

    async def _run(self,issue_id):
        server = StdioServerParameters(
            command="uvx",
            args=["mcp-atlassian"],
            env={
                "JIRA_URL": "https://dbalacloud.atlassian.net/",
                "JIRA_USERNAME": "dbala.cloud@gmail.com",
                "JIRA_API_TOKEN": "*****"
            }
        )
        # connect to mcp server, start the mcp process
        async with stdio_client(server) as (read,write):

            # list the jira tools, functions 
            async with ClientSession(read,write) as session:
                await session.initialize()
                result= await session.call_tool(
                     "jira_get_issue",
                     {"issue_key":issue_id}
                     )
                result=json.loads(result.content[0].text)
        return result
