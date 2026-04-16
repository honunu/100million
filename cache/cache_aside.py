import time

from add_100_million_alien.user_repository import AlienRepo
from cache.inmemorycache import InMemoryCache

cache = InMemoryCache()
repository = AlienRepo()


class CacheAside:

    # Read from cache, if exists, then return
    # If not exists, read from database and return
    # Write into cache
    def read_procedure(self, user_id):
        cached_user = cache.get(user_id)
        if cached_user:
            return cached_user
        else:
            persisted_user = repository.get_user_by_id_db(user_id=user_id)
            return persisted_user

    # Update in database, then remove cache
    def write_procedure(self, user: dict):
        repository.update_user_by_id_db(user_id=user['ID'], user=user)
        cache.delete(user['ID'])
        return


def add_user(user_amount_list, user_repo):
    for user_amount in user_amount_list:
        print(f"新增 {user_amount} 个外星人用户")
        start_time = time.time()

        for i in range(user_amount):
            user = {'Name': f'小灰人{i}号', 'Age': 1}
            user_repo.add_user(user)

        print(f'当前 {user_repo.count_all_user()} 个用户')
        print(f'消耗时间 {time.time() - start_time} 秒')

def clean_up(user_repo):
    user_repo.remove_all_user()



user_amount_list = [100]
cache_aside = CacheAside()
add_user(user_amount_list=user_amount_list, user_repo=repository)

for i in range(user_amount_list):
    user_id = i
    cache_aside.read_procedure(user_id=user_id)

clean_up()
