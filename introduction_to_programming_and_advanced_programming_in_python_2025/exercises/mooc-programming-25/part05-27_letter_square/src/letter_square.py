# HOW I SOLVED THE EXERCISE:
# The letters on the square follow this pattern:
#  - The number of layers gives the possible letters (eg. layers = 3 --> letters will be A, B and C)
#  - It also gives the possible distances from one element of the matrix to their borders (eg. layers = 3 --> dists.: dist(A) = 2 , dist(B) = 1, dist(C) = 0)
#  - Every element of the matrix has 4 distances from the 4 borders; we will calculate them all and then use the least one
#  - If we have layers = K, the matrix size is S = (2*K - 1), and the 4 distances from element A[i][j] to the 4 borders are: 
#  - distances = [i, j, 2*(layers - 1) - i, 2*(layers - 1) - j]
def put_letter(layers: int, no_row: int, no_col: int):
    """
    Calculates which letter should be at position (no_row, no_col).
    
    The letter is determined by the minimum distance to any border.
    - Distance 0 (border) → outermost letter (e.g., 'C' for layers = 3)
    - Distance 1 → second letter (e.g., 'B')
    - Distance 2 (center) → 'A'
    """
    A_ASCII_value = ord('A')  # bears value 65; conversely chr(65) == 'A'
    
    # Calculate distances to all 4 borders
    distances = [
        no_row,                      # Distance to top
        no_col,                      # Distance to left
        2*(layers - 1) - no_row,     # Distance to bottom
        2*(layers - 1) - no_col      # Distance to right
    ]
    
    main_distance = min(distances)
    letter = chr(A_ASCII_value + (layers - 1) - main_distance) # Formula to determine the letter according to the position of the element on the square
    return letter

def create_empty_square(layers: int):
    """Creates a square matrix filled with zeros"""
    size = 2 * layers - 1
    empty_square = []
    for _ in range(size):  # _ indicates iterator not used
        row = [0] * size
        empty_square.append(row)
    return empty_square

def print_square(square: list):
    """Prints the square matrix"""
    for row in square:
        for element in row:
            print(element, end="")
        print()

def create_square(layers: int):
    """Creates and fills the square with appropriate letters"""
    square = create_empty_square(layers)
    
    for i in range(len(square)):
        for j in range(len(square)):
            square[i][j] = put_letter(layers, i, j)
    print_square(square) # I chose to print the square AND return its list (2-dimensional array or matrix, basically a list of lists (rows))
    return square

def main():
    layers = int(input("Layers: "))
    square = create_square(layers)
main()