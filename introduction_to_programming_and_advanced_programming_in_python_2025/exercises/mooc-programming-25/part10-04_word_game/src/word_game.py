# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        winner = 0
        if len(player1_word) > len(player2_word):
            winner = 1
        elif len(player1_word) < len(player2_word):
            winner = 2
        return winner

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        winner = 0
        p1_vowel_count = 0
        for ch in player1_word:
            if ch in "aeiou":
                p1_vowel_count += 1
        p2_vowel_count = 0

        for ch in player2_word:
            if ch in "aeiou":
                p2_vowel_count += 1

        if p1_vowel_count > p2_vowel_count:
            winner = 1
        elif p1_vowel_count < p2_vowel_count:
            winner = 2

        return winner

class RockPaperScissors(WordGame):
        def __init__(self, rounds: int):
            super().__init__(rounds)

        def round_winner(self, player1_word: str, player2_word: str):
            winner = 0
            options = ["rock", "paper", "scissors"]

            if player1_word == options[0]:
                if player2_word == options[2]:
                    winner = 1
                elif player2_word == options[1]:
                    winner = 2
                elif player2_word not in options:
                    winner = 1

            elif player1_word == options[1]:
                if player2_word == options[2]:
                    winner = 2
                elif player2_word == options[0]:
                    winner = 1
                elif player2_word not in options:
                    winner = 1

            elif player1_word == options[2]:
                if player2_word == options[1]:
                    winner = 1
                elif player2_word == options[0]:
                    winner = 2
                elif player2_word not in options:
                    winner = 1

            elif player1_word not in options:
                if player2_word in options:
                    winner = 2

            return winner

if __name__ == "__main__":
    # p = LongestWord(3)
    # p.play()

    # q = MostVowels(3)
    # q.play()

    r = RockPaperScissors(4)
    r.play()
