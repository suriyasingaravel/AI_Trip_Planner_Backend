import os
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv()

_search = TavilySearch(
    tavily_api_key=os.getenv("TAVILY_API_KEY"),
    max_results=10,
    topic="general"
)

def web_search(query: str) -> str:
    results = _search.invoke(query).get("results", [])
    return " ".join(item["content"] for item in results[:5])
