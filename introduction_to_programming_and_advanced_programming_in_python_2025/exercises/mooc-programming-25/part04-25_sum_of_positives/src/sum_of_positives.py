# Write your solution here
def sum_of_positives(int_list: list):
    sum_pos = 0
    for i in int_list:
        if i > 0:
            sum_pos += i
    return sum_pos

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
