# integer - int()

a = 10      # object of integer class
print(a)        # 10
print(type(a))  # <class 'int'>


a = int(10)     # object of integer class
print(a)
print(type(a))

####################################################################################
# float - float()

b = 1.2
print(b)
print(type(b))

b = float(1.2)
print(b)
print(type(b))

#############################################################################
# complex - complex()

c = 1 + 2j
print(c)
print(type(c))

c = complex(1+2j)
print(c)
print(type(c))

c = complex(1, 2)
print(c)
print(type(c))

####################################################################################
# boolean - bool()

a = True
print(a)
print(type(a))

a = False
print(a)
print(type(a))

#########################################################
# default values

# integer
a = 0
a1 = int()

# float
f = 0.0
f1 = float()

# complex
c = 0j
c1 = complex()

# boolean
b = False
b1 = bool()

###############################################################################
# operations on integer

num1 = 10
num2 = 20

print(num1 + num2)      # 30
print(num1 - num2)      # -10
print(num1 * num2)      # 200
print(num2 / num1)      # 2
print(num2 % num1)      # 0
print(num1 // num2)     # 0
print(2 ** 3)           # 8
print()

num = -92
print(abs(num))
print(divmod(7, 3))

##############################################################################
# functions on floating point numbers

a = -1.2
print(abs(a))
print(round(3.141))
print(round(3.141, 1))
print(round(3.161, 1))
print(round(3.141, 2))
print()

print(round(2.5))       # 2
print(round(3.5))       # 4

import math
print(math.trunc(3.78))
print(round(2.99))




























































