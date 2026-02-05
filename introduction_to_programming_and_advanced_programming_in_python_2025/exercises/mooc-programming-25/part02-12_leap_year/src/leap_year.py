# Write your solution here
year              = int(input("Please type in a year:"))
msg               = ""
leap_year_msg     = "That year is a leap year."
not_leap_year_msg = "That year is not a leap year." 

if (not year%4):
    if(not year%100):
        if(not year%400):
            msg+=leap_year_msg
        else:
            msg+=not_leap_year_msg
    else:
        msg+=leap_year_msg
else:
    msg+=not_leap_year_msg

print(msg)