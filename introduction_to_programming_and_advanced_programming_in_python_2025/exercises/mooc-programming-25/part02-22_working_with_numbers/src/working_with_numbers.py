# Write your solution here
count       = 0
sum_number  = 0
pos_numbers = 0
neg_numbers = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number:"))
    if (number==0):
        break
    count+=1
    sum_number+=number
    if(number>0):
        pos_numbers+=1
    if(number<0):
        neg_numbers+=1    
print("... the program asks for numbers")
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum_number}")
print(f"The mean of the numbers is {sum_number/count}")
print(f"Positive numbers {pos_numbers}")
print(f"Negative numbers {neg_numbers}")