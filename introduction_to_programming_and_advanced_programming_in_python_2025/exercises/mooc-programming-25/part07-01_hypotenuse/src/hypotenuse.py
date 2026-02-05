# Write your solution here
def hypotenuse(leg1: float, leg2: float):
    from math import sqrt

    hyp = sqrt( (leg1 ** 2) + (leg2 ** 2))
    return hyp

if __name__ == "__main__":
    d = hypotenuse(3, 4)
    print(d)
