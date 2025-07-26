import time

# 데이터 준비
N = 10_000_000
target = N - 1

data_list = list(range(N))  # 리스트
data_dict = {i: f"value_{i}" for i in range(N)}  # 딕셔너리

# 리스트 조회 (존재 여부 확인)
start = time.perf_counter_ns()
found = target in data_list  # O(n)
elapsed_list = time.perf_counter_ns() - start
print(f"List 조회 결과: {found}, 시간: {elapsed_list // 1000}us")

# 딕셔너리 조회 (Key 존재 여부 확인)
start = time.perf_counter_ns()
found = target in data_dict  # O(1)
elapsed_dict = time.perf_counter_ns() - start
print(f"Dict 조회 결과: {found}, 시간: {elapsed_dict // 1000}us")
