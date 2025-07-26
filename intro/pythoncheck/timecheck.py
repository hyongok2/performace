import time

repeat = 100
total = 0
for outloop in range(repeat):
    start = time.perf_counter()
    for i in range(1_000_000):
        x = i + 1229
    end = time.perf_counter()
    total += end - start

elapsed_sec = total / repeat
elapsed_us = elapsed_sec * 1_000_000

print(f"Elapsed time: {elapsed_sec * 1000:.3f} ms")
print(f"Elapsed time: {elapsed_us:.2f} us")

