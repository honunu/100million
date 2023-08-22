import sqlite3

database_file = 'cache_test.db'


def get_user_by_id_db(user_id: int):
    user = {}
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Query and retrieve data from the table
    cursor.execute(f'SELECT * FROM user where id ={user_id}')
    result = cursor.fetchall()

    # Display the retrieved data
    for row in result:
        user = {'ID': row[0], 'Name': row[1], 'Age': row[2]}

    cursor.close()
    conn.close()

    return user


def update_user_by_id_db(user_id: int, user: dict):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    update_query = '''
        UPDATE user
        SET age = ?
        WHERE id = ?
    '''
    cursor.execute(update_query, (user['Age'], user_id))
    # Query and retrieve data from the table
    cursor.execute(f'SELECT * FROM user where id ={user_id}')

    conn.commit()
    cursor.close()
    conn.close()

    return user


def add_user(user: dict):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    data_to_insert = [
        (user['Name'], user['Age'])
    ]
    cursor.executemany('INSERT INTO user (name, age) VALUES (?, ?)', data_to_insert)

    conn.commit()
    cursor.close()
    conn.close()

    return user


def remove_all_user():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM user')

    # Commit the transaction to make the changes permanent
    conn.commit()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()


def count_all_user():
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM user')

    # Fetch the result of the query
    count = cursor.fetchone()[0]

    return count
