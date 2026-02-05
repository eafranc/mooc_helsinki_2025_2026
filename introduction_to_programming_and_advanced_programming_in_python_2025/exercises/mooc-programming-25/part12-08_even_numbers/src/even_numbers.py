# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if beginning % 2:
        beginning += 1

    while beginning <= maximum:
        yield beginning
        beginning += 2


if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)
# 2
# 4
# 6
# 8
# 10
    print()

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)
# 12
# 14
# 16
# 18
# 20
