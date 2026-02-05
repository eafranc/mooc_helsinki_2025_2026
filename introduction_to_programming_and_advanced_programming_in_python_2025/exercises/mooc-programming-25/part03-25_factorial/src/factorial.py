# Write your solution here
while True:
    num = int(input("Please type in a number:"))
    if (num <= 0):
        break

    i = 1
    factorial = 1

    while (i <= num): 
        factorial *= i
        i += 1
    
    print(f"The factorial of the number {num} is {factorial}")    

print("Thanks and bye!")