# Write your solution here
def roll(die: str):
    from random import choice
    # Dice:
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]
    if   die == "A":
        return choice(A)
    elif die == "B":
        return choice(B)
    elif die == "C":
        return choice(C)

def play(die1: str, die2: str, times: int):
    wins1 = 0
    wins2 = 0
    ties  = 0
    for i in range(times):
        result1 = roll(die1)
        result2 = roll(die2)
        if   result1 > result2:
            wins1 += 1
        elif result1 < result2:
            wins2 += 1
        else:
            ties += 1
    return (wins1, wins2, ties)

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
# 3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
# 2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
# 4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
# (292, 708, 0)
# (249, 273, 478)
