import asyncio

from add_100_million_alien.models import Alien, generate_aliens
from cache.inmemorycache import InMemoryCache
from utils import timing_log

cache = InMemoryCache()

aliens = generate_aliens()
async def add_alien(alien: Alien):
    cache.set(alien.name, alien.age)


@timing_log
async def event_loop_run():
    coroutines = [add_alien(alien) for alien in aliens]
    results = await asyncio.gather(*coroutines)
    print(f"cache size is {cache.size}")


asyncio.run(event_loop_run())
