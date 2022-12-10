# # inbuilt function polymorphism - len()
#
# print(len("hai"))                   # 3
# print(len([1, 2, 3, "hello"]))      # 4
# print(len({"a": 1, "b": 2}))        # 2
#
#
# # operator overloading
#
# # addition(+)
# print(1 + 2)            # 3
# print("hai" + "hello")  # haihello
#
# # multiplication(*)
# print(3 * 9)            # 27
# print("hai" * 2)        # haihai
#
# l = [10, 20, 30]
# print(*l)               # 10 20 30
#
# def add(*args):
#     print(args)
#
#
# add(1, 2, 3, 4, 5)
#
#
# # subtraction(-)
# print(19 - 15)          # 4
# print({1, 2, 3, 4} - {1, 2})        # {3, 4}
#
#
# ###########################################################################
# # polymorphism in functions
#
# def add(a=0, b=0, c=0):
#     print(a + b + c)
#
#
# add(1)
# add(1, 2)
# add(1, 2, 3)

################################################################################
# polymorphism in class

class Demo:

    def spam(self):
        print("in Demo.spam")


class Sample:

    def spam(self):
        print("in Sample.spam")


# d = Demo()
# s = Sample()
#
# print(d.spam())
# print(s.spam())

################################################################################
from functools import singledispatch, singledispatchmethod

@singledispatch
def add(a):
    print("in add")

@add.register(int)
def _(a):
    print("int")
    print(a + 1)

@add.register(float)
def _(a):
    print("float")
    print(a + 1.2)

# add(1.2)
# add(2)


class Calculator:

    @singledispatchmethod
    def add(self, a):
        print("in add")

    @add.register(int)
    def _(self, a):
        print("int")
        print(a + 1)

    @add.register(float)
    def _(self, a):
        print("float")
        print(a + 1.2)


# c = Calculator()
# c.add(1)
# c.add(1.6)

##################################################################################
from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    print("int, int")
    print(a + b)


@dispatch(float, float)
def add(a, b):
    print("float, float")
    print((a + 1.2) + (b + 8.7))

@dispatch(float, int)
def add(a, b):
    print("float, float")
    print((a + 1.2) + (b + 8.7))


# add(1, 2.2)











