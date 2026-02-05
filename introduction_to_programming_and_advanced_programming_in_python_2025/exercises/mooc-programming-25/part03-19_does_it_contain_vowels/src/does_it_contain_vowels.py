# Write your solution here
string1 = input("Please type in a string:")
vowels ="aeo"
index = 0

while(index < len(vowels)):
    if vowels[index] in string1:
        print(f"{vowels[index]} found")
    else:
        print(f"{vowels[index]} not found")
    index += 1