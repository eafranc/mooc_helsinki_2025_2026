# Write your solution here
def even_numbers(int_list: list):
    even_list = []
    for i in int_list:
        if not i%2:
            even_list.append(i)
    return even_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)