class WordFinder:
    def set_grid(self, grid):
        self.grid_list = []
        for i in range(len(grid)):
            grid_rows = []
            for j in range(len(grid[i])):
                grid_rows.append(grid[i][j])
            self.grid_list.append(grid_rows)

    def count(self, word):
        grid_rows = self.grid_list

        rows = len(grid_rows)
        cols = len(grid_rows[0])
        word_len = len(word)

        directions = [ # each direction is like a vector which "walks" over a direction starting from a cell in the grid
        #   row, col, direction
            (-1, -1, "diag-up-left"   ),
            (-1,  0, "up"             ),
            (-1,  1, "diag-up-right"  ),
            ( 0, -1, "left"           ),
            ( 0,  1, "right"          ),
            ( 1, -1, "diag-down-left" ),
            ( 1,  0, "down"           ),
            ( 1,  1, "diag-down-right")
        ]

        results = []
        for row in range(rows):
            for col in range(cols):
                for d_row, d_col, dir in directions:
                    if self.is_palindrome(word):
                        if word_len == 1:
                            if (d_row, d_col, dir) != directions[4]: # if a word has only one char, all the 8 directions will find the same char
                                continue
                        if  (d_row, d_col, dir) == directions[0] or\
                            (d_row, d_col, dir) == directions[1] or\
                            (d_row, d_col, dir) == directions[2] or\
                            (d_row, d_col, dir) == directions[3]:
                            continue # if a word is a palindrome, its symmetry will be found twice by opposite directions
                        

                    # Verifies if the word fits in the tested direction
                    end_row = row + d_row * (word_len - 1)
                    end_col = col + d_col * (word_len - 1)

                    if not (0 <= end_row < rows and 0 <= end_col < cols):
                        continue #if doesn't fit it goes to the next direction

                    # Verifies letter by letter
                    found = True
                    for i in range(word_len):
                        check_row = row + d_row * i
                        check_col = col + d_col * i

                        if self.grid_list[check_row][check_col] != word[i]:
                            found = False
                            break

                    if found:
                        results.append((row, col, dir))
        return len(results)

    def is_palindrome(self, word):
        listed_word = [ch for ch in word]
        inverted_word = listed_word[::-1]
        return listed_word == inverted_word

    def print_grid(self, grid_rows):
        print("   0  1  2  3  4  5  6  7  ")
        print("   ______________________")
        for i in range(len(grid_rows)):
            print(f"{i} |", end = "")
            for j in range(len(grid_rows[i])):
                print(f"{grid_rows[i][j]}  ", end = "")
            print()

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)
    finder.print_grid(finder.grid_list)

    print()
    print()

    print(finder.count("TIRA")) # 7
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0
