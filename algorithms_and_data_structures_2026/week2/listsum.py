# 1 - My first naïve (and too slow) approach
# def find_sums(numbers, size):
#     sublists = (numbers[i: i + size] for i in range(len(numbers) - size + 1))
#     return [sum(sublist) for sublist in sublists]

# 2 - A better solution - the idea is to calculate first sum and them use it to calculate all others
def find_sums(numbers: list, size: int):
    result = []
    current_sum = sum(numbers[:size])
    result.append(current_sum)
    for i in range(size, len(numbers)):
        current_sum += numbers[i] - numbers[i - size]
        result.append(current_sum)
    return result

if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]

    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000
