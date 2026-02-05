# Write your solution here
items = []
number_items = int(input("How many items:"))

counter = 1
while (counter <= number_items):
    item = int(input(f"Item {counter}: "))
    items.append(item)
    counter +=1

print(items)
