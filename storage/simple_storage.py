import json
import os


class SimpleStorage():
    """
        Simple storage is a binary key value store that stores anything to file
        """

    def __init__(self):
        self.db_filename = 'simple_storage.db'
        self.index_filename = 'simple_storage.index'
        self.create_file_if_not_exist(self.db_filename)
        self.create_file_if_not_exist(self.index_filename)

    def create_file_if_not_exist(self, filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write("")

    def get(self, filename: str) -> bytes:
        position = self.get_index(filename)

    def set(key: str, value: bytes):
        pass

    def read_db_file(self):
        with open(self.db_filename, 'rw') as f:
            pass

    def get_index(self, filename):
        with open(self.index_filename, 'r') as f:
            content = f.read()
            index_json = json.loads(content)
            position = index_json[filename]
            return position

    def get_bytes(self, position, length):
        pass

    def add_index(self, filename, position):
        if self.is_file_empty(self.index_filename):
            index_json = {}
        else:

            with open(self.index_filename, 'r') as f:

                index_json = json.load(f)

        index_json[filename] = position

        with open(self.index_filename, 'w') as f:
            json.dump(index_json, f)

    def write_file(self, filename, content):
        position = os.path.getsize(self.db_filename)

        self.add_index(filename, position)

        with open(self.db_filename, 'wb') as f:
            f.seek(position)
            f.write(content)

    def is_file_empty(self, file_path):
        try:
            return os.path.getsize(file_path) == 0
        except FileNotFoundError:
            return False  # File doesn't exist


s = SimpleStorage()
# s.write_file('cat', b'01234')
# s.write_file('cat2', b'222222')
# s.write_file('cat3', b'444444523')
