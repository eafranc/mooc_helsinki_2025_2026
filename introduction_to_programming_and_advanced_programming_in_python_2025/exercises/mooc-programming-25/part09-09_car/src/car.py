# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        # Reminder: the car consumes 1 L of petrol per km
        self.__tank     = 0
        self.__odometer = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__tank} litres"

    def fill_up(self):
        self.__tank = 60

    def drive(self, km: int):
        if km > 0:
            if km > self.__tank:
                km = self.__tank # Reminder: the car consumes 1 L of petrol per km
            self.__odometer += km
            self.__tank     -= km


if __name__ == "__main__":
    car = Car()
    print(car) # Car: odometer reading 0 km, petrol remaining 0 litres
    car.fill_up()
    print(car) # Car: odometer reading 0 km, petrol remaining 60 litres
    car.drive(20)
    print(car) # Car: odometer reading 20 km, petrol remaining 40 litres
    car.drive(50)
    print(car) # Car: odometer reading 60 km, petrol remaining 0 litres
    car.drive(10)
    print(car) # Car: odometer reading 60 km, petrol remaining 0 litres
    car.fill_up()
    car.fill_up()
    print(car) # Car: odometer reading 60 km, petrol remaining 60 litres
