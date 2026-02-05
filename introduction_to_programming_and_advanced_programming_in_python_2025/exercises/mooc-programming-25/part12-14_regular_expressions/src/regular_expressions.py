# Write your solution here
import re
def is_dotw(my_string: str):
    return True if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) else False

def all_vowels(my_string: str):
    return True if re.search("^[aeiou]+$", my_string) else False

def time_of_day(my_string: str):
    return True if re.search("^([0-1]\d|2[0-3]):[0-5]\d:[0-5]\d$", my_string) else False

if __name__ == "__main__":
###########################################################################
    print("=" * 100)
    print("PART 1\n")

    print(is_dotw("Mon")) # True
    print(is_dotw("Fri")) # True
    print(is_dotw("Tui")) # False
###########################################################################
    print("=" * 100)
    print("PART 2\n")

    print(all_vowels("eioueioieoieou")) # True
    print(all_vowels("autoooo")) # False

###########################################################################
    print("=" * 100)
    print("PART 3\n")

    print(time_of_day("12:43:01")) # True
    print(time_of_day("AB:01:CD")) # False
    print(time_of_day("17:59:59")) # True
    print(time_of_day("33:66:77")) # False

    print("=" * 100)
###########################################################################
