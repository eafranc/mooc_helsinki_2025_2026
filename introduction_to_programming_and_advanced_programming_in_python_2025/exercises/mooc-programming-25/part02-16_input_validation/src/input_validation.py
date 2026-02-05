from math import sqrt
# Write your solution here
while True:
    num = float(input("Please type in a number:"))
    if (num<0):
        print("Invalid number")
    elif (num==0):
        break
    else:
        print(sqrt(num))
print("Exiting...")