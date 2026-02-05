# What determines the number of rounds is the number of inversions, i.e,
# the number of times a bigger number occurs before a smaller number on the list
def count_rounds(numbers):
    n = len(numbers)
    no_of_inversions = 0
    positions = [0] * (n + 1) # index 0 is not important

    for i in range(n):
        positions[numbers[i]] = i  # the value of position[k] gives the position of number k in numbers

    for j in range(1, n): # 2 for loops still counts as O(n)
        if positions[j] > positions[j + 1]:
            no_of_inversions += 1

    return no_of_inversions + 1

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10 ** 5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000
