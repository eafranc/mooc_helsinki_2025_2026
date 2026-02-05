# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, another):
        result = True if self._euros == another._euros and self._cents == another._cents else False
        return result

    def __ne__(self, another):
        result = True if self._euros != another._euros or self._cents != another._cents else False
        return result

    def __gt__(self, another):
        result = True if self._euros + 0.01 * self._cents > another._euros + 0.01 * another._cents else False
        return result

    def __lt__(self, another):
        result = True if self._euros + 0.01 * self._cents < another._euros + 0.01 * another._cents else False
        return result

    def __add__(self, another):
        add_result = 100 * (self._euros + another._euros) + (self._cents + another._cents)
        add_money = Money(int(add_result // 100), int(add_result % 100))
        return add_money

    def __sub__(self, another):
        sub_result = 100 * (self._euros - another._euros) + (self._cents - another._cents)
        if sub_result < 0:
            raise ValueError("a negative result is not allowed")
        else:
            sub_money = Money(int(sub_result // 100), int(sub_result % 100))
        return sub_money

if __name__ == "__main__":
######################################################################
    print("=" * 50)
    print("PART 1")

    e1 = Money(4, 10)
    e2 = Money(2, 5)  # two euros and five cents

    print(e1) # 4.10 eur
    print(e2) # 2.05 eur
######################################################################
    print("=" * 50)
    print("PART 2")

    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)

    print(e1) # 4.10 eur
    print(e2) # 2.05 eur
    print(e3) # 4.10 eur
    print(e1 == e2) # False
    print(e1 == e3) # True
######################################################################
    print("=" * 50)
    print("PART 3")

    e1 = Money(4, 10)
    e2 = Money(2, 5)

    print(e1 != e2) # True
    print(e1 < e2) # False
    print(e1 > e2) # True
######################################################################
    print("=" * 50)
    print("PART 4")

    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3) # 7.00 eur
    print(e4) # 1.10 eur

    e5 = e2-e1
# Traceback (most recent call last):
# File "money.py", line 416, in
# e5 = e2-e1
# File "money.py", line 404, in sub
# raise ValueError(f"a negative result is not allowed")
# ValueError: a negative result is not allowed
######################################################################
    print("=" * 50)
    print("PART 5")

    print(e1) # 4.05 eur
    e1.euros = 1000
    print(e1) # 1000.05 eur

    print("=" * 50)
######################################################################
