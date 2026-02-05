# Write your solution here
def longest_series_of_neighbours(ls: list[int]) -> int:
    i          = 0
    count      = 1
    all_counts = []
    while i < len(ls) - 1:
        neighbours_difference = ls[i+1] - ls[i]
        if abs(neighbours_difference) == 1:
            count += 1
            all_counts.append(count)
        else:
            count = 1
        i +=1
    return max(all_counts)

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list)) # 4