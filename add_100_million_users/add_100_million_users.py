from user_repository import UserRepository, UserRepositoryOneConnection
import time

user_amount_list = [1, 1000, 10_000]
user_repo = UserRepository()
user_repo_one_connection = UserRepositoryOneConnection()


def add_user_and_clean(user_amount_list, user_repo):
    for user_amount in user_amount_list:
        print(f"新增 {user_amount} 个外星人用户")
        start_time = time.time()

        for i in range(user_amount):
            user = {'Name': f'小灰人{i}号', 'Age': 1}
            user_repo.add_user(user)

        print(f'当前 {user_repo.count_all_user()} 个用户')
        print(f'消耗时间 {time.time() - start_time} 秒')

        user_repo.remove_all_user()

    user_repo.close()


# add_user_and_clean(user_amount_list, user_repo)
add_user_and_clean(user_amount_list=user_amount_list,
                   user_repo=user_repo_one_connection)
