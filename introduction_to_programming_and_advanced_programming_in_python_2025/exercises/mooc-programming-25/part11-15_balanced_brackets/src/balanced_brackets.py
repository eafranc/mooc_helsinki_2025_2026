# 1 - MY SOLUTION - CLUMSY, BUT WORKS
# def balanced_brackets(my_string: str):
#     if len(my_string) == 0:
#         return True

#     round_brackets  = "()"
#     square_brackets = "[]"
#     left_brackets   = [round_brackets[0], square_brackets[0]]
#     right_brackets  = [round_brackets[1], square_brackets[1]]

#     [start, end] = [0, len(my_string)]

#     lefts  = 0
#     rights = 0
#     for ch in my_string:
#         if ch in left_brackets:
#             lefts += 1
#         if ch in right_brackets:
#             rights += 1
#     if lefts != rights:
#         return False

#     if lefts:
#         while my_string[start] not in left_brackets and start < len(my_string):
#             start += 1

#         while my_string[end - 1] not in right_brackets and end > 0:
#             end -= 1

#         if start >= end:
#             return False

#         if my_string[start] == round_brackets[0]:
#             current_brackets = round_brackets
#         elif my_string[start] == square_brackets[0]:
#             current_brackets = square_brackets
#         else:
#             return False

#         my_string = my_string[start: end]

#         lefts -= 1
#         [left, right] = current_brackets
#         if not (my_string[0] == left and my_string[-1] == right):
#             return False

    # # remove first and last character
    # return balanced_brackets(my_string[1:-1])

# 2 - Another solution - dealing only with the brackets
# def balanced_brackets(my_string: str):
#     clean = "" # only picks the brackets and ignores other characters
#     for ch in my_string:
#         if ch in "()[]":
#             clean += ch

#     if len(clean) == 0: # if there's no brackets at all, the empty string is already balanced
#         return True

#     if len(clean) < 2: # if not empty, the string must have at least a pair of brackets
#         return False

#     if clean[0] not in "([": # it must begin with left brackets
#         return False

#     opening = clean[0]
#     closing = ")" if opening == "(" else "]"

#     # analyze depth in order to find the right closing
#     depth = 0
#     closing_index = -1
#     for i, ch in enumerate(clean):
#         if ch in "([":
#             depth += 1
#         elif ch in ")]":
#             depth -= 1
#             if depth == 0: # when depth is 0 again, we've found the closing bracket
#                 if ch == closing:
#                     closing_index = i
#                     break
#                 else: 
#                     return False # wrong bracket

#     if closing_index == -1: # in case the closing bracket wasn't found
#         return False

#     if closing_index != len(clean) - 1: # this guarantees the brackets are completely nested
#         return False

#     inner = clean[1:closing_index] # recursively analyzes the inner string; same as inner = clean[1:-1]
#     return balanced_brackets(inner)

# 3 - Course's solution, even simpler
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    if my_string[0] not in "()[]": # if first char is not bracket, pass on to the next char
        return balanced_brackets(my_string[1:])

    if my_string[-1] not in "()[]": # if the last char is not bracket, pass on to the previous char
        return balanced_brackets(my_string[:-1])

    # at this point, we're sure the first and the last char are brackets, we need to see if they're correctly paired
    if my_string[0] == "(" and my_string[-1] == ")":
        return balanced_brackets(my_string[1:-1])
    elif my_string[0] == "[" and my_string[-1] == "]":
        return balanced_brackets(my_string[1:-1])
    else:
        return False

if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok) # True

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok) # True

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok) # False

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok) # False

    ok = balanced_brackets("(x + 1)(y + 1)")
    print(ok) # False (the string is not entirely nested)

    ok = balanced_brackets("((x)")
    print(ok) # False

    ok = balanced_brackets("(x)y)")
    print(ok) # False
