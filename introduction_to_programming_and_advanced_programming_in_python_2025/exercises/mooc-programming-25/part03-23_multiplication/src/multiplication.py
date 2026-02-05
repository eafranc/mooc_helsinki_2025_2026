# Write your solution here
num = int(input("Please type in a number:"))
i   = 1
while (i <= num):
    j = 1
    while (j <= num):
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1