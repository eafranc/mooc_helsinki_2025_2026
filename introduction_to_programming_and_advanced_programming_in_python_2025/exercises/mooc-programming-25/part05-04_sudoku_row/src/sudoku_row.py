# Write your solution here
def row_correct(sudoku: list, row_no: int):
    square_numbers = list(range(1,10)) # valid numbers: [1, 2, ..., 9] (0 represents an empty square)
    for square in sudoku[row_no]:
        if (square in square_numbers and sudoku[row_no].count(square) > 1):
            return False
    return True

if __name__ == "__main__":

    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0)) # True
    print(row_correct(sudoku, 1)) # False
    print(row_correct(sudoku, 2)) # True
    print(row_correct(sudoku, 3)) # True