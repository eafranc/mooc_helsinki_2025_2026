# Write your solution to exercise 1 here
from math import sqrt

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_from_origo(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

class ComparablePoint(Point):
    def __add__(self, another):
        new_point = ComparablePoint(self.x + another.x, self.y + another.y)
        return new_point

    def __eq__(self, another):
        return self.x == another.x and self.y == another.y

    def __gt__(self, another):
        dist_1 = self.distance_from_origo()
        dist_2 = another.distance_from_origo()
        return dist_1 > dist_2

if __name__ == "__main__":
    point1 = ComparablePoint(1, 1)
    point2 = ComparablePoint(2, 2)

    # testing +
    point3 = point1 + point2
    print(point3) # Point(x=3, y=3)

    # testing ==
    print(point1 == point2) # False
    print(point1 == point1) # True

    # testing >
    print(point2 > point1) # True
    print(point1 > point2) # False
    print(point1 > point1) # False

    # testing method distance_from_origo() - the method is inherited
    print(point1.distance_from_origo()) # sqrt(2) = 1.4142135623730951
    print(point2.distance_from_origo()) # 2 * sqrt(2) = 2.8284271247461903
    print(point3.distance_from_origo()) # 3 * sqrt(2) = 4.242640687119285
