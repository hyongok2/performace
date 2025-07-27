import time

cache = {}

def expensive_function(x):
    if x in cache:
        print(f"✅ 캐시 hit: {x}")
        return cache[x]

    print(f"❌ 캐시 miss: {x}")
    time.sleep(2) # 시간 소요 되는 작업 -  DB 쿼리 API 요청 머신러닝 추론
    result = x * 2  # 시간이 오래 걸리는 연산이라고 가정
    cache[x] = result # 캐시에 결과 저장
    return result


print(time.ctime())
print(expensive_function(5))
print(time.ctime())
print(expensive_function(5))
print(time.ctime())

## 간단한 캐시는 다양한 기능이 없지만, 상황에 따라서 유용할 수 있습니다. ##
## 보통의 경우 이 정도로도 충분할 수 있습니다. ##
