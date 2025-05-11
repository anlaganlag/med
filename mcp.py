from composio_openai import ComposioToolSet, App, Action
from openai import OpenAI
import os

# Set your API keys here
OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your actual OpenAI API key
COMPOSIO_API_KEY = "6uqs6aifix4ursj7plxzy"   # Your Composio API key

# Initialize clients with API keys
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY))
composio_toolset = ComposioToolSet(api_key=COMPOSIO_API_KEY)

tools = composio_toolset.get_tools(actions=[Action.GITHUB_STAR_A_REPOSITORY_FOR_THE_AUTHENTICATED_USER])

task = "Star a repo composiohq/composio on GitHub"

response = openai_client.chat.completions.create(
    model="gpt-4o",
    tools=tools,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": task},
    ],
)

result = composio_toolset.handle_tool_calls(response)
print(result)
