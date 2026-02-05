# Write your solution here
name1 = input("Person 1:")
age1  = int(input("Age:"))
name2 = input("Person 2:")
age2  = int(input("Age:"))

if(age1>age2):
    print(f"The elder is {name1}")
elif(age2>age1):
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")