# Write your solution here
def prime_numbers():
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if not num % i:
                is_prime = False
        if is_prime:
            yield num
        num += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
