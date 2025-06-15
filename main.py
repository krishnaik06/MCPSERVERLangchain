from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], ## Ensure correct absolute path
                "transport":"stdio",
            
            },
            "weather": {
                "url": "http://localhost:8000/mcp",  # Ensure server is running here
                "transport": "streamable_http",
            },
            "cars":{
                "command":"python",
                "args":["cars.py"],
                "transport":"stdio",
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent=create_react_agent(
        model,tools
    )

    while True:
        user_input=input("Enter your query: ")
        if user_input.lower() in ["exit","quit","bye"]:
            break
        else:
            response=await agent.ainvoke(
                {"messages": [{"role": "user", "content": user_input}]}
            )
            print("Response: ", response['messages'][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
