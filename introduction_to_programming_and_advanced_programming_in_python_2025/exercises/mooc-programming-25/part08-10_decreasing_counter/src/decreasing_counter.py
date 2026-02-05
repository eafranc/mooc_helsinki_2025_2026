# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    # Write the rest of the methods here!

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original_value

if __name__ == "__main__":
    print("PART 1")
    counter = DecreasingCounter(10)
    counter.print_value() # value: 10
    counter.decrease()
    counter.print_value() # value: 9
    counter.decrease()
    counter.print_value() # value: 8
    print("===================================")
    print("PART 2")
    counter = DecreasingCounter(2)
    counter.print_value() # value: 2
    counter.decrease()
    counter.print_value() # value: 1
    counter.decrease()
    counter.print_value() # value: 0
    counter.decrease()
    counter.print_value() # value: 0
    print("===================================")
    print("PART 3")
    counter = DecreasingCounter(100)
    counter.print_value() # value: 100
    counter.set_to_zero()
    counter.print_value() # value: 0
    print("===================================")
    print("PART 4")
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value() # value: 51
    counter.reset_original_value()
    counter.print_value() # value: 55
    print("===================================")
