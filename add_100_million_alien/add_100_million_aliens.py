from add_100_million_alien.models import generate_aliens
from user_repository import AlienRepo, AlienRepoInMemory
import time

from utils import timing_log

alien_repo = AlienRepo()
alien_repo_in_memory = AlienRepoInMemory()


def add_user_and_clean(user_repo):
    aliens = generate_aliens()
    for alien in aliens:
        print(f"新增 {aliens.count()} 个外星人用户")

        user_repo.add_alien(alien)

        print(f'当前 {user_repo.count_all_alien()} 个用户')

        user_repo.remove_all_alien()

    user_repo.close()


@timing_log
def add_alien_batch_and_clean(alien_list, alien_repo):
    start_time = time.perf_counter()

    alien_repo.add_alien_batch(alien_list)

    print(f'当前 {alien_repo.count_all_alien()} 个用户')
    print(f'消耗时间 {time.perf_counter() - start_time} 秒')

    alien_repo.remove_all_alien()

    alien_repo.close()


# add_user_and_clean(user_amount_list, user_repo)
# add_user_and_clean(user_amount_list=user_amount_list,
#                    user_repo=user_repo_one_connection)

aliens = generate_aliens()
add_alien_batch_and_clean(alien_list=aliens,
                          alien_repo=alien_repo)

add_alien_batch_and_clean(alien_list=aliens,
                          alien_repo=alien_repo_in_memory)
