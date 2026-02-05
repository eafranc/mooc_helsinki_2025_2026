# Write your solution here
# 1 - A GOOD NO-NONSENSE SOLUTION
# def distinct_numbers(ls: list):   
#     distincts = []

#     i = 0
#     while(i < len(ls)):
#         j = 0
#         exists = False
#         while (j < len(distincts)):
#             if ls[i] == distincts[j]:
#                 exists = True
#                 break
#             j += 1
        
#         if not exists:
#             distincts.append(ls[i])
#         i +=1
#     distincts.sort()
#     return distincts

# 2 - THE BEST AND EASIEST SOLUTION:
def distinct_numbers(ls: list):
    distincts = []
    for l in ls:
        if l not in distincts:
            distincts.append(l)
    distincts.sort()
    return distincts

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]