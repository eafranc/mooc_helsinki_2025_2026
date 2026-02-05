def check_number(number):
    if number[0] != "0" or len(number) != 9:
        return False

    verification_list = [3, 7, 1, 3, 7, 1, 3, 7, 0]
    verification_digit = int(number[8])
    verification_sum = sum([(int(number[i]) * verification_list[i]) for i in range(len(number))])

    return True if (verification_sum + verification_digit) % 10 == 0 else False

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
