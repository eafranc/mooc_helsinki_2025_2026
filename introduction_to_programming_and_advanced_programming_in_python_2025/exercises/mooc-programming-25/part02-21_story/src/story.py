# Write your solution here
words = ""
previous_word =""
while True:
    word = input("Please type in a word:")
    if(word == "end" or word == previous_word):
        break
    words = words +" "+ word
    previous_word = word
print(words)
