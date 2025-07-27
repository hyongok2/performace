import time

cache = {}  # key: (value, timestamp)
TTL = 5  # 초 단위

def expensive_function(x):
    now = time.time()
    if x in cache:
        value, saved_time = cache[x]
        if now - saved_time < TTL:
            print(f"✅ 캐시 hit (TTL 유효): {x}")
            return value
        else:
            print(f"⚠️ 캐시 expired: {x}")
    
    print(f"❌ 캐시 miss: {x}")
    result = x * 2
    time.sleep(2)
    cache[x] = (result, now)
    return result

print(expensive_function(10))
print(expensive_function(10))  # hit
time.sleep(6)
print(expensive_function(10))  # expired → miss

# 실전에서는 TTL 같은 기능이 필요한 경우 잘 설계된 캐시 라이브러리를 사용하는 것이 좋습니다. ##
