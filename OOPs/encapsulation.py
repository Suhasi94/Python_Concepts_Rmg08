# public access specifiers

class Employee:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def display(self):
        print("in display")

#
# e = Employee("John", 2000)
# print(e.__dict__)
# print(e.name)

######################################################################################
# protected access specifiers (_attr)

class Employee:

    def __init__(self, name, pay):
        self._name = name
        self._pay = pay

    def display(self):
        print("in display")


# e = Employee("John", 2000)
# print(e.__dict__)
# print(e._name)

######################################################################################
# private access specifiers (__attr)

class Employee:

    def __init__(self, name, pay):
        self.__name = name
        self.__pay = pay

    def display(self):
        print("in display")


# e = Employee("John", 2000)
# print(e._Employee__name)
# print(e.__dict__)

#######################################################################################
# accessing protected and private attributes outside the class

class Employee:

    def __init__(self, name, pay):
        self._name = name
        self.__pay = pay

    def get_name(self):
        print("getting name....")
        return self._name

    def get_pay(self):
        print("getting pay....")
        return self.__pay

    def set_name(self, new_name):
        print("setting new name...")
        self._name = new_name


# e = Employee("John", 2000)
# print(e.get_name())
# print(e.get_pay())
# e.set_name("Steve")
# print(e.get_name())

#########################################################################################
# accessing protected variables inside child class
class Parent:
    _a = 10

    def display(self):
        print(self._a)


class Child(Parent):

    def get_a(self):
        print(self._a)


# c = Child()
# c.get_a()
# print(Parent.__dict__)

######################################################################################

# accessing private variables inside child class
class Parent:
    __a = 10

    def display(self):
        print(self.__a)


class Child(Parent):

    def get_a(self):
        print(self.__a)


# c = Child()
# c.get_a()           # AttributeError

######################################################################################
# overriding protected variables inside child class
class Parent:
    _a = 10

    def display(self):
        print(self._a)


class Child(Parent):
    _a = 20

    def get_a(self):
        print(self._a)


# c = Child()
# c.get_a()
# print(dir(Parent()))
# print(dir(Child()))


#####################################################################################
# overriding private variables inside child class
class Parent:
    __a = 10

    def display(self):
        print(self.__a)


class Child(Parent):
    __a = 20

    def get_a(self):
        print(self.__a)


# c = Child()
# c.get_a()
# print(dir(Parent()))
# print(dir(Child()))

###################################################################################









