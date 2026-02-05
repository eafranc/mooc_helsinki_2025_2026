# Write your solution here
word = input("Please type in a word:")
char = input("Please type in a character:")

slice_3 = word[(word.find(char)):(word.find(char)+3)]

if (len(slice_3) == 3):
    print(slice_3)