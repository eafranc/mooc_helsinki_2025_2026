# Write your solution here
from fractions import Fraction
def fractionate(amount: int):
    f = Fraction(1, amount)
    return [f] * amount

if __name__ == "__main__":
    fraction = fractionate(5)
    print(fraction)
