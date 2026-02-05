# 1 - ONE WAY
# def remove_smallest(numbers: list):
#     smallest = numbers[0]
#     for i in range(len(numbers)):
#         if numbers[i] < smallest:
#             smallest = numbers[i]
#     numbers.remove(smallest)

# 2 - ANOTHER (BETTER)
def remove_smallest(numbers: list):
    smallest = min(numbers)
    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers) # [2, 4, 6, 3, 5]

