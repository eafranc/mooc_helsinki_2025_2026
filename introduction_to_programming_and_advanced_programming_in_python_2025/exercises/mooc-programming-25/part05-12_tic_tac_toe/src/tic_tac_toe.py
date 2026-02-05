# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if not (0 <= x <= 2) or not (0 <= y <=2):
        return False
    elif game_board[y][x] != "":
        return False
    else:
        game_board[y][x] = piece
        return True

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X")) # True
    print(play_turn(game_board, 3, 0, "X")) # False
    print(game_board) # [['', '', 'X'], ['', '', ''], ['', '', '']]