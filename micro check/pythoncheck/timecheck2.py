import timeit

code = """
for i in range(1_000_000):
    x = i + 1229
"""

elapsed = timeit.timeit(stmt=code, number=1)
print(f"timeit: {elapsed * 1000:.3f} ms")