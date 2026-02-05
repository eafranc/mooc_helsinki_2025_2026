# Write your solution to exercise 2 here
class Car:
    year = 0

    def __init__(self, brand: str, purchase_year: int, purchase_price: int):
        self.brand = brand
        self.purchase_year = purchase_year
        self.purchase_price = purchase_price

        self.distance = 0
        self.costs = 0
        self.expenses = 0
        self.value = purchase_price

        if self.purchase_year > Car.year:
            Car.year = self.purchase_year

    def __str__(self):
        return f"{self.brand} purchase year {self.purchase_year}, value {int(self.value)}"

    def set_year(self, new_year: int):
        if new_year > Car.year:
            Car.year = new_year

    def drive(self, distance_driven: int, cost_per_kilometer: float):
        self.distance += distance_driven
        self.costs += cost_per_kilometer * distance_driven

    def add_expense(self, expense: int):
        self.expenses += expense

    def distance_driven_by_car(self):
        return self.distance

    def current_value(self):
        depreciation_rate = 0.15
        self.value = self.purchase_price * ((1 - depreciation_rate) ** (Car.year - self.purchase_year))
        return int(self.value)

    def cost_per_kilometer(self):
        depreciation = self.purchase_price - self.current_value()
        all_costs = self.costs + self.expenses + depreciation

        if self.distance == 0:
            raise ValueError("Distance driven cannot be zero")

        return all_costs / self.distance

if __name__ == "__main__":
    toyota = Car("Toyota", 2020, 10000)
    print(toyota)
    # Toyota: purchase year 2020, value 10000
    toyota.drive(100, 0.10)
    print(f"Distance driven with Toyota: {toyota.distance_driven_by_car()}")
    # Distance driven with Toyota: 100
    toyota.set_year(2021)
    print(f"Value of Toyota in 2021: {toyota.current_value()}")
    # Value of Toyota in 2021: 8500
    print(toyota)
    # Toyota: purchase year 2020, value 8500
    print(f"Cost per kilometer for Toyota in 2021: {toyota.cost_per_kilometer()}")
    # Cost per kilometer for Toyota in 2021: 15.1
    toyota.set_year(2022)
    print(f"Value of Toyota in 2022: {toyota.current_value()}")
    # Value of Toyota in 2022: 7224
    bmw = Car("BMW", 2023, 20000)
    print(f"Value of Toyota after purchasing BMW: {toyota.current_value()}")
    # Value of Toyota after purchasing BMW: 6141
    bmw.drive(200, 0.12)
    bmw.drive(300, 0.13)
    print(f"Distance driven with BMW: {bmw.distance_driven_by_car()}")
    # Distance driven (BMW): 500
    print(f"Cost per kilometer for BMW in 2023: {bmw.cost_per_kilometer()}")
    # Cost per kilometer for BMW in 2023: 0.126
    bmw.add_expense(1000)
    print(f"Cost per kilometer for BMW after a 1000 euro service: {bmw.cost_per_kilometer()}")
    # Cost per kilometer for BMW after a 1000 euro service: 2.126
