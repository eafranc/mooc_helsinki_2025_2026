# Write your solution here
sentence = input("Please type in a sentence:")
i = 0
while(i < len(sentence)):
    if(i == 0 or sentence[i-1]== " "):
        print(sentence[i])
    i += 1