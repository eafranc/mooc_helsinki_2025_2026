# Write your solution here
string1 = input("Please type in a string:")
msg = "The second and the second to last characters are "
if(string1[1] == string1[-2]):
    msg += f"{string1[1]}"
else:
    msg += "different"

print(msg)
