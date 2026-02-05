# Write your solution here

while True:
    print("1- add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))

    if function == 1:
        with open("diary.txt", "a") as write_file:
            diary_entry = input("Diary entry: ")
            diary_entry += "\n"
            write_file.write(diary_entry)
            print("Diary saved")
    elif function == 2:
        print("Entries:")
        with open("diary.txt") as read_file:
            for line in read_file:
                line = line.strip()
                print(line)
    elif function == 0:
        print("Bye now!")
        break



# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

#>>>> When the program is executed for the second time, this should happen:

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!
