# # normal way
# l1 = [1, 2, 3, 4]
# l2 = [2, 4, 6, 8]
#
# # using class names
# # instances or objects of list class
#
# l1 = list([1, 2, 3, 4])
# l2 = list([1, 2, 3, 4])
#
# # calling append method of list class using instance l1
# l1.append(10)
# print(l1)
# print(l2)
#
# # # calling append method of list class using class name
# list.append(l1, 11)
# print(l1)
#
# l1.pop()
# print(l1)
# print(l2)
#
# # swap first and last element
# l1 = list([1, 2, 3, 4])
# l2 = list([1, 2, 3, 4])
#
# temp = l1[0]
# l1[0] = l1[-1]
# l1[-1] = temp
#
# print(l1)
# l1[0], l1[-1] = l1[-1], l1[0]
# ####################################################################################
# # pascal case
# l2 = [1, 2, 3, 4]
#
#
# class ListExtension:
#
#     def swap(self, list_):
#         temp = list_[0]
#         list_[0] = list_[-1]
#         list_[-1] = temp
#         return list_
#
#
# # creating an instance- of ListExtension class
# l = ListExtension()
# l1 = ListExtension()
#
# # using instance
# print(l.swap([10, 20, 30, 40]))
#
# # classname
# print(ListExtension.swap(l, [10, 20, 30, 40]))
#
# #############################################################################################
# # accessing class variables
#
# class Demo:
#     # class variables
#     a = 10
#     b = 20
#
#
# # using instance
# d = Demo()
# print(d.a)
#
# # using classname
# print(Demo.a)
#
# ##########################################################################################
# # modifying class variable
#
# class Demo:
#     # class variables
#     a = 10
#     b = 20
#
#
# d = Demo()
#
# # modify class variable through instance
# print(d.a)          # 10
# print(Demo.a)       # 10
#
# d.a = 100
#
# print(d.a)          # 100
# print(Demo.a)       # 10
#
# # modifying class variable using classname
# print(d.b)          # 20
# print(Demo.b)       # 20
#
# Demo.b = 50
#
# print(d.b)          # 50
# print(Demo.b)       # 50
#
#
#
# class Sample:
#
#     # class variables
#     a = 10
#     b = 20
#
#
# print(Sample.a)
#
# s = Sample()
# print(s.b)


class Calculator:
    # class variables
    a = 1
    b = 2

    def __init__(self, a, b):   # instance variables or instance dictionary
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a // self.b


# c1 = Calculator(10, 20)
# c2 = Calculator(100, 200)
#
# print(Calculator.__dict__)
# print(c1.__dict__)
# print(c2.__dict__)

#################################################################################

class Bank:

    def __init__(self, bal):
        self.balance = bal

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Rs {amount} has been debited and the available balance is {self.balance} ")
        else:
            print("****** Insufficient balance *******")

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

#
# customer1 = Bank(5000)
# customer2 = Bank(10000)
#
# customer1.transfer(customer2, 2000)
# print(customer1.balance)
# print(customer2.balance)

##############################################################################################

class ShoppingCart:
    products = ["oneplus mobile", "dell laptop", "bosch washing machine", "iphone", "iwatch", "airpods", "nokia mobile"]

    def __init__(self):
        self.cart = []
        self.wishlist = []

    def add_to_cart(self, product):
        if product.lower() in ShoppingCart.products:
            self.cart.append(product)
            print(self.cart)
        else:
            print("Invalid product name")

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
            print(self.cart)

    def add_to_wishlist(self, product):
        if product in ShoppingCart.products:
            self.wishlist.append(product)

# customer1 = ShoppingCart()
# customer1.add_to_cart("Dell laptop")
# print(customer1.cart)
#
# customer1.remove_from_cart("Dell laptop")











