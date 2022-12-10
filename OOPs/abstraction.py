from abc import ABC, abstractmethod


class BaseClass(ABC):           # Abstract class

    @abstractmethod
    def spam(self):
        pass


class Derived(BaseClass):

    def spam(self):
        print("in spam of derived class")


# d = Derived()
# d.spam()

########################################################################################
class InsufficientFundException(Exception):
    pass


class Bank(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def statement(self):
        pass




class SBI(Bank):

    def __init__(self, balance):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount < 1000:
            raise InsufficientFundException("Minimum amount should be 1000")

        self.balance += amount
        self.transactions.append(f"Rs.{amount} is credited and the balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundException("Invalid amount")

        self.balance -= amount
        self.transactions.append(f"Rs.{amount} is debited and the balance is {self.balance}")

    def statement(self):
        print("----- statement -----")
        for item in self.transactions:
            print(item)

    def check_balance(self):
        print(f"Current balance is {self.balance}")


s = SBI(10000)
s.withdraw(5000)
s.deposit(20000)
s.statement()




















