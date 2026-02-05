# Write your solution here
age = int(input("What is your age?"))

if (age<0 or age>120):
    print("That must be a mistake")
elif (0<=age<5):
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {age} years old")
