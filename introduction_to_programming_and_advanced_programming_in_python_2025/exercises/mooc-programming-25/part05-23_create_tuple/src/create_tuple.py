# Write your solution here
def create_tuple(x: int, y: int, z: int):
    numbers = [x, y, z]
    min_max_sum_tuple = (min(numbers), max(numbers), sum(numbers))
    return min_max_sum_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1)) # (-1, 5, 7)