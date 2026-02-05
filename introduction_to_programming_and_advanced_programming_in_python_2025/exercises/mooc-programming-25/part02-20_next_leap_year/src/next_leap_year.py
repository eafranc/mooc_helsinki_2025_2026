# Write your solution here
#VERBOSE SOLUTION (BUT IT WORKS)
#year = int(input("Year:"))
#nextYearEval = False
#
#msg = f"The next leap year after {year} is "
#
#while True:
#    if(year%4==0):
#        if(year%100==0):
#            if(year%400==0):
#                if (nextYearEval == False):
#                    year+=4 # year is Leap and we must evaluate if year+4 is Leap too
#                    nextYearEval = True
#                else:
#                    break
#            else:
#                nextYearEval = True
#                year+=1 # year is not Leap
#        else:
#            if (nextYearEval == False):
#                year+=4 # year is Leap and we must evaluate if year+4 is Leap too
#                nextYearEval = True
#            else:
#                break
#    else:
#        nextYearEval = True
#        year+=1 # year is not Leap
#
#msg += f"{year}"
#
#print(msg)
####################################################################
# A BETTER SOLUTION
start_year = int(input("Year:"))
year = start_year + 1
while True:
    if (year%4==0):
        if(year%100==0):
            if(year%400==0):
                break # Leap Year               
            else:
                year+=1 # Not Leap Year
        else:
            break # Leap Year
    else:
        year+=1 # Not Leap Year
print(f"The next leap year after {start_year} is {year}")


