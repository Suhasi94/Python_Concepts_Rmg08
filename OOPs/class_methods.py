# change or modify the class variable using instances

class Employee:

    name = "John"
    pay = 2000

    @classmethod
    def change_name(cls, new_name):
        cls.name = new_name


# e1 = Employee()
# e2 = Employee()
# print(Employee.name)
# e1.change_name("steve")




class Demo:

    def __init__(self, a):
        self.a = a

    @classmethod
    def construct_object(cls):
        d1 = cls(10)
        return d1


# normal way of constructing an object
# d1 = Demo(20)
#
# object_ = Demo.construct_object()
# print(object_.a)


#######################################################################################

class EmployeeDetails:
    company_name = "XYZ"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def create_email(cls):
        obj = cls("John", "25", 2000)
        print(obj)
        email = f"{obj.name}_@{cls.company_name}.com"
        return email

#
# print(EmployeeDetails.create_email())
#
# ##########################################################################################
class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return Circle.PI * (self.radius ** 2)

    @classmethod
    def calculate_area_using_diameter(cls, d):
        radius = d / 2
        obj = cls(radius)
        print(obj.calculate_area())


# Circle.calculate_area_using_diameter(10)
#####
# class Circle:
#     PI = 3.14
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return Circle.PI * (self.radius ** 2)
#
#     @classmethod
#     def create_object_with_diameter(cls, d):
#         radius = d/2
#         obj = cls(radius)
#         return obj
#
#
# # c1 = Circle.create_object_with_diameter(10)
# # c1.calculate_area()
#
# ########################################################################################
# # independent function outside a class
def spam():
    print("hello everyone")


class Sample:

    # function independent of class and object
    @staticmethod
    def spam(message):
        print(message)


s = Sample()
s1 = Sample()
s.spam("hello")
Sample.spam("hai")



















































