from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        value = self.cache.get(key, None)
        if value is None:
            return -1
        self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None) is not None:
            self.cache.pop(key)
            self.cache[key] = value
        elif self.capacity != len(self.cache):
            self.cache[key] = value
        else:
            self.cache.popitem(0)
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)