class Employee:

    def __init__(self, name, pay):
        self.name = name
        self.__pay = pay

    @property
    def pay(self):
        print("getting pay....")
        return self.__pay

    @pay.setter
    def pay(self, new_pay):
        print("setting new pay...")
        raise ValueError("Salary cannot be modified")

    @pay.deleter
    def pay(self):
        del self.__pay


# e = Employee("John", 3000)
# print(e.pay)
# # e.pay(2000)
# # e.pay = 2500
# # print(e.pay)
# #del e.pay


#############################################################################################################
"""
1. create a class named Circle with instance variable is radius which should always be set to an integer
2. create a class named Person with username and age, the user should not be able to delete the username and
   set the age to less than 18
"""

"""
accessing an attribute

1. attribute protocol - __getattribute__, __getattr__, __setattr__, __delattr
2. property decorator - @property, @prop_name.setter, @prop_name.deleter
3. descriptor protocol - __get__, __set__, __delete__

"""

