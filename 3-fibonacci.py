from functools import lru_cache
import time


cache = {}


@lru_cache(maxsize=10000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


start = time.time()

for n in range(1, 10):
    # print(n, ":", fibonacci(n))
    fibonacci(n)

stop = time.time()
print("time:", stop - start)
