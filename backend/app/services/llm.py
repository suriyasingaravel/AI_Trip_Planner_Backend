import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import tool
from .weather import get_weather
from .search import web_search
from .hotels import find_hotels
from dotenv import load_dotenv
load_dotenv()

# ---- Wrap helper functions as tools for ReAct agent ----
@tool
def realtime_weather(city: str) -> str:
    "Weather snapshot for a city"
    return get_weather(city)

@tool
def tavily_search(q: str) -> str:
    "Tavily general search"
    return web_search(q)

@tool
def hotel_suggest(city: str) -> str:
    "Hotel & restaurant suggestions"
    return find_hotels(city)

TOOLS = [realtime_weather, tavily_search, hotel_suggest]

# ---- Configure Gemini 1.5-Flash ----
_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

_prompt = hub.pull("hwchase17/react")
_agent = create_react_agent(_llm, TOOLS, _prompt)
_executor = AgentExecutor(agent=_agent, tools=TOOLS, verbose=True)

def build_itinerary(city, duration, interests, time_pref, budget) -> str:
    user_query = (
        f"I'm visiting {city} for {duration} days. "
        f"My interests are {interests}. "
        f"I prefer {time_pref} activities. "
        f"Budget: {budget if budget else 'flexible'}. "
        "Generate an optimized day-by-day itinerary with weather-aware activity choices, "
        "restaurant picks, estimated per-item costs (INR) and short justifications."
    )
    response = _executor.invoke({"input": user_query})
    return response["output"]
