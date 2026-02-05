def check_year(year):
    # for a number in the form abcd (base 10),
    # ab = abcd // 10 ** 2 and cd = abcd % 10 ** 2

    return True if (year // 10 ** 2 + year % 10 ** 2) ** 2 == year else False

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False
