class Employee:

    fname = "steve"
    lname = "jobs"
    salary = 2000

    def display(self):
        print(f"the employee {Employee.fname} {Employee.lname} has a salary of {Employee.salary}")


# e1 = Employee()
#
# # calling a method using classname
# Employee.display(e1)
# print(Employee.__dict__)        # class dictionary
# print(dir(Employee))
#
# print()
# # calling a method using instance
# e1.display()
# print(e1.__dict__)              # instance dictionary
# print(dir(e1))

###############################################################################################
# using instances to access the class variables
class Employee:

    fname = "steve"
    lname = "jobs"
    salary = 2000

    def display(self):
        print(f"the employee {self.fname} {self.lname} has a salary of {self.salary}")

#
# emp1 = Employee()       # steve, jobs, 2000
# emp1.display()
#
# emp2 = Employee()       # john, sam, 3000
# emp2.display()
#
# ###############################################################################################
# # instantiating a class using instance variables - constructor

class Employee:

    # creating instance variables
    def __init__(self, firstname, lastname, salary):     # constructor
        self.fname = firstname
        self.lname = lastname
        self.salary = salary

    def display(self):
        print(self)
        print(Employee)
        print(f"the employee {self.fname} {self.lname} has a salary of {self.salary}")

#
# emp1 = Employee("steve", "jobs", 2000)       # steve, jobs, 2000
# emp1.display()
#
# emp2 = Employee("john", "sam", 3000)       # john, sam, 3000
# emp2.display()

# #################################################################################################

class Points:
    # class variables
    a = 12
    b = 14

    def __init__(self, a, b):       # instance variables
        self.a = a
        self.b = b

#
# p1 = Points(1, 2)
# p2 = Points(10, 20)
#
# # __dict__ --> returns a dictionary of attributes present in the class or instances
# print(Points.__dict__)      # class dictionary
# print(p1.__dict__)          # instance dictionary
# print(p2.__dict__)          # instance dictionary

# #############################################################################################
#
class Points:

    def __init__(self, a, b):       # instance variables
        self.a = a
        self.b = b

    def move(self, x, y):
        self.a = self.a + x
        self.b = self.b + y


# p1 = Points(1, 2)
# p2 = Points(10, 20)
#
# print(p1.__dict__)
# p1.move(12, 15)
# print(p1.__dict__)

# ################################################################################################
# # constructor with default values
class Points:

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b


# p1 = Points(10, 20)
# print(p1.__dict__)      # {"a": 10, "b": 20}
#
# p2 = Points(13, 87)
# print(p2.__dict__)      # {"a": 13, "b": 87}
#
# p3 = Points()
# print(p3.__dict__)      # {"a": 0, "b": 0}

# #################################################################################
# # constructor with variable number of arguments

class Employee:

    def __init__(self, fname, lname, pay, *args):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.args = args

#
# emp = Employee("steve", "jobs", 2000, "hello", "hai", 12,9)
# print(emp.__dict__)

# #################################################################################################
# # function overloading
#
# def add(a, b, c=0):
#     print(a + b + c)
#
#
# add(1, 2, 3)
# add(1, 2)
#
# # constructor overloading
# class Point:
#
#     def __init__(self, a=0, b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
# p1 = Point()
# print(p1.__dict__)
#
# p2 = Point(1)
# print(p2.__dict__)
#
# p3 = Point(1, 2)
# print(p3.__dict__)
#
# p4 = Point(1, 2, 3)
# print(p4.__dict__)








