# bench_addition.py
import pyperf
import numpy as np

N = 100_000_000

def for_loop():
    total = 0
    for i in range(1, N + 1):
        total += i
    return total

def builtin_sum():
    return sum(range(1, N + 1))

def formula():
    return N * (N + 1) // 2

def numpy_sum():
    arr = np.arange(1, N + 1, dtype=np.int64)
    return np.sum(arr)

runner = pyperf.Runner()
runner.bench_func("for loop addition", for_loop)
runner.bench_func("builtin_sum addition", builtin_sum)
runner.bench_func("formula addition", formula)
runner.bench_func("numpy_sum addition", numpy_sum)