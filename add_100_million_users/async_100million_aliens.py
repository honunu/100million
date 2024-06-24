import asyncio

from add_100_million_users.models import Alien
from cache.inmemorycache import InMemoryCache
from utils import timing_log

cache = InMemoryCache()

alien_count = 100000
alien_list = [Alien(name=f'{i}', age=1) for i in range(alien_count)]


async def add_alien(alien: Alien):
    cache.set(alien.name, alien.age)


@timing_log
async def event_loop_run():
    coroutines = [add_alien(alien) for alien in alien_list]
    results = await asyncio.gather(*coroutines)
    print(f"cache size is {cache.size}")

    print(f"adding {alien_count} aliens finished")


asyncio.run(event_loop_run())
