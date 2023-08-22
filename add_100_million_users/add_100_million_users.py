from user_repository import add_user, count_all_user, remove_all_user
import time


user_amount_list = [1, 1000, 10_000, 1_000_000]


def add_user_and_clean(user_amount_list):
    for user_amount in user_amount_list:
        print(f"新增 {user_amount} 个外星人用户")
        start_time = time.time()

        for i in range(user_amount):
            user = {'Name': f'小灰人{i}号', 'Age': 1}
            add_user(user)

        print(f'当前 {count_all_user()} 个用户')
        print(f'消耗时间 {time.time()-start_time} 秒')

        remove_all_user()


add_user_and_clean(user_amount_list)