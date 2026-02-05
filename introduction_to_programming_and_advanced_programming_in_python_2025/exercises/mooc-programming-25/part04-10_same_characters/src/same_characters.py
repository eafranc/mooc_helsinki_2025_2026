# Write your solution here
def same_chars(word, ind1, ind2):
    if (ind1 >= len(word) or ind2 >= len(word) or word[ind1] != word[ind2]):
        return False
    elif (word[ind1] == word[ind2]):
        return True
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))