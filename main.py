from src.tools.tools import tavily_web_search, extract_scrape_url
from rich import print


result =extract_scrape_url.invoke({
    "url": "https://www.crescendo.ai/news/latest-ai-news-and-updates"
})

print(result)