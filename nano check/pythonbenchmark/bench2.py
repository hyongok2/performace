# bench_addition.py
import pyperf

def run():
    x = 0
    for i in range(1_000_000):
        x += i + 1234
    return x

runner = pyperf.Runner()
runner.bench_func("for loop addition", run)