# Write your solution here
hourly_wage  = float(input("Hourly wage:"))
hours_worked = float(input("Hours worked:"))
day_week     = input("Day of the week:")

if(day_week != "Sunday"):
    print(f"Daily wages: {hourly_wage * hours_worked} euros")
if(day_week == "Sunday"):
    print(f"Daily wages: {2*hourly_wage * hours_worked} euros")