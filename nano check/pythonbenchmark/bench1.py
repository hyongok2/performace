import timeit

setup_code = """
x = 0
"""

test_code = """
for i in range(1_000_000):
    x += i + 1234
"""

# 실행
execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
print(f"수행 시간: {execution_time:.6f} 초")