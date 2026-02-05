# Write your solution here
def shortest(ls : list):
    shortest_str = ls[0]
    for l in ls:
        if len(l) < len(shortest_str):
            shortest_str = l # If there were more than 1 string with the least size, the code will bring the 1st shortest string in the list
    return shortest_str

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)

    my_list = ["first", "second", "fourth", "", "eleventh"]
    result = shortest(my_list)
    print(result)