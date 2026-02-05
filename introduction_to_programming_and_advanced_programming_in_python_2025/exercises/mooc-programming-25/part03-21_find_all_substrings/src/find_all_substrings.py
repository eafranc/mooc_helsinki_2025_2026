# Write your solution here
word = input("Please type in a word:")
char = input("Please type in a character:")

while True:
    if len(word) == 0:
        break
    slice_3 = word[(word.find(char)):(word.find(char)+3)]    
    if(len(slice_3) == 3):    
        print(slice_3)
        word = word[word.find(char)+1:]
    else:
        break