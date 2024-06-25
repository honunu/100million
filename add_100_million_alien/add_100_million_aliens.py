from add_100_million_alien.models import generate_aliens
from user_repository import AlienRepo, AlienRepoInMemory
import time

from utils import timing_log


@timing_log
def add_alien_batch_and_clean(alien_list, alien_repo):
    start_time = time.perf_counter()

    alien_repo.add_alien_batch(alien_list)

    print(f'当前 {alien_repo.count_all_alien()} 个用户')
    print(f'消耗时间 {time.perf_counter() - start_time} 秒')

    alien_repo.remove_all_alien()

    alien_repo.close()


aliens = generate_aliens()
add_alien_batch_and_clean(alien_list=aliens,
                          alien_repo=AlienRepo())

add_alien_batch_and_clean(alien_list=aliens,
                          alien_repo=AlienRepoInMemory())
