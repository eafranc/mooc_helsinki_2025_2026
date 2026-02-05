# Write your solution here
limit = int(input("Limit:"))
count = 1
total = 1
calculation = "The consecutive sum: 1 "

while(total < limit):
    count +=1
    total += count
    calculation += f"+ {count} "
calculation += f"= {total}"    
print(calculation)