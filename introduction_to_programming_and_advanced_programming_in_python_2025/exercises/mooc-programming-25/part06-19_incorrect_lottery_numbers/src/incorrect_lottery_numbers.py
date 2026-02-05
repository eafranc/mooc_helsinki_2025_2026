# Write your solution here
def filter_incorrect():
    filtered_lines = {}
    with open("lottery_numbers.csv") as read_file:
        for line in read_file:
            line = line.strip()
            parts = line.split(";")
            week_parts  = parts[0].split(" ")
            # week = week_parts[0]
            week_number = week_parts[1]
            lottery_numbers = parts[1].split(",")

            if len(lottery_numbers) < 7: # Too few number
                continue
            try:
                int(week_number) # The week number is incorrect
            except:
                continue

            error = False
            for number in lottery_numbers:
                try:
                    if int(number) < 1 or int(number) > 39:  # One or more numbers are not correct, The numbers are too small or large
                        error = True
                        break
                except:
                    error = True
                    break
                if lottery_numbers.count(number) != 1: # The same number appears twice
                    error = True
                    break
            if not error:
                filtered_lines[week_number] = lottery_numbers
                # print(f"{week_number} {filtered_lines[week_number]}")
                write_correct(filtered_lines)

def write_correct(filtered: dict):
    filtered_lines = filtered
    with open("correct_numbers.csv", "w") as write_file:
        for week_number in filtered_lines:
            write_file.write(f"week {week_number};")
            number_counter = 0
            for number in filtered_lines[week_number]:
                write_file.write(f"{number}")
                number_counter += 1
                if number_counter < 7:
                    write_file.write(",")
            write_file.write("\n")
if __name__ == "__main__":
    def main():
        filter_incorrect()

    main()

# The week number is incorrect:
# week zzc;1,5,13,22,24,25,26
# One or more numbers are not correct:
# week 22;1,**,5,6,13,2b,34
# Too few numbers:
# week 13;4,6,17,19,24,33
# The numbers are too small or large:
# week 39;5,9,15,35,39,41,105
# The same number appears twice:
# week 41;5,12,3,35,12,14,36
