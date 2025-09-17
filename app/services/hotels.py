from .search import web_search

def find_hotels(city: str) -> str:
    q = f"best mid-range hotels and local restaurants in {city}"
    return web_search(q)
