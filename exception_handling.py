"""
try
except
"""

# default except block

# a = 10
# b = 3
#
# try:
#     print(x)        # NameError
#     print(a/b)      # ZeroDivisionError
#
# except:
#     b += 2
#     print(a/b)

############################################################################
# specific exception block

# a = 10
# b = 0
#
# try:
#     print(a / b)  # ZeroDivisionError
#     print(x)        # NameError
#
#
# except ZeroDivisionError as error_msg:
#     print(error_msg)
#     b += 2
#     print(a/b)

####################################################################################

a = 10
b = 0

try:
    print(x)  # NameError
    print(a / b)  # ZeroDivisionError


except BaseException as error_msg:
    print(error_msg)
    b += 2
    print(a/b)

#####################################################################

a = 10

# try:5
#     try:
#         print(x)
#     except:
#         print("no variable x")
#
#
# except:
#     try:
#         pass
#     except:
#         pass
#
# except:


######################################################################################

# a = 10
# b = 0

# try:
#     print(x)  # NameError
#     print(a / b)  # ZeroDivisionError
#
#
# except NameError as error_msg:
#     print(error_msg)
#     raise error_msg
#
#
# except ZeroDivisionError as error_msg:
#     b += 2
#     print(a / b)

##################################################################################

# a = 10
# b = 0
#
# try:
#     print(x)
#     print(a/b)
#
#
# except ZeroDivisionError as error_msg:
#     print(error_msg)
#
# finally:
#     print("hello world")


############################################################################

# a = 10
# b = 0
#
# try:
#     print(a/b)
#     print("hai")
#
#
# except ZeroDivisionError as error_msg:
#     print(error_msg)
#
# else:
#     print("hello world")



###########################################################################

class InsufficientBalanceException(BaseException):
    pass


class Bank:

    def __init__(self, bal):
        self.balance = bal

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Rs {amount} has been debited and the available balance is {self.balance} ")
        else:
            raise InsufficientBalanceException("Insufficient balance")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Rs {amount} has been credited and the available balance is {self.balance} ")

    def check_balance(self):
        print(f"The available balance is {self.balance} ")

    def transfer(self, customer, amount):
        # deducting amount from customer1
        self.balance -= amount
        # crediting amount to customer2
        customer.balance += amount


# customer1 = Bank(5000)
# customer2 = Bank(10000)
#
# customer1.withdraw(6000)






