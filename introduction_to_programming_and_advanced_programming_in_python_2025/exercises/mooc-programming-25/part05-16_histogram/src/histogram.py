# Write your solution here
def histogram(string: str):
    letters_frequency = {}
    for ch in string:
        letter = ch
        if letter not in letters_frequency:
            letters_frequency[letter] = ""
        letters_frequency[letter] += "*"
    for key, value in letters_frequency.items():
        print(f"{key} {value}")
if __name__ == "__main__":
    print("Histogram of the string abba:\n")
    histogram("abba")
    # a **
    # b **
    print("===============================")
    print("Histogram of the word statistically:\n")
    histogram("statistically")
    # s **
    # t ***
    # a **
    # i **
    # c *
    # l **
    # y *
