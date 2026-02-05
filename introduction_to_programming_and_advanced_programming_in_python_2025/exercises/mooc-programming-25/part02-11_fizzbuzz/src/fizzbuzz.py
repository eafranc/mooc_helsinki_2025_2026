# Write your solution here
num = int(input("Number:"))
FizzBuzz = ""

if(not num%3):
    FizzBuzz += "Fizz"
if(not num%5):
    FizzBuzz += "Buzz"
print(FizzBuzz)