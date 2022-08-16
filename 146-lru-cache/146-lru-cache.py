class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        value = self.cache.get(key, None)
        if value is None:
            return -1
        del self.cache[key]
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None) is not None:
            del self.cache[key]
            self.cache[key] = value
        elif self.capacity != len(self.cache):
            self.cache[key] = value
        else:
            first = list(self.cache.keys())[0]
            del self.cache[first]
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)