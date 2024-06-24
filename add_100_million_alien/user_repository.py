import sqlite3
from typing import List

from add_100_million_alien.configs import DB_FILE
from add_100_million_alien.models import Alien


class AlienRepo:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    def __init__(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alien
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           age INTEGER)''')
        self.conn.commit()



    def get_alien_by_id_db(self, alien_id: int):
        alien = {}

        # Query and retrieve data from the table
        self.cursor.execute(f'SELECT * FROM alien where id ={alien_id}')
        result = self.cursor.fetchall()

        # Display the retrieved data
        for row in result:
            alien = {'ID': row[0], 'Name': row[1], 'Age': row[2]}

        return alien

    def update_alien_by_id_db(self, alien_id: int, alien: dict):
        update_query = '''
            UPDATE alien
            SET age = ?
            WHERE id = ?
        '''
        self.cursor.execute(update_query, (alien['Age'], alien_id))
        # Query and retrieve data from the table
        self.cursor.execute(f'SELECT * FROM alien where id ={alien_id}')

        self.conn.commit()

        return alien

    def add_alien(self, alien: Alien):
        data_to_insert = [
            (alien.name, alien.age)
        ]
        self.cursor.executemany('INSERT INTO alien (name, age) VALUES (?, ?)', data_to_insert)

        self.conn.commit()

        return alien

    def add_alien_batch(self, aliens: List[Alien]):
        data_to_insert = [
            (alien.name, alien.age) for alien in aliens
        ]
        self.cursor.executemany('INSERT INTO alien (name, age) VALUES (?, ?)', data_to_insert)

        self.conn.commit()
        pass

    def remove_all_alien(self):
        self.cursor.execute('DELETE FROM alien')

        # Commit the transaction to make the changes permanent
        self.conn.commit()

        # Close the cursor and the database connection

    def count_all_alien(self):
        self.cursor.execute('SELECT COUNT(*) FROM alien')

        # Fetch the result of the query
        count = self.cursor.fetchone()[0]

        return count

    def close(self):
        self.cursor.close()
        self.conn.close()


class AlienRepoInMemory:
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    def __init__(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alien
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           age INTEGER)''')
        self.conn.commit()

    def add_alien_batch(self, aliens: List[Alien]):
        data_to_insert = [
            (alien.name, alien.age) for alien in aliens
        ]

        self.cursor.executemany('INSERT INTO alien (name, age) VALUES (?, ?)', data_to_insert)
        self.conn.commit()

    def remove_all_alien(self):
        self.cursor.execute('DELETE FROM alien')
        self.conn.commit()

    def count_all_alien(self):
        self.cursor.execute('SELECT COUNT(*) FROM alien')
        # Fetch the result of the query
        count = self.cursor.fetchone()[0]
        return count

    def close(self):
        self.cursor.close()
        self.conn.close()
