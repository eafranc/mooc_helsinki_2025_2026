# Write your solution here
def times_ten(start_index: int, end_index: int):
    dictionary = {}
    for i in range(start_index, end_index+1):
        dictionary[i] = 10*i
    return dictionary

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d) # {3: 30, 4: 40, 5: 50, 6: 60}

