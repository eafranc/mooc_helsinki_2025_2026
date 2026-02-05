# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, lottery_numbers: list):
        self.week = week
        if len(lottery_numbers) == 7:
            self.lottery_numbers = lottery_numbers
        else:
            raise ValueError("There must be 7 lottery numbers")

    def number_of_hits(self, numbers: list):
        return sum([1 if number in self.lottery_numbers else 0 for number in numbers])


    def hits_in_place(self, numbers: list):
        return [number if number in self.lottery_numbers else -1 for number in numbers]

if __name__ == "__main__":
    week5 = LotteryNumbers(5, [1,2,3,4,5,6,7])
    my_numbers = [1,4,7,11,13,19,24]
    print(week5.number_of_hits(my_numbers)) # 3

    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers)) # [1, -1, -1, 10, -1, 20, 30]
