# 1 - NORMAL SOLUTION, NO TRICKS
# # Write your solution here
# def all_the_longest(ls: list):
#     longest = []
#     longest_string = ls[0]
#     for l in ls:
#         if len(l) > len(longest_string):
#             longest_string = l
#     for l in ls:
#         if len(l) == len(longest_string):
#             longest.append(l)
#     return longest

# 2 - PROBABLY THE BEST SOLUTION
def all_the_longest(names: list):
    longest_names = []

    for name in names:
        if longest_names == [] or len(name) > len(longest_names[0]):
            longest_names = [name] # This line makes the list of longest strings be updated with only 1 new value 
                                   # and remove the previous strings thought to be the longest on earlier iterations
        elif len(name) == len(longest_names[0]):
            longest_names.append(name)
    return longest_names

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result) # ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']

# INTERESTING PIECE OF THEORY
#
# 💡 The Pattern "Reset-or-Append"
# This pattern is common in Python:
#
# best = []
#
# for item in itens:
#     if best_than_others(item):
#         best = [item]            # 🔥 RESET
#     elif as_good_as_the_best(item):
#         best.append(item)        # ADD to the best ones