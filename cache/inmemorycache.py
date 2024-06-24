
class InMemoryCache():
    def __init__(self):
        self.cache = {}
        self.size=0

    def set(self, key, value):

        if self.cache.get(key) is None:
            self.size = self.size+1

        self.cache[key] = value
    def get(self, key):
        return self.cache.get(key)

    def delete(self, key):
        if self.cache[key] is not None:
            self.size=self.size-1
            self.cache.pop(key)
    def clear(self):
        self.cache.clear()
        self.size=0
