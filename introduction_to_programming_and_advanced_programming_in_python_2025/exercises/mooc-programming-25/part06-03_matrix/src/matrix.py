# write your solution here
def read_matrix():
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(",")
            matrix.append(parts)
    for row in range(len(matrix)): # Transform every string element in int value using int()
        for column in range(len(matrix[row])):
            matrix[row][column] = int(matrix[row][column])
    return matrix

def matrix_sum():
    matrix = read_matrix()
    sum_matrix = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            sum_matrix += matrix[row][column]
    return sum_matrix

def matrix_max():
    matrix = read_matrix()
    max_matrix = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] > max_matrix:
                max_matrix = matrix[row][column]
    return max_matrix

def row_sums():
    matrix = read_matrix()
    sums_per_rows = []
    for row in matrix:
        sums_per_rows.append(sum(row))
    return sums_per_rows

if __name__ == "__main__":
    mtx = read_matrix()
    print(mtx)
    sum_mtx = matrix_sum()
    print(sum_mtx)
    max_mtx = matrix_max()
    print(max_mtx)
    sums_per_rows_mtx = row_sums()
    print(sums_per_rows_mtx)
