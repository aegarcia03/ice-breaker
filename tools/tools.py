# Get a name and find URL
from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str) -> str:
    """Searches for LinkedIn or Twitter profile page"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res