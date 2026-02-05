import random
import time

# implementation 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)
####################################################################
n = 10_000_000 # n = 10 ^ 7
random.seed(1999)
numbers = [random.randint(1, 10**9) for _ in range(n)]
####################################################################
# IMPLEMENTATION 1
start_time = time.time()
result = count_even1(numbers)
end_time = time.time()

print("=" * 50)
print("implementation 1")
print("=" * 50)
print("result:", result)
print("time:", round(end_time - start_time, 2), "s")
print("=" * 50)
print()
print()
####################################################################
# IMPLEMENTATION 2
start_time = time.time()
result = count_even2(numbers)
end_time = time.time()

print("=" * 50)
print("implementation 2")
print("=" * 50)
print("result:", result)
print("time:", round(end_time - start_time, 2), "s")
print("=" * 50)
print()
print()
####################################################################
# OUTPUT:

# ==================================================
# implementation 1
# ==================================================
# result: 5000439
# time: 0.35 s
# ==================================================


# ==================================================
# implementation 2
# ==================================================
# result: 5000439
# time: 0.44 s
# ==================================================
