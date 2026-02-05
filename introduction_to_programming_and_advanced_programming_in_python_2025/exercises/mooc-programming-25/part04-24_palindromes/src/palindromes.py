# Write your solution here
def palindromes(test_string):
    index = 0
    while (index < (len(test_string)/2) + (index%2)):
        if test_string[index] != test_string[len(test_string) - 1 - index]:
            return False
        index += 1
    return True

while True:
    test = input("Please type in a palindrome:")
    if palindromes(test):
        print(f"{test} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
