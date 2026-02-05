# Write your solution to exercise 2 here
def find_allowed(list_of_strings: list(str), minimum_allowed: int) -> list(str):
    allowed_chars = "aeiouy"
    allowed_strings = []

    for string in list_of_strings:
        allowed_occurrences = 0
        for ch in string:
            if ch in allowed_chars:
                allowed_occurrences += 1
        if allowed_occurrences < minimum_allowed:
            continue
        allowed_strings.append(string)

    return allowed_strings

# wordlist = ["apple", "banana", "cherry", "orange", "peach", "pineapple"]
# minimum = 3
# result = find_allowed(wordlist, minimum)
# print(result)
