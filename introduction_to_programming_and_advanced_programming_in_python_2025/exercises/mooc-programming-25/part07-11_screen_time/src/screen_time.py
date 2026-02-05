# Write your solution here
from datetime import datetime, timedelta

def write_screen_times(filename: str, screen_times: dict):
    screen_time_dates = []
    number_of_days = 0
    total_minutes = 0
    for key in screen_times:
        total_minutes += (screen_times[key]["TV"] + screen_times[key]["computer"] + screen_times[key]["mobile"])
        screen_time_dates.append(key)
        number_of_days += 1
    avg_minutes = total_minutes / number_of_days
    screen_time_dates.sort()
    first_date = screen_time_dates[0]
    last_date  = screen_time_dates[-1]

    with open(filename, "w") as file:
        file.write(f"Time period: {first_date.strftime("%d.%m.%Y")}-{last_date.strftime("%d.%m.%Y")}\n")
        file.write(f"Total minutes: {total_minutes}\n")
        file.write(f"Average minutes: {avg_minutes:.1f}\n")
        for day in screen_times:
            file.write(f"{day.strftime("%d.%m.%Y")}: {screen_times[day]["TV"]}/{screen_times[day]["computer"]}/{screen_times[day]["mobile"]}\n")
    print(f"Data stored in file {filename}")

def get_screen_times():
    if True:
        filename       = input("Filename: ")
        in_start_date  = input("Starting date: ")
        start_date     = datetime.strptime(in_start_date, "%d.%m.%Y")
        number_of_days = int(input("How many days: "))
    else:
        filename          = "late_june.txt"
        in_start_date     = "29.6.2020"
        start_date        = datetime.strptime(in_start_date, "%d.%m.%Y")
        number_of_days    = 4

    print("Please type in screen time in minutes on each day (TV computer mobile)")
    screen_times = {}
    for i in range(number_of_days):
        day = start_date + timedelta(days = i)
        screen_times[day] = {"TV": 0, "computer": 0, "mobile": 0}
        minutes_per_media = input(f"Screen time {day.strftime("%d.%m.%Y")}: ")
        [tv, computer, mobile] = minutes_per_media.split(" ")
        [screen_times[day]["TV"], screen_times[day]["computer"], screen_times[day]["mobile"]] = [int(tv), int(computer), int(mobile)]
    write_screen_times(filename, screen_times)

def main():
    get_screen_times()

main()
# screen_times[datetime(24, 6, 2020)] = {"TV": 0, "computer": 0, "mobile": 0}

# Filename: late_june.txt
# Starting date: 24.6.2020
# How many days: 5
# Please type in screen time in minutes on each day (TV computer mobile):
# Screen time 24.06.2020: 60 120 0
# Screen time 25.06.2020: 0 0 0
# Screen time 26.06.2020: 180 0 0
# Screen time 27.06.2020: 25 240 15
# Screen time 28.06.2020: 45 90 5
# Data stored in file late_june.txt

# With the above input, the program should store the data in a file named late_june.txt.
# The contents should look like this:

# Time period: 24.06.2020-28.06.2020
# Total minutes: 780
# Average minutes: 156.0
# 24.06.2020: 60/120/0
# 25.06.2020: 0/0/0
# 26.06.2020: 180/0/0
# 27.06.2020: 25/240/15
# 28.06.2020: 45/90/5

# Please type in screen time in minutes on each day (TV computer mobile)
# Screen time 29.06.2020: 30 100 0
# Screen time 30.06.2020: 55 40 0
# Screen time 01.07.2020: 0 240 25
# Screen time 02.07.2020: 180 240 100
# Data stored in file late_june.txt

# Time period: 29.06.2020-02.07.2020
# Total minutes: 1010
# Average minutes: 252.5
# 29.06.2020: 30/100/0
# 30.06.2020: 55/40/0
# 01.07.2020: 0/240/25
# 02.07.2020: 180/240/100
