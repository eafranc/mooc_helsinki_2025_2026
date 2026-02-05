# Write your solution here
def everything_reversed(words: list):
    all_reversed_list = []
    for word in words[::-1]:
        all_reversed_list.append(word[::-1])
    return all_reversed_list

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list) # ['erom eno', 'elpmaxe', 'ereht', 'iH']