import asyncio
from scraper import MyDramaListScraper

async def main():
    s = MyDramaListScraper()
    soup = await s._make_request('https://mydramalist.com/calendar')
    with open('calendar.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

asyncio.run(main())
