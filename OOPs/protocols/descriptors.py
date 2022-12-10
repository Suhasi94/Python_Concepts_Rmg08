class Descriptor:

    def __get__(self, instance, owner):
        """
            self     - Descriptor object's address
            instance - Employee object's address (e)
            owner    - Employee class' address(Employee)
        """
        return self.pay

    def __set__(self, instance, value):
        if value > 0:
            self.pay = value
        else:
            raise ValueError

    def __delete__(self, instance):
        pass


class Employee:
    pay = Descriptor()

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay


e = Employee("John", 2000)
print(Employee.__dict__)
print(Descriptor.__dict__)
print(e.__dict__)


########################################################################################
class CheckFname:

    def __get__(self, instance, owner):
        print("in check fname get()")
        return self.fname

    def __set__(self, instance, value):
        print("in check fname set()")
        if len(value) < 5:
            raise Exception
        self.fname = value


class CheckLname:

    def __get__(self, instance, owner):
        print("in check lname get()....")
        return self.lname

    def __set__(self, instance, value):
        print("in check lname set()....")
        if len(value) < 5:
            raise Exception
        self.lname = value


class Person:
    fname = CheckFname()
    lname = CheckLname()

    def __init__(self, fname, lname, age):
        self.age = age
        self.fname = fname
        self.lname = lname

    def is_adult(self):
        if self.age > 18:
            print(f"The person {self.fname} {self.lname} is an adult")
        else:
            print(f"The person {self.fname} {self.lname} is a child")


p1 = Person("steve", "jobs__", 11)
p1.is_adult()


############################################################################################
class NameDescriptor:

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        if len(value) < 5:
            raise Exception
        self.name = value


class Person:

    fname = NameDescriptor("fname")
    lname = NameDescriptor("lname")

    def __init__(self, fname, lname, age):
        self.age = age
        self.fname = fname
        self.lname = lname

    def is_adult(self):
        if self.age > 18:
            print(f"The person {self.fname} {self.lname} is an adult")
        else:
            print(f"The person {self.fname} {self.lname} is a child")


p1 = Person("Sayan", "Bhattacharjee", 19)
p1.is_adult()
