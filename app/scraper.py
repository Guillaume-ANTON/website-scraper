import aiohttp
import asyncio
from bs4 import BeautifulSoup

data = []

async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.select('a.storylink')
        return [title.text for title in titles]
    
async def scrape():
    async with aiohttp.ClientSession() as session:
        articles = await fetch(session, 'https://news.ycombinator.com/')
        global data
        data = articles
        return articles