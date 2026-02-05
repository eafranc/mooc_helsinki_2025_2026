# Write your solution here
str1 = input("Please type in string 1:")
str2 = input("Please type in string 2:")

if(len(str1)>len(str2)):
    msg = f"{str1} is longer"
elif(len(str2)>len(str1)):
    msg = f"{str2} is longer"
else:
    msg = "The strings are equally long"
print(msg)