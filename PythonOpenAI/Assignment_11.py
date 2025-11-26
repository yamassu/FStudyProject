# Assignment_11.py

# Required installations:
# pip install langchain openai requests tavily-api tiktoken langchain-openai langchain-community langchain-tavily langgraph pyowm

import os
from langchain.tools import tool
from langchain_openai import AzureChatOpenAI
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent

# Step 1: Setup API keys
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_DEPLOYMENT_NAME"] = "GPT-4o-mini"
os.environ["OPENWEATHERMAP_API_KEY"] = ""
os.environ["TAVILY_API_KEY"] = ""

# Step 2: Define weather tool using Langchain wrapper
weather = OpenWeatherMapAPIWrapper()

@tool
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    print(f"get_weather tool calling: Getting weather for {city}")
    return weather.run(city)

# Step 3: Initialize Tavily search tool
tavily_search_tool = TavilySearch(
    max_results=1,
    topic="general",
)

# Step 4: Initialize Azure OpenAI LLM
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_DEPLOYMENT