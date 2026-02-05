# 1 - FIRST SOLUTION
# def get_wordlist():
#     wordlist = []
#     with open("words.txt") as file:
#         for line in file:
#             line = line.strip()
#             wordlist.append(line)
#         return wordlist

# def words(n: int, beginning: str):
#     from random import choice
#     wordlist = get_wordlist()
#     words_beginning = []
#     for word in wordlist:
#         if word.startswith(beginning):
#             words_beginning.append(word)
#     if len(words_beginning) < n:
#         raise ValueError
#     words_sample = []
#     while len(words_sample) < n:
#         random_word = choice(words_beginning)
#         if random_word not in words_sample:
#             words_sample.append(random_word)
#     return words_sample

# 2 - SIMPLER SOLUTION
def words(n: int, beginning: str):
    from random import sample
    words_beginning = []
    with open("words.txt") as file:
        for line in file:
            line = line.strip()
            if line.startswith(beginning):
                words_beginning.append(line)
        if len(words_beginning) < n:
            raise ValueError
        return sample(words_beginning, n)
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
# cat
# car
# carbon

