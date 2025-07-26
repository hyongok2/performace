import time

start_ns = time.perf_counter_ns()
for i in range(1_000_000):
    x = i + 1229
end_ns = time.perf_counter_ns()

elapsed_ns = end_ns - start_ns
print(f"Elapsed time: {elapsed_ns} ns")
print(f"Elapsed time: {elapsed_ns / 1_000:.3f} μs")
print(f"Elapsed time: {elapsed_ns / 1_000_000:.3f} ms")

""" 파이썬의 시간 측정도 100ns 단위로 할 수 있다."""