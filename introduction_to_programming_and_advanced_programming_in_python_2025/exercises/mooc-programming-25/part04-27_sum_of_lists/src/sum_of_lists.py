# Write your solution here
# 1 - LESS SIMPLE SOLUTION
# def list_sum(list1: list, list2: list):
#     sum_list = []
#     index = 0
#     while index < len(list1):
#         sum_list.append(list1[index] + list2[index])
#         index += 1
#     return sum_list
#
# 2 - SIMPLER SOLUTION
def list_sum (ls1: list, ls2: list):
    sum_list = []
    for i in range(len(ls1)):
        sum_list.append(ls1[i] + ls2[i])
    return sum_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]