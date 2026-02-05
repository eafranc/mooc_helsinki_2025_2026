# Write your solution here
char1 = input("1st letter:")
char2 = input("2nd letter:")
char3 = input("3rd letter:")

n1 = n2 = n3 = char1

if(char2<n1):
    n1 = char2
if(char3<n1):
    n1 = char3

if(char2>n3):
    n3 = char2
if(char3>n3):
    n3 = char3

if(char1!=n1 and char1!=n3):
    n2 = char1
if(char2!=n1 and char2!=n3):
    n2 = char2
if(char3!=n1 and char3!=n3):
    n2 = char3

print(f"The letter in the middle is {n2}")



        

