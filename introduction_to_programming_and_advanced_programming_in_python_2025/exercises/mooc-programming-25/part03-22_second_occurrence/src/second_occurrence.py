# Write your solution here
string1    = input("Please type in a string:")
substring  = input("Please type in a substring:")

# Index of the final char of the 1st occurrence of the substring:
final_index_1   = string1.find(substring) + len(substring) - 1
# Substring which begins on the next char after the last char of the 1st substring
string2         = string1[final_index_1 + 1:]
# Index of the 2nd occurence of the substring
initial_index_2 = string2.find(substring) + final_index_1 + 1

if substring in string1 and substring in string2:
    msg = f"The second occurrence of the substring is at index {initial_index_2}."
else:
    msg = "The substring does not occur twice in the string."
print(msg)