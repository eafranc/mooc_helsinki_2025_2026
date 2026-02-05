# 1 - ONE WAY OF DOING
# def double_items(numbers: list):
#     new_numbers = []
#     for number in numbers:
#         new_numbers.append(2*number) 
#     return new_numbers # returns a new list without editing the original list

# 2 - OTHER WAY:
def double_items(numbers: list):
    new_numbers = numbers[:] # slicing (even if we take all list by slicing) results in a copy of the original list
    for i in range(len(new_numbers)):
        new_numbers[i] *= 2  # NOTICE: this line is actually updating new_numbers list to point to the new (doubled) value
    return new_numbers

# REMEMBER: That while lists are mutable in Python, ints, floats and bools are immutable,
# so you don't actually change a variable value, you create a new object with a new value and then you use the variable
# to point to this new object.

# e.g., in the line: new_numbers[i] *= 2  --> What really is happening is:
#   temp = new_numbers[i]        # Gets the reference
#   temp = temp * 2              # Creates a new object
#   new_numbers[i] = temp        # <-- UPDATES THE LIST

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)        # original: [2, 4, 5, 3, 11, -4]
    print("doubled:", numbers_doubled) # doubled: [4, 8, 10, 6, 22, -8]

# 3 -THE WRONG WAY - LET'S SEE HOW NOT TO CHANGE THE LIST COPY:
# def double_items(numbers: list):
#     new_numbers = numbers[:] # slicing (even if we take all list by slicing) results in a copy of the original list
#     for number in new_numbers:
#         number *= 2 # THE ERROR: Python creates a new object here, but only 'number' (the loop variable) 
                      #  points to it. The list 'new_numbers' still points to the original objects.
#     return new_numbers

# if __name__ == "__main__":
#     numbers = [2, 4, 5, 3, 11, -4]
#     numbers_doubled = double_items(numbers)
#     print("original:", numbers)        # original: [2, 4, 5, 3, 11, -4]
#     print("doubled:", numbers_doubled) # ERROR:  doubled: [2, 4, 5, 3, 11, -4] ---> IT DOESN'T CHANGE