# Write your solution here
num = int(input("Please type in a number:"))

i = 1
while (i <= num/2 + num%2):
    print(i)
    if (i != (num - i + 1)):
        print(num - i + 1)
    i += 1