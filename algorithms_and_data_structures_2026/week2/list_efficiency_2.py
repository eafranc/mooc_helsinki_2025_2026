import time

def add_to_end_of_list(lst: list, number: int):
    for i in range(1, number + 1):
        lst.append(i)

def delete_first_element(lst: list, number: int):
    for i in range(1, number + 1):
        lst.pop(0)

# Test setup
n = 100_000 # n = 10 ^ 5
lst = [] # empty list

# 1 - Additions
start_time = time.time()
add_to_end_of_list(lst, n)
end_time = time.time()

# 2 - Deletions
start_time2 = time.time()
delete_first_element(lst, n)
end_time2 = time.time()

# Report
print("=" * 50)
print(f"1 - Adding 1, 2, ..., n = {n} to a list:")
print(f"time for additions: {round(end_time - start_time, 10):.10f} s")
print()
print("=" * 50)
print(f"2 - Deleting the first element from the list n = {n} times:")
print(f"time for deletions: {round(end_time2 - start_time2, 10):.10f} s")
