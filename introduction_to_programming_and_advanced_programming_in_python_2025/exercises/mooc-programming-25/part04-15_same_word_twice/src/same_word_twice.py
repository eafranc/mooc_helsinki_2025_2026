# Write your solution here
words   = []
counter = 0
while True:
    word = input("Word:")
    if word in words:
        print(f"You typed in {counter} different words")
        break
    else:
        counter += 1
        words.append(word)