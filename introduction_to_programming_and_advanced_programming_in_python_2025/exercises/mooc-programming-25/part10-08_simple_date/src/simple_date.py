# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, another):
        is_equal = True if (self.day == another.day and self.month == another.month and self.year == another.year) else False
        return is_equal

    def __ne__(self, another):
        is_not_equal = not (self == another)
        return is_not_equal

    def __lt__(self, another):
        # ONE WAY
        # is_lt = True if int(f"{self.year:04d}{self.month:02d}{self.day:02d}") - int(f"{another.year:04d}{another.month:02d}{another.day:02d}") < 0 else False
        # return is_lt

        # ANOTHER WAY
        self_total_days = self.year * 360 + (self.month - 1) * 30 + self.day
        another_total_days = another.year * 360 + (another.month - 1) * 30 + another.day
        is_lt = True if self_total_days < another_total_days else False
        return is_lt

    def __gt__(self, another):
        # ONE WAY
        # is_gt = True if int(f"{self.year:04d}{self.month:02d}{self.day:02d}") - int(f"{another.year:04d}{another.month:02d}{another.day:02d}") > 0 else False
        # return is_gt

        # ANOTHER WAY
        self_total_days = self.year * 360 + (self.month - 1) * 30 + self.day
        another_total_days = another.year * 360 + (another.month - 1) * 30 + another.day
        is_gt = True if self_total_days > another_total_days else False
        return is_gt

    def __add__(self, days_to_add: int):
        # ONE WAY
        # add_days = SimpleDate(self.day, self.month, self.year)
        # for i in range(days_to_add):
        #     add_days.day += 1
        #     if add_days.day > 30:
        #         add_days.day = 1
        #         add_days.month += 1
        #         if add_days.month > 12:
        #             add_days.month = 1
        #             add_days.year += 1
        # return add_days

        # ANOTHER WAY - MUCH FASTER
        total_days = self.year * 360 + (self.month - 1) * 30 + self.day # rearrange the date in terms of total of days, consider 1 to offset month
        total_days += days_to_add                                       # (since there's no month 0)
        remaining_days = total_days % 360

        new_year  = total_days // 360
        new_month = (remaining_days - 1) // 30 + 1 # again 1 to offset days (there's no day 0)
        new_day   = (remaining_days - 1) % 30 + 1
        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, another):
        self_total_days = self.year * 360 + (self.month - 1) * 30 + self.day
        another_total_days = another.year * 360 + (another.month - 1) * 30 + another.day
        diff_days = abs(self_total_days - another_total_days)
        return diff_days

if __name__ == "__main__":
######################################################################
    print("=" * 50)
    print("PART 1")

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1) # 4.10.2020
    print(d2) # 28.12.1985
    print(d1 == d2) # False
    print(d1 != d2) # True
    print(d1 == d3) # False
    print(d1 < d2) # False
    print(d1 > d2) # True
######################################################################
    print("=" * 50)
    print("PART 2")

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1) # 4.10.2020
    print(d2) # 28.12.1985
    print(d3) # 7.10.2020
    print(d4) # 8.2.1987
######################################################################
    print("=" * 50)
    print("PART 3")

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1) # 28
    print(d1-d2) # 28
    print(d1-d3) # 12516

    print("=" * 50)
######################################################################
