# Write your solution here
def length_of_longest(ls: list):
    longest = ls[0]
    for l in ls:
        if len(l) > len(longest):
            longest = l
    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)