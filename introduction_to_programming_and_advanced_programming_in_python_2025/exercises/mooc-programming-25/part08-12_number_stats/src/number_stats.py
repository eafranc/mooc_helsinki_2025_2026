# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0
        self.sum     = 0

    def add_number(self, number: int):
        self.numbers  = number
        self.counter += 1
        self.sum     += number

    def count_numbers(self):
        return self.counter

    def get_sum(self):
        return self.sum

    def average(self):
        try:
            avg = self.sum / self.counter
        except:
            avg = 0
        return avg

def main():
    stats      = NumberStats()
    odd_stats  = NumberStats()
    even_stats = NumberStats()
    while True:
        num = int(input("Please type in integer numbers:"))
        if num != -1:
            stats.add_number(num)
            if num % 2:
                odd_stats.add_number(num)
            else:
                even_stats.add_number(num)
        else:
            print("Numbers added:", stats.count_numbers())
            print("Sum of numbers:", stats.get_sum())
            print("Mean of numbers:", stats.average())
            print(f"Sum of even numbers: {even_stats.get_sum()}")
            print(f"Sum of odd numbers: {odd_stats.get_sum()}")
            break
main()

