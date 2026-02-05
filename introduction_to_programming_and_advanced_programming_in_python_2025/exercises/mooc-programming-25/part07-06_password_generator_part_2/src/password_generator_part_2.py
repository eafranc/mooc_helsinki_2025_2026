# 1 - FIRST SOLUTION - WILL BE SIMPLIFIED ON THE NEXT SOLUTION
# def generate_strong_password(pw_len: int, is_dig: bool, is_spc: bool):
#     from string import ascii_lowercase, digits
#     from random import choice
#     special_characters = "!?=+-()#"

#     possible_chars = ascii_lowercase
#     if is_dig:
#         possible_chars += digits
#     if is_spc:
#         possible_chars += special_characters

#     while True:
#         new_pw = ""
#         for i in range(pw_len):
#             new_pw += choice(possible_chars)

#         low_flag = False
#         dig_flag = not is_dig
#         spc_flag = not is_spc

#         for ch in new_pw:
#             if ch in ascii_lowercase:
#                 low_flag = True
#             if ch in digits:
#                 dig_flag = True
#             if ch in special_characters:
#                 spc_flag = True

#         if low_flag and dig_flag and spc_flag:
#             return new_pw

# 2 - A BETTER AND SIMPLIFIED SOLUTION: WE CHECK AND ASSURE EARLIER IF WE NEED A LOWERCASE LETTER, A DIGIT, AND A SPECIAL CHARACTER
def generate_strong_password(pw_len: int, is_dig: bool, is_spc: bool):
    from string import ascii_lowercase, digits
    from random import choice, shuffle
    special_characters = "!?=+-()#"

    password = []
    possible_characters = ascii_lowercase
    password.append(choice(ascii_lowercase)) # at least one lowercase letter
    if is_dig:
        password.append(choice(digits)) # if is_dig = True, it must have at least one digit
        possible_characters += digits
    if is_spc:
        password.append(choice(special_characters)) # if is_spc = True, it must have at least one special char
        possible_characters += special_characters

    while len(password) < pw_len:
        password.append(choice(possible_characters))

    shuffle(password) # shuffle because earlier the minimum required chars were added in order
    return "".join(password) # joins all the chars in the list to form a string

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
# 2?0n+u31
# u=m4nl94
# n#=i6r#(
# da9?zvm?
# 7h)!)g?!
# a=59x2n5
# (jr6n3b5
# 9n(4i+2!
# 32+qba#=
# n?b0a7ey
