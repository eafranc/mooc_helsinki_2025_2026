# Write your solution here
# 1 - ONE WAY (MY WAY):
# def invert(dictionary: dict):
#     new_dictionary = {}
#     for key, value in dictionary.items():
#         new_dictionary[value] = key
#     dictionary.clear()
#     for key, value in new_dictionary.items():
#         dictionary[key] = value

# 2 - OTHER WAY (SOLUTION KEY'S WAY):
def invert(dictionary: dict):
    new_dictionary = {}
    for key in dictionary: # Copies dictionary in new_dictionary
        new_dictionary[key] = dictionary[key]
    for key in new_dictionary: # Deletes every value in dictionary using iteration from the keys of the copy new_dictionary
        del dictionary[key]
    for key in new_dictionary:
        dictionary[new_dictionary[key]] = key

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s) # {"first": 1, "second": 2, "third": 3, "fourth": 4}