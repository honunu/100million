from add_100_million_alien.models import Alien, generate_aliens
from cache.inmemorycache import InMemoryCache
from utils import timing_log
import aiohttp
import asyncio

cache = InMemoryCache()

aliens = generate_aliens()


async def add_alien(alien: Alien):
    cache.set(alien.name, alien.age)


async def download():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8000/files/giphy.gif") as response:
            body = await response.read()
            return body


@timing_log
async def event_loop_run():
    coroutines = [add_alien(alien) for alien in aliens]
    results = await asyncio.gather(*coroutines)
    print(f"cache size is {cache.size}")


@timing_log
async def event_loop_download():
    coroutines = [download() for i in range(1000)]

    results = await asyncio.gather(*coroutines)

    size = 0
    for result in results:
        size = size + len(result)

    print(f"{size/1024/1024} MBytes downloaded")


# asyncio.run(event_loop_run())
asyncio.run(event_loop_download())
