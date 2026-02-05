# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    def __service_charge(self):
        service_percentage = 0.01
        self.__balance *= (1 - service_percentage)

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        else:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        else:
            self.__balance -= amount
            self.__service_charge()

    # getter - balance
    @property
    def balance(self):
        return self.__balance

    # # setter - balance
    # @balance.setter
    # def balance(self, balance: float):
    #     if balance >= 0:
    #         self.__balance = balance
    #     else:
    #         raise ValueError("Amount cannot be negative")

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance) # 891.0
    account.deposit(100)
    print(account.balance) # 981.09
