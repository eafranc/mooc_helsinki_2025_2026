# Write your solution here
def no_shouting(list_of_strings: list[str]) -> list[str]:
    non_upper_list = []
    for string in list_of_strings:
        if not string.isupper():
            non_upper_list.append(string)
    return non_upper_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list) # ['def', 'lower', 'another lower', 'Capitalized']