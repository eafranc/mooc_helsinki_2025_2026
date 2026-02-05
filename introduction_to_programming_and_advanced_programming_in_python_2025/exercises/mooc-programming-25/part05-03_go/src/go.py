# Write your solution here
def who_won(game_board: list):
    """
    The function returns:
      1: if player 1 won;
      2: if player 2 won
      0: if both players have the same number of pieces on the board

    The game is won by whomever player has more pieces on the board.

    The function takes a two-dimensional array as its argument. The array consists of integer values,
    which represent the following situations:
      1: player 1 game piece
      2: player 2 game piece
      0: empty square
    """
    counter_1 = 0
    counter_2 = 0    
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                counter_1 += 1
            elif game_board[i][j] == 2:
                counter_2 += 1
    if counter_1 > counter_2:
        return 1
    elif counter_2 > counter_1:
        return 2
    else:
        return 0