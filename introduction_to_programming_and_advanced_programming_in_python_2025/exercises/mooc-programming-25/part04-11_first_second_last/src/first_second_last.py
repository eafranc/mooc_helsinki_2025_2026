# Write your solution here
def first_word(sentence):
    first_word = sentence[:sentence.find(" ")]
    return first_word

def second_word(sentence):
    sentence_minus_1st_word = sentence[sentence.find(" ") + 1:]
    if (sentence_minus_1st_word.find(" ")!= -1): # if there's two or more words left in the "adjusted" sentence 
        second_word = sentence_minus_1st_word[:sentence_minus_1st_word.find(" ")]
    else: # if there's only one word left in the "adjusted" sentence
        second_word = sentence_minus_1st_word
    return second_word

def last_word(sentence):
    while (sentence.find(" ") != -1): # sentence will lose first word every time until only the last word remains
        sentence = sentence[sentence.find(" ") + 1:]
    last_word = sentence
    return last_word
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))