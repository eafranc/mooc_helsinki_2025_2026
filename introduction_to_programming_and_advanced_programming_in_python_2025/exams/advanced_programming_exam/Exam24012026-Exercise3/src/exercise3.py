# Write your solution to exercise 3 here
from random import randint

class Dice:
    def __init__(self, sides=6):
        self.__sides = sides

    def __str__(self):
        return f"{self.__sides}-sided dice"

    def roll_dice(self, times: int):
        results = []
        for i in range(times):
            results.append(randint(1, self.__sides))
        return results

class DiceGame:
    def __init__(self, dice: Dice):
        self.__dice = dice
        self.__dices = []
        for i in range(5):
            self.__dices.append(dice)

    def __str__(self):
        return f"The goal of the game is to roll the dice and get 5 of the same number. Using {self.__dice}."

    def roll_once(self):
        roll = []
        for dice in self.__dices:
            [result] = dice.roll_dice(1)
            roll.append(result)
        yatzy = self.__is_yatzy(roll)
        if yatzy:
            print("Yatzy!")
        else:
            print("Rolled 5 dice and got ", end = "")
            for i, res in enumerate(sorted(roll)):
                if i != len(sorted(roll)) -1:
                    print(f"{res}, ", end = "")
                else:
                    print(f"{res}.")

    def __is_yatzy(self, dice_results: list):
        is_yatzy = True
        last_roll = dice_results[0]
        for roll in dice_results:
            if last_roll != roll:
                is_yatzy = False
                break
            last_roll = roll
        return is_yatzy

    def roll_five_of_a_kind(self):
        yatzy = False
        no_of_rolls = 0
        while not yatzy:
            roll = []
            for dice in self.__dices:
                [result] = dice.roll_dice(1)
                roll.append(result)
            yatzy = self.__is_yatzy(roll)
            no_of_rolls += 1
        print(f"It took {no_of_rolls} rolls to get five of a kind.")

if __name__ == "__main__":
    # testing the dices (or die)
    six_sided_dice = Dice()
    eight_sided_dice = Dice(8)

    print(six_sided_dice) # 6-sided dice
    print(eight_sided_dice) # 8-sided dice

    dice_roll = six_sided_dice.roll_dice(5)
    print(dice_roll) # [1, 4, 5, 2, 4]

    second_dice_roll = eight_sided_dice.roll_dice(2)
    print(second_dice_roll) # [8, 1]

    # testing the dice game
    six_sided_dice = Dice()
    game = DiceGame(six_sided_dice)

    print(game) # The goal of the game is to roll the dice and get 5 of the same number. Using 6-sided dice.

    game.roll_once() # Rolled 5 dice and got 2, 2, 3, 4, 6.
    game.roll_once() # Rolled 5 dice and got 1, 1, 2, 5, 6.
    game.roll_once() # Yatzy!
    game.roll_once() # Rolled 5 dice and got 1, 2, 4, 6, 6.

    game.roll_five_of_a_kind() # It took 886 rolls to get five of a kind.

    difficult_game = DiceGame(Dice(10))
    difficult_game.roll_five_of_a_kind() # It took 4490 rolls to get five of a kind.

    easy_game = DiceGame(Dice(1))
    easy_game.roll_once() # Yatzy!
    easy_game.roll_once() # Yatzy!
    easy_game.roll_once() # Yatzy!
    easy_game.roll_once() # Yatzy!
