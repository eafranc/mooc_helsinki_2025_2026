# WRITE YOUR SOLUTION HERE:
def get_words(filename: str):
    with open(filename) as file:
        all_words = []
        for line in file:
            words = line.replace(",", "").replace(".", "").strip().split()
            all_words += words
        return all_words

def most_common_words(filename: str, lower_limit: int):
    words = get_words(filename)
    return {word: words.count(word) for word in words if words.count(word)>= lower_limit}

if __name__ == "__main__":
    words = get_words("comprehensions.txt")
    print(words)
    words_occur_3_plus = most_common_words("comprehensions.txt", 3)
    print()
    print(words_occur_3_plus)
