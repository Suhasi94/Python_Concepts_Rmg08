# # single level inheritance
#
class Parent:
    a = 10

    def display(self):
        print(Parent.a)


class Child(Parent):
    b = 20

    def print_(self):
        print(Child.a,Child.b,Parent.a)

#
# print(Parent.__dict__)
# print(Child.__dict__)
# c1 = Child()
# c1.print_()

#
# #######################################################################################
# # multi level
#
class Parent:
    c_name = "ABC"

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class Child(Parent):
    EID = 1

    def display(self):
        print(self.fname)


class Child2(Child):
    pass


# c = Child2("steve", "jobs")
# c.display()
# print(c.c_name)

###########################################################################################
class Parent:
    a = 10

    def display(self):
        print("in Parent display")

    def spam(self):
        print("in Parent Spam")


# independent methods
class Child(Parent):
    def demo(self):
        print("in child demo")


# c = Child()
# c.display()
# c.demo()

#############################################################33
# overriding the Parent class' methods

class Parent:
    a = 10

    def display(self):
        print("in Parent display")

    def spam(self):
        print("in Parent Spam")


class Child1(Parent):

    def display(self):
        print("in Child display")


# c1 = Child1()
# c1.display()
#
# Parent().display()

# partially overriding parent methods

class Parent:
    a = 10

    def display(self):
        print("in Parent display")

    def spam(self):
        print("in Parent Spam")


class Child2(Parent):

    def display(self):
        print("in Child display")
        super().display()


# c2 = Child2()
# c2.display()

#####################################################################################

class Parent:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(self.a, self.b)


class Child3(Parent):

    def __init__(self, x, a, b):
        self.x = x
        super().__init__(a, b)

    def demo(self):
        print(self.x)


# c3 = Child3(10, 1, 2)
# c3.display()

###################################################################################
class Parent1:
    a = 10
    b = 20


class Parent2:
    c = 130
    b = 125


class Child(Parent1, Parent2):
    a = 80
    d = 64


# c = Child()
# print(Child.__mro__)

# ###################################################################################
# accessing class variable through class name
class Sample:
    num = 13

    def display(self):
        print(Sample.num)

class Demo(Sample):
    num = 67


# d = Demo()
# d.display()     # 13
# s = Sample()
# s.display()     # 13

################################################################################
# accessing class variable by creating class method
class Sample:
    num = 13

    def __init__(self, a):
        self.a = a

    @classmethod
    def display(cls):
        print(cls.num)
        # print(self.a)         # NameError

class Demo(Sample):
    num = 67

# d = Demo(10)
# d.display()     # 67
#
# s = Sample(10)
# s.display()     # 13

#######################################################################################
# using self.__class__ to access the class variable

class Sample:
    num = 13

    def __init__(self, other):
        self.other = other

    def display(self):
        print(self.__class__.num)
        print(self.other)

class Demo(Sample):
    """This is Demo class"""            # documentation string
    num = 67

d = Demo(3)
d.display()         # self.__class__.num --> Demo.num --> 67

s = Sample(7)
s.display()         # self.__class__.num --> Sample.num --> 13

print(d.__class__)      # <class '__main__.Demo'>
print(Demo.__dict__)    # {'__module__': '__main__', '__doc__': 'This is Demo class', 'num': 67}
print(d.__doc__)        # This is Demo class

"""
__name__
__dict__
__init__
__call__
__mro__
__dir__
__class__

"""









