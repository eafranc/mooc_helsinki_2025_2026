# Write your solution here
def most_common_character(chs: str):
    most_common_char = chs[0]
    for ch in chs:
        if chs.count(ch) > chs.count(most_common_char):
            most_common_char = ch
    return most_common_char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string)) # b

    second_string = "exemplaryelementary"
    print(most_common_character(second_string)) # e
