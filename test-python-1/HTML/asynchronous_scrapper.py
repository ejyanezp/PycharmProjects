import aiohttp
import asyncio
import async_timeout
import time


async def fetch_page(session, url):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f'Page took {time.time() - page_start}, status: {response.status}')
            return await response.text()


async def get_multiple_pages(*urls):
    tasks = []
    global loop
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        # launch the coroutines, control de timeout
        grouped_tasks = asyncio.gather(*tasks)
        # await: get_multiple_pages finishes only when all the created coroutines finish
        return await grouped_tasks


loop = asyncio.get_event_loop()
my_urls = [f'http://books.toscrape.com/catalogue/page-{page_number}.html' for page_number in range(1, 50)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(*my_urls))
print(f'All took {time.time() - start}')
