import time
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # 가장 최근 사용으로 이동
            print(f"✅ 캐시 hit: {key}")
            return self.cache[key]
        print(f"❌ 캐시 miss: {key}")
        return None

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            oldest = next(iter(self.cache))
            print(f"🗑️ 캐시 제거 (LRU): {oldest}")
            self.cache.popitem(last=False)  # FIFO = LRU 제거
        self.cache[key] = value

# 테스트
cache = LRUCache(capacity=2)

def expensive_function(x):
    result = cache.get(x)
    if result is not None:
        return result
    time.sleep(2)
    result = x * 2
    cache.set(x, result)
    return result

print(expensive_function(1))  # miss
print(expensive_function(2))  # miss
print(expensive_function(1))  # hit
print(expensive_function(3))  # 2 제거됨
print(expensive_function(2))  # 다시 miss


## LRU 캐시는 자주 사용되는 데이터를 우선적으로 유지하고, 오래된 데이터를 제거하는 데 유용합니다. ##
## 실전에서는 LRU 캐시를 구현한 라이브러리를 사용하는 것이 좋습니다. ##
