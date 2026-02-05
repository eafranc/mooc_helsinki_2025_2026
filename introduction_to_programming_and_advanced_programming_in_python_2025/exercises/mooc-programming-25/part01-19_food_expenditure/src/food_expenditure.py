# Write your solution here
st_times_day  = int(input("How many times a week do you eat at the student cafeteria? "))
st_price_day  = float(input("The price of a typical student lunch?"))
grocery_week  = float(input("How much money do you spend on groceries in a week?\n"))
print("Average food expenditure:")
print(f"Daily: {(st_times_day*st_price_day + grocery_week)/7} euros")
print(f"Weekly: {st_times_day*st_price_day + grocery_week} euros")