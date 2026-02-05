# Write your solution here
from random import *

def lottery_numbers(amount: int, lower: int, upper: int):
    lottery_list = []
    for i in range(amount):
        while len(lottery_list) < amount:
            lottery_number = randint(lower, upper)
            if lottery_number not in lottery_list:
                lottery_list.append(lottery_number)
    lottery_list.sort()
    return lottery_list

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)

# 4
# 7
# 11
# 16
# 22
# 29
# 38
