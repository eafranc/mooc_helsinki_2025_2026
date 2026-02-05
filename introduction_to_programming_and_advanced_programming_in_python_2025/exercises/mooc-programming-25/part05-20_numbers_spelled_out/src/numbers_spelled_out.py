# 1 - BEST SOLUTION:

def dict_of_numbers():
    dictionary_of_numbers = {}
    unities = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens   = [ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens    = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    for key in range(0, 10):
        dictionary_of_numbers[key] = unities[key]
    for key in range(10, 20):
        dictionary_of_numbers[key] = teens[key % 10]
    for i in range(2, 10): # PERFECT: Makes 8 x 10 iterations to set exactly 80 values in dictionary
        dictionary_of_numbers[10*i] = tens[i - 2]
        for j in range(1, 10):
            dictionary_of_numbers[10*i + j] = tens[i -2] + ("-" + unities[j])
    return dictionary_of_numbers

# 2 - MY FIRST SOLUTION (COULD BE IMPROVED)

# def dict_of_numbers():
#     dictionary_of_numbers = {}
#     unities = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#     teens   = [ "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
#     tens    = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#     for key in range(0, 10):
#         dictionary_of_numbers[key] = unities[key]
#     for key in range(10, 20):
#         dictionary_of_numbers[key] = teens[key % 10]
#     for key in range(20, 100): # INEFFICIENT: Makes 80 x 8 = 640 iterations to set 80 values in the dictionary
#         for i in range(2, 10):
#             if key in range(10*i, 10*(i + 1)):
#                 dictionary_of_numbers[key] = tens[i - 2]
#         if (key % 10) != 0:
#             dictionary_of_numbers[key] += ("-" + unities[key % 10])
#     return dictionary_of_numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    for number, value in numbers.items():
        print(f"{number: <2} : {value}")