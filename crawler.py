import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def run_google_search(query: str):
    url = f"https://www.google.com/search?q={query}&hl=en&gl=us"

    config = BrowserConfig(headless=True)
    async with AsyncWebCrawler(config=config) as crawler:
        run_config = CrawlerRunConfig(delay_before_return_html=2)
        result = await crawler.arun(url, config=run_config)

        if result.success:
            print(" Google page loaded.")
            print(result.html[:1000])  
        else:
            print(" Failed to crawl:", result.error)

if __name__ == "__main__":
    query = input("Enter search query: ")
    asyncio.run(run_google_search(query))
