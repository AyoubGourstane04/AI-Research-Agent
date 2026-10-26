from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime
import wikipedia as wikipedia_client


ddg_search = DuckDuckGoSearchRun()

wikipedia_wrapper = WikipediaAPIWrapper(
    wiki_client=wikipedia_client,
    top_k_results=2,
    doc_content_chars_max=100,
)

wikipedia_search = WikipediaQueryRun(
    api_wrapper=wikipedia_wrapper
)


@tool
def search(query: str) -> str:
    """Search the web for current information about a topic."""
    return ddg_search.run(query)

@tool
def wikipedia(query: str) -> str:
    """Search Wikipedia for background information about a topic."""
    return wikipedia_search.run(query)

@tool 
def save_to_txt(data: str, filename: str="research_output.txt") -> str:
    """Save structured research data to a text file."""
    
    timestamp = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"

agent_tools = [
    search,
    wikipedia,
    save_to_txt,
]


