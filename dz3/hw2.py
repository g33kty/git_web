#Синхронна версія:
def factorize_sync(*numbers):
    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    return [factors(n) for n in numbers]
#Паралельна версія з multiprocessing:
from multiprocessing import Pool, cpu_count


def factorize_parallel(*numbers):
    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]

    with Pool(cpu_count()) as pool:
        result = pool.map(factors, numbers)

    return result
#Перевірка продуктивності:
import time

numbers = [128, 255, 99999, 10651060]

# Синхронна версія
start = time.time()
factorize_sync(*numbers)
end = time.time()
print(f"Синхронна версія виконана за: {end - start} секунд")

# Паралельна версія
start = time.time()
factorize_parallel(*numbers)
end = time.time()
print(f"Паралельна версія виконана за: {end - start} секунд")

#Перевірка факторизації:

a, b, c, d = factorize_sync(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
