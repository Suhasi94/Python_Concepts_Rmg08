class Point:
    c = 10

    def __init__(self, v1, v2):
        self.a = v1          # self.__dict__[a] = v1    --> __setattr__
        self.b = v2          # self.__dict__[b] = v2    --> __setattr__

    def __getattribute__(self, item):
        print("getting value....")
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print(" the attribute is missing....")
        raise AttributeError(f"{item} is not an attribute of Point class")

    def __setattr__(self, key, value):
        print("setting value....")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("deleting value....")
        super().__delattr__(item)


# p1 = Point(1, 2)
# p1.a = 10
# print(p1.a)
# # print(p1.x)
#
# del p1.a

#################################################################################
class Sample:

    def __init__(self, name):
        self.name = name


s = Sample("John")


################################################################################
class PositivePoint:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __setattr__(self, key, value):
        if value < 0:
            raise Exception("Value cannot be negative")
        super().__setattr__(key, value)


# p = PositivePoint(-1, 3)
# print(p.a)

#################################################################################
class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __setattr__(self, key, value):
        if key == "fname":
            super().__setattr__(key, value.upper())
        elif key == "lname":
            super().__setattr__(key, value.lower())


e = Employee("steve", "jobs")
print(e.__dict__)
# print(e.fname, e.lname)


##############################################################################
class Employee:

    def __init__(self, fname, lname):
        super().__setattr__("fname", fname)
        super().__setattr__("lname", lname)

    def __setattr__(self, key, value):
        raise Exception("Values cannot be modified")

    def __delattr__(self, item):
        raise Exception("Values cannot be deleted")


# e1 = Employee("john", "jacobs")
# print(e1.__dict__)
# print(e1.fname)
# # e1.fname = "shyam"
# del e1.fname


#################################################################################
class Sample:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, key, value):
        if key not in ("x", "y"):
            raise Exception("Key not found")
        super().__setattr__(key, value)


# s1 = Sample(1, 2)
# print(s1.__dict__)
# s1.z = 3
# print(s1.__dict__)

#################################################################################
# sort based on last character

l = ["google", "microsoft", "amazon", "gmail", "apple"]


def last_char(string):
    return string[-1]


print(sorted(l, key=last_char))

# function protocol
class LastChar:

    def __call__(self, string):
        return string[-1]


last = LastChar()
print(sorted(l, key=last))

########################################################################################
temperatures = [("Bangalore", 25), ("Delhi", 35), ("Chennai", 37), ("Mumbai", 32)]


class Temperature:

    def __call__(self, item):
        return item[-1]


print(sorted(temperatures, key=Temperature()))

########################################################################################
portfolio = [
                {"name": "IBM", "shares": 100, "price": 91.1},
                {"name": "AAPL", "shares": 50, "price": 543.22},
                {"name": "FB", "shares": 200, "price": 21.09},
                {"name": "HPQ", "shares": 35, "price": 31.75},
                {"name": "YHOO", "shares": 45, "price": 16.35}
            ]


class By:

    def __init__(self, key):
        self.key = key

    def __call__(self, item):
        if self.key == "name":
            return item["name"]

        elif self.key == "shares":
            return item["shares"]

        elif self.key == "price":
            return item["price"]

        
print(sorted(portfolio, key=By("name")))
print(sorted(portfolio, key=By("shares")))
print(sorted(portfolio, key=By("price")))

















