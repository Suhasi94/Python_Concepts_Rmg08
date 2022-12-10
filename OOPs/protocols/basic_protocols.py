l = [10, 20, 30, 40]

# container protocol
"""
1. __contains__(self, obj)
2. __len__(self)
3. __getitem__(self, index)
4. __setitem__(self, index, value)
5. __delitem__(self, name)
"""

print(l[1])
print(l.__getitem__(1))

print(len(l))
print(l.__len__())

l[2] = 35
print(l)
l.__setitem__(2, 30)
print(l)

print(10 in l)
print(l.__contains__(10))


########################################################################################
# implementing container protocol in custom class Point
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __len__(self):
        return 2

    def __getitem__(self, item):
        if item == 0:
            return self.a
        elif item == 1:
            return self.b
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value
        else:
            raise IndexError("Index out of range")

    def __delitem__(self, index):
        raise AttributeError("delete operation cannot be performed")

    def __contains__(self, value):
        if value == self.a or value == self.b:
            return True
        return False


p = Point(4, 9)

# finding length of object p
print(len(p))
print(p.__len__())

# accessing the attributes of object p using indexing
print(p[0])
print(p[1])

# assigning new values to the attributes using indexing
p[0] = 17
p[1] = 37

# accessing the attributes of object p using indexing after setting it to new values
print(p[0])
print(p[1])

# deleting the attributes of object p using indexing
del p[0]

# checking for membership among the attributes
print(15 in p)
print(37 in p)


#####################################################################################
# extending the above Point class for only positive values of a and b

class PositivePoint(Point):

    def __setitem__(self, index, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        super().__setitem__(index, value)


#####################################################################################
# extending the Point class for a range of values for both a (1-100) and b (1-50)

class RangePoint(Point):

    def __setitem__(self, index, value):
        if index == 0:
            if value in range(1, 100):
                super().__setitem__(index, value)
            else:
                raise Exception

        elif index == 1:
            if value in range(1, 50):
                super().__setitem__(index, value)
            else:
                raise Exception


r = RangePoint(1, 3)
r[0] = 199              # Exception

#################################################################################
# number protocols
"""
1. __add__(self, other)
2. __sub__(self, other)
3. __mul__(self, other)
"""


class PointNumber(Point):

    def __init__(self, a, b):
        super().__init__(a, b)

    def __add__(self, other):
        return self.a + other.b

    def __sub__(self, other):
        return self.a - other.b

    def __mul__(self, other):
        return self.a * other.b


p = Point(3, 8)
print(p.a + p.b)
print(p[0] + p[1])


#####################################################################################
class PointNumber(Point):

    def __init__(self, a, b):
        super().__init__(a, b)

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __mul__(self, other):
        return self.a * other.a, self.b * other.b


p1 = PointNumber(6, 72)
p2 = PointNumber(5, 8)
print(p1 + p2)          # self -> p1, other -> p2
print(p1 - p2)
print(p1 * p2)

######################################################################
# comparison protocol

"""
1. __eq__()
2. __lt__()
3. __gt__()
4. __le__()
5. __ge__()
6. __ne__()

"""


# custom class with comparison protocol
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, value):
        if self.a == value and self.b == value:
            return True
        else:
            return False

    def __lt__(self, value):
        if self.a < value and self.b < value:
            return True
        return False

    def __gt__(self, value):
        if self.a > value and self.b > value:
            return True
        return False

    def __ne__(self, value):
        if self.a != value and self.b != value:
            return True
        return False


p1 = Point(2, 1)
print(p.a == p.b)
print(p.__eq__(5))
print(p.a < p.b)


#####################################################################################
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        return False

    def __gt__(self, other):
        if self.a > other.a and self.b > other.b:
            return True
        return False

    def __lt__(self, other):
        if self.a < other.a and self.b < other.b:
            return True
        return False

    def __ne__(self, other):
        if self.a != other.a and self.b != other.b:
            return True
        return False


p1 = Point(2, 7)
p2 = Point(8, 4)
print(p1 == p2)
print(p2 == p1)

print(p1.__eq__(p2))
print(p2.__eq__(p1))

######################################################################################
t = (1, 2, 3, 4)
print(bool(t))

# Truthiness implementation using __bool__ and __len__

"""
* By default, an object is considered true unless its class defines either a __bool__() method that 
  returns False or a __len__() method that returns zero, when called with the object.
  
In the below example,
* Point class has not implemented either __bool__ or __len__
* So by default, the boolean value of point object is always considered as True
"""


class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b


p = Point(1, 2)
print(bool(p))      # True

p = Point(0, 0)
print(bool(p))      # True


#######################################################################################
# implementing __bool__ to evaluate the truthiness of Point class
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # By default __bool__ is called to evaluate Truthiness of the object.
    def __bool__(self):
        if self.a > 0 and self.b > 0:
            return True
        return False


print()
p1 = Point(1, 2)
print(bool(p1))

p1 = Point(-1, 2)
print(bool(p1))

p1 = Point(1, 0)
print(bool(p1))


################################################################################
# implementing __len__ to evaluate the truthiness of Point class
class Point:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # __len__ function is called as fallback mechanism if __bool__ is not defined on the object
    # If both __bool__ and __len__ are not defined, the object is considered to be evaluated to True
    def __len__(self):
        return self.a + self.b


p1 = Point(1, 2)
print(bool(p1))

p1 = Point(-1, 2)
print(bool(p1))

p1 = Point(0, 0)
print(bool(p1))
