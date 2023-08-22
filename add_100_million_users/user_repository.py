import sqlite3


class UserRepository:
    database_file = 'cache_test.db'

    def get_user_by_id_db(self, user_id: int):
        user = {}
        conn = sqlite3.connect(self.database_file)
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

    def update_user_by_id_db(self, user_id: int, user: dict):
        conn = sqlite3.connect(self.database_file)
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

    def add_user(self, user: dict):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        data_to_insert = [
            (user['Name'], user['Age'])
        ]
        cursor.executemany('INSERT INTO user (name, age) VALUES (?, ?)', data_to_insert)

        conn.commit()
        cursor.close()
        conn.close()

        return user

    def remove_all_user(self):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        cursor.execute('DELETE FROM user')

        # Commit the transaction to make the changes permanent
        conn.commit()

        # Close the cursor and the database connection
        cursor.close()
        conn.close()

    def count_all_user(self):
        conn = sqlite3.connect(self.database_file)
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM user')

        # Fetch the result of the query
        count = cursor.fetchone()[0]

        return count

    def close(self):
        pass


class UserRepositoryOneConnection:
    database_file = 'cache_test.db'
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    def get_user_by_id_db(self, user_id: int):
        user = {}

        # Query and retrieve data from the table
        self.cursor.execute(f'SELECT * FROM user where id ={user_id}')
        result = self.cursor.fetchall()

        # Display the retrieved data
        for row in result:
            user = {'ID': row[0], 'Name': row[1], 'Age': row[2]}

        return user

    def update_user_by_id_db(self, user_id: int, user: dict):
        update_query = '''
            UPDATE user
            SET age = ?
            WHERE id = ?
        '''
        self.cursor.execute(update_query, (user['Age'], user_id))
        # Query and retrieve data from the table
        self.cursor.execute(f'SELECT * FROM user where id ={user_id}')

        self.conn.commit()

        return user

    def add_user(self, user: dict):
        data_to_insert = [
            (user['Name'], user['Age'])
        ]
        self.cursor.executemany('INSERT INTO user (name, age) VALUES (?, ?)', data_to_insert)

        self.conn.commit()

        return user

    def remove_all_user(self):
        self.cursor.execute('DELETE FROM user')

        # Commit the transaction to make the changes permanent
        self.conn.commit()

        # Close the cursor and the database connection

    def count_all_user(self):
        self.cursor.execute('SELECT COUNT(*) FROM user')

        # Fetch the result of the query
        count = self.cursor.fetchone()[0]

        return count

    def close(self):
        self.cursor.close()
        self.conn.close()
