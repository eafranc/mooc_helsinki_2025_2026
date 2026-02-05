# Write your solution here
def row_correct(sudoku: list, row_no: int):
    square_numbers = list(range(1,10)) # valid numbers: [1, 2, ..., 9] (0 represents an empty square)
    for square in sudoku[row_no]:
        if (square in square_numbers and sudoku[row_no].count(square) > 1):
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    square_numbers = list(range(1, 10))
    checked_numbers_in_column = []
    for row in sudoku:
        if row[column_no] in square_numbers and row[column_no] in checked_numbers_in_column:
            return False
        checked_numbers_in_column.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    square_numbers = list(range(1, 10))
    checked_numbers = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no +3):
            if sudoku[i][j] in square_numbers and sudoku[i][j] in checked_numbers:
                return False
            checked_numbers.append(sudoku[i][j])
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(len(sudoku)):
        if not row_correct(sudoku, row):
            return False
    for column in range(len(sudoku)):
        if not column_correct(sudoku, column):
            return False
    for block_row in range(0, 9, 3):
        for block_column in range(0, 9, 3):
            if not block_correct(sudoku, block_row, block_column):
                return False
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1)) # False

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(sudoku_grid_correct(sudoku2)) # True