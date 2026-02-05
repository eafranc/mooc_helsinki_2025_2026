# Write your solution here
from string import ascii_lowercase
from random import randint

def generate_password(pw_length: int):
    generated_password = ""
    for i in range(pw_length):
        generated_password += ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]
    return generated_password

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))
# lttehepy
# olsxttjl
# cbjncrzo
# dwxqjdgu
# gpfdcecs
# jabyvgar
# xnbbonbl
# ktmsjyww
# ejhprmel
# rjkoacib
