# msg = "hello everyone"
# msg1 = "hai"
# msg2 = "greetings!!!!"
#
# for _ in range(5):
#     print(msg)
#
# for _ in range(5):
#     print(msg1)
#
# for _ in range(5):
#     print(msg2)


# def func_name(message):     # parameters/ formal arguments
#     for _ in range(5):
#         print(message)


# func_name("hai")    # arguments/ actual arguments
# func_name("hello everyone")
# func_name("greetings!!!")

############################################################################################

# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
#
# res = add(1, 2)
# print(res)

#######################################################################################
# Types of arguments

# def add(a, b):
#     print(a + b)
#
#
# add(1, 2)           # positional arguments
# add(b=1, a=2)       # keyword arguments
# add(1, b=2)         # combination
# add(1, a=2, b=2)    # TypeError
#
# ################################################################################
# # positional only arguments(/) - parameters before "/" must take only positional arguments
#
# def add(a, b, /):
#      print(a + b)
#
# add(1, 2)
# add(a=1, b=2)     # TypeError
#
#
# def add(a, /, b):
#     print(a + b)
#
#
# add(1, 2)
# add(1, b=3)
# add(a=1, b=3)       # TypeError
#
# ############################################################################
# # keyword only arguments(*) - parameters after "*" must take only keyword arguments
#
# def add(*, a, b):
#      print(a + b)
#
#
# add(1, 2)           # TypeError
# add(a=1, b=2)
#
#
# def add(a, *, b):
#     print(a + b)
#
#
# add(1, b=2)
# add(a=1, b=2)
#
# #############################################################################
# # combination of positional-only and keyword-only arguments
#
# # always "/" should be followed by "*" as the syntax of function definition takes positional
# # arguments before keyword arguments
#
# def add(a, /, *, b, c):
#     print(a + b + c)
#
# add(1, b=2, c=3)

##########################################################################################

# def add(*args):
#     print(sum(args))
#
#
# add()
# add(1)
# add(1, 2)
# add(1, 2, 3)
# add(1, 2, 3, 4)
#
#
# def add(**kwargs):
#     print(kwargs)
#
#
# add()
#
# add(a=1, b=2)
#
#
# def add(*args, **kwargs):
#     print(args, kwargs)
#
# add(1, 2, c=3, d=4)
#
# add()

##################################################################################
# # packing
#
# def spam(*args):
#     print(args)
#
#
# spam(1, 2, 3)       # (1, 2, 3)
#
# # unpacking
# l = [10, 20, 30]
#
# def display(a, b, c):
#     print(a, b, c)
#
#
# display(*l)     # 10, 20, 30

#####################################################################################
# def greet(msg="good morning"):
#     print(msg)
#
#
# greet()             # good morning
# greet("hai")        # hai
# greet("hello")      # hello
#
#
# msg = "good evening"
# def greet(message=msg):
#     print(message)
#
#
# greet()                 # good evening
# msg = "good morning"
# greet()                 # good evening

#######################################################################################
# function to return length of an iterable without using len()

def len_(iterable):
    count = 0

    for _ in iterable:
        count += 1

    return count


# len_("hai")
# len_([10, 20, 30, 40])

####################################################################################
# check if a number is prime or not

def prime(num):     # 5
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return "number is not a prime number"
        return "number is prime"
    else:
        return "number should be a positive number"


# prime(5)
###################################################################################
# prime number series

def prime_series(start: int, end: int):
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")


# prime_series(1, 10)

#######################################################

def arguments_count(*args, **kwargs):
    print("positional args:", len(args))
    print("keyword args:", len(kwargs))


# arguments_count(1, 2, 3, 4, a=10, b=20)

def display(msg="hello everyone"):
    print(msg)


# display()
# display("hai")


def check_args(*args, **kwargs):
    if len(args) + len(kwargs) >= 5:
        print("There are >= 5 arguments")
    else:
        print("There are < 5 arguments")


# check_args(1, 2, a=10, b=20)
# check_args(1, 2, 3, a=10, b=20)

#################################################################
# function to return last digit of a number

def last_digit(num):
    return num % 10


print(last_digit(147))

"""
Write a function to print the below output.

# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX
"""

































































