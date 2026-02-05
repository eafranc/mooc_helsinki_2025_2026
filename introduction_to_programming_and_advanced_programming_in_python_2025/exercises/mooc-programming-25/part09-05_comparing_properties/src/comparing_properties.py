# Write your solution here:
class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, another: "RealProperty"):
        return self.square_metres > another.square_metres

    def price_difference(self, another: "RealProperty"):
        return abs(self.square_metres * self.price_per_sqm - another.square_metres * another.price_per_sqm)

    def more_expensive(self, another: "RealProperty"):
        return self.square_metres * self.price_per_sqm > another.square_metres * another.price_per_sqm

if __name__ == "__main__":
    print("=" * 30)
    print("PART 1")
##########################################################
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.bigger(downtown_two_bedroom)) # False
    print(suburbs_three_bedroom.bigger(downtown_two_bedroom)) # True

    print("=" * 30)
    print("PART 2")
##########################################################
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.price_difference(downtown_two_bedroom)) # 71600
    print(suburbs_three_bedroom.price_difference(downtown_two_bedroom)) # 35400

    print("=" * 30)
    print("PART 3")
##########################################################
    central_studio = RealProperty(1, 16, 5500)
    downtown_two_bedroom = RealProperty(2, 38, 4200)
    suburbs_three_bedroom = RealProperty(3, 78, 2500)

    print(central_studio.more_expensive(downtown_two_bedroom)) # False
    print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom)) # True
    print("=" * 30)
##########################################################
