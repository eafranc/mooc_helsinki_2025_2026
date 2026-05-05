# Write your solution to exercise 1 here
all_strings = []
while True:
    string = input("Type in a string: ")
    if string == "":
        break
    all_strings.append(string)

length_of_all_strings = []
for string in all_strings:
    length_of_all_strings.append(len(string))
length_of_all_strings.sort()

all_strings_together = ""
for string in all_strings:
    all_strings_together += string

chars_count = {}
for ch in all_strings_together:
    if ch not in chars_count:
        chars_count[ch] = 1
    else:
        chars_count[ch] += 1

frequency_most_common_char = 0
most_common_char = ""
for key in chars_count:
    if chars_count[key] > frequency_most_common_char:
        frequency_most_common_char = chars_count[key]
        most_common_char = key

print("Total number of strings:", len(all_strings))
print("The length of the longest string:", length_of_all_strings[-1])
print("The most common character in strings:", most_common_char)
