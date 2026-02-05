# Write your solution here:
# 1 - This solution works, but it has a flaw:
#     It always gives different chars in the words generated; it passes the tests, but it's technically incorrect

# def word_generator(characters: str, length: int, amount: int):
#     from random import sample
#     return ("".join(sample(characters, length)) for i in range(amount))

# 2 - A true solution would be using something that allows the same characters to reoccur in the same word generated
def word_generator(characters: str, length: int, amount: int):
    from random import choice
    return ( "".join([choice(characters) for i in range(length)]) for j in range(amount))

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
# dbf
# baf
# ead
# fga
# ccc
