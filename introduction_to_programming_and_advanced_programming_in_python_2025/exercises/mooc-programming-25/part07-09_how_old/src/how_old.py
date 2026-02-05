# Write your solution here
from datetime import datetime, timedelta
if True:
    birth_day   = int(input("Day: "))
    birth_month = int(input("Month: "))
    birth_year  = int(input("Year: "))
else:
    birth_day   = 24
    birth_month = 7
    birth_year  = 1991

birthday = datetime(birth_year, birth_month, birth_day)

new_millennium_eve = datetime(1999, 12, 31)

difference = new_millennium_eve - birthday

if difference.days >= 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
    # print(f"Which is roughly {difference.days // 365} years old")
else:
    print("You weren't born yet on the eve of the new millennium.")

# Day: 10
# Month: 9
# Year: 1979
# You were 7417 days old on the eve of the new millennium.

# Day: 28
# Month: 3
# Year: 2005
# You weren't born yet on the eve of the new millennium.
