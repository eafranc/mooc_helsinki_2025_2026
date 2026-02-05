# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        lunch_price   = 2.50
        if payment >= lunch_price:
            self.funds   += lunch_price
            self.lunches += 1
            return payment - lunch_price
        else:
            return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        special_price = 4.30
        if payment >= special_price:
            self.funds   += special_price
            self.specials += 1
            return payment - special_price
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        lunch_price   = 2.50
        if card.balance >= lunch_price:
            card.balance -= lunch_price
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        special_price = 4.30
        if card.balance >= special_price:
            card.balance  -= special_price
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        if amount < 0:
            raise ValueError("You cannot deposit amount less than zero")
        card.balance += amount
        self.funds   += amount


if __name__ == "__main__":
    print("=" * 30)
    print("PART 1 & 2")
##########################################################################
    card = LunchCard(10)
    print("Balance", card.balance) # Balance 10
    result = card.subtract_from_balance(8)
    print("Payment successful:", result) # Payment successful: True
    print("Balance", card.balance) # Balance 2
    result = card.subtract_from_balance(4)
    print("Payment successful:", result) # Payment successful: False
    print("Balance", card.balance) # Balance 2

    print("=" * 30)
    print("PART 3")
##########################################################################
    exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change) # The change returned was 7.5

    change = exactum.eat_lunch(5)
    print("The change returned was", change) # The change returned was 2.5

    change = exactum.eat_special(4.3)
    print("The change returned was", change) # The change returned was 0.0

    print("Funds available at the terminal:", exactum.funds) # Funds available at the terminal: 1009.3
    print("Regular lunches sold:", exactum.lunches) # Regular lunches sold: 2
    print("Special lunches sold:", exactum.specials) # Special lunches sold: 1

    print("=" * 30)
    print("PART 4")
##########################################################################
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros") # Card balance is 2 euros

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result) # Payment successful: False

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros") # Card balance is 102 euros

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result) # Payment successful: True
    print(f"Card balance is {card.balance} euros") # Card balance is 97.7 euros

    print("Funds available at the terminal:", exactum.funds) # Funds available at the terminal: 1100
    print("Regular lunches sold:", exactum.lunches) # Regular lunches sold: 0
    print("Special lunches sold:", exactum.specials) # Special lunches sold: 1
    print("=" * 30)
##########################################################################
