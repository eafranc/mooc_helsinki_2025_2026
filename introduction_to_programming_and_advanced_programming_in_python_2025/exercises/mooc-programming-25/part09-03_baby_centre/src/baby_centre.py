
# WRITE YOUR SOLUTION HERE:
#Note! Do not change the class Person!

class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0

    def weigh(self, person: Person):
        # return the weight of the person passed as an argument
        self.number_of_weigh_ins += 1
        return person.weight

    def feed(self, person: Person):
        person.weight += 1

    def weigh_ins(self):
        return self.number_of_weigh_ins

if __name__ == "__main__":
    print("=" * 30)
    print("PART 1")
#######################################################################################
    baby_centre = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg") # Eric weighs 7 kg
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg") # Peter weighs 85 kg

    print("=" * 30)
    print("PART 2")
#######################################################################################
    baby_centre = BabyCentre()
    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg") # Eric weighs 7 kg
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg") # Peter weighs 85 kg
    print()

    baby_centre.feed(eric)
    baby_centre.feed(eric)
    baby_centre.feed(eric)

    print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg") # Eric weighs 10 kg
    print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg") # Peter weighs 85 kg

    print("=" * 30)
    print("PART 3")
#######################################################################################
    baby_centre = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}") # Total number of weigh-ins is 0

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}") # Total number of weigh-ins is 2

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}") # Total number of weigh-ins is 6
    print("=" * 30)
