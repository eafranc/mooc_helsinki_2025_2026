# Write your solution here
def transpose(matrix: list): # We assume it is a square matrix
    x = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i < j: # We only need to chance the elements "above" the main diagonal
                x            = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = x

if __name__ == "__main__":
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]    
    ]
    print("Before transposing the matrix:\n")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]} ", end="")
        print()
    print("=====================")
    print("After transposing the matrix:\n")
    transpose(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]} ", end="")
        print()
    print("=====================")