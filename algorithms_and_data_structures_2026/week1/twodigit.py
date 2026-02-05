# FIRST ATTEMPTS:

# def count_numbers(a, b): # not an ideal code - too slow
#     counter = 0
#     for i in range(a, b + 1):
#         digits = str(i)
#         count = True
#         for digit in digits:
#             if digit not in "25":
#                 count = False
#                 break
#         if count:
#             counter += 1
#     return counter

# def count_numbers(a, b): # also too slow
#     import re
#     counter = 0
#     for i in range(a, b + 1):
#         digits = str(i)
#         if re.search("^[25]+$", digits):
#             counter += 1
#     return counter
#############################################################
# A faster solution

# def convert_to_binary(num: int):
#     binary = []
#     if num == 0:
#         binary.append("0")
#     while num:
#         binary.append(str(num % 2))
#         num //= 2
#     return "".join(binary[::-1]) # invert the list of all the remainders of the successive division of num by 2

# def fill_bits(num: int, no_of_bits: int):
#     binary = convert_to_binary(num)
#     if len(binary) > no_of_bits:
#         return None
#     while len(binary) != no_of_bits:
#         binary = "0" + binary
#     return binary

# def transform_binary_in_special(binary: str): # I will from now on call special numbers those only formed by digits 2 and 5
#     special = ""
#     for bit in binary:
#         if bit == "0":
#             special += "2"
#         if bit == "1":
#             special += "5"
#     return int(special)

# def list_of_specials(sup_limit: int):
#     specials = []
#     num = 0
#     no_of_bits = 1
#     special = 0
#     while special <= sup_limit:
#         if num == 2 ** no_of_bits:
#             num = 0
#             no_of_bits += 1
#         special = transform_binary_in_special(fill_bits(num, no_of_bits))
#         num += 1
#         if special <= sup_limit:
#             specials.append(special)
#     return specials

# def count_numbers(a: int, b: int):
#     return len(list_of_specials(b)) - len(list_of_specials(a -1))

# Another solution using recursion
def generate_specials(current, limit, result):
    if current > limit:
        return
    result.append(current)
    generate_specials(10 * current + 2, limit, result)
    generate_specials(10 * current + 5, limit, result)
    return result

def list_of_specials(limit):
    result = []
    generate_specials(2, limit, result)
    generate_specials(5, limit, result)
    result.sort()
    return result

def count_numbers(a, b):
    specials = list_of_specials(b)
    return sum(1 for x in specials if x >= a)


if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512
