def find_rounds(numbers):
    result = []
    limit = min(numbers)
    while limit != max(numbers) + 1:
        i = 0
        round_collection = []
        while i < len(numbers):
            if numbers[i] == limit:
                round_collection.append(numbers[i])
                limit += 1
            i += 1
        result.append(round_collection)
    return result

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
