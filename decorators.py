"""
1. nested function
2. outer functions should take only one argument, i.e, function's address
3. inner function should have the actual function call(func())
4. outer function must return inner function's address
"""

# decorator function
import functools


def display(func):          # func --> add
    def wrapper(*args, **kwargs):       # (1, 2, 3)
        print("The sum is: ")
        func(*args, **kwargs)       # add()
    return wrapper


# decorated function
def add(a, b, c):
    print(a + b + c)


add = display(add)          # add --> wrapper address, func --> add
# add(1, 2, 3)

# add(10, 20, 30)

##########################################################################
# print function's name before calling the main function

def name_function(func):
    def wrapper(*args, **kwargs):
        print("function name is:", func.__name__)
        func(*args, **kwargs)
    return wrapper


@name_function          # palindrome = name_function(palindrome)
def palindrome(string):
    print(string == string[::-1])

# decorated_func = decorator(decorated_func)
# palindrome("mom")


@name_function      # add = name_function(add)
def add(a, b, c):
    print(a + b + c)

# add(1, 2, 3)
#################################################################################
# decorator to log a msg

def log(func):
    def wrapper(*args, **kwargs):
        print("hello everyone")
        res = func(*args, **kwargs)     # return func(*args, **kwargs)
        return res

    return wrapper


@log            # add = log(add)        func --> add, add--> wrapper
def add(a, b):
    return a + b

# print(add(1, 2))

#####################################################################################
# name of the decorated function


def display_func_name(func):
    def wrapper(*args, **kwargs):
        print("The decorated function is:", func.__name__)
        res = func(*args, **kwargs)
        return res

    return wrapper


@display_func_name
def check_even(num):
    if num % 2 == 0:
        return "num is even"
    return "num is odd"

# print(check_even(6))
###############################################################################
# delay decorator
import time     #  sleep()

def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        func(*args, **kwargs)
    return wrapper


@delay
def demo():
    print("hello!!!!")


# demo()

###################################################################################
# execution time
import time


def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()      # time.time()
        res = func(*args, **kwargs)
        end = time.perf_counter_ns()        # time.time()
        return f"execution time {end-start}", f"result is: {res}"

    return wrapper


@execution_time
def difference(a, b):
    return a - b
# print(difference(10, 20))


#################################################################################
def delay_n_sec(n):
    def delay(func):
        def wrapper(*args, **kwargs):
            time.sleep(n)
            func(*args, **kwargs)
        return wrapper
    return delay


# delay = delay_n_sec(5)

# @delay      # display = delay(display)

@delay_n_sec(5)     # @delay     --> display = delay(display)
def display():
    print("hello world")


# display()

@delay_n_sec(3)
def spam():
    print("hi everyone")


# spam()

################################################################
def n_times(n):
    def multiple_times(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return multiple_times


@n_times(2)
def display():
    print("hello world")


display()


@n_times(3)
def spam():
    print("hi everyone")

# spam()


def delay(func):        # func --> wrapper_multiple
    def wrapper_delay(*args, **kwargs):
        print("in delay")
        func(*args, **kwargs)
    return wrapper_delay


def multiple_times(func):       # func --> spam
    def wrapper_multiple(*args, **kwargs):
        print("in multiple times")
        func(*args, **kwargs)
    return wrapper_multiple


@delay                  # spam = delay(multiple_times(spam))
@multiple_times
def spam():
    print("hi everyone")


# spam = multiple_times(spam)
# spam = delay(wrapper_multiple)
# spam = wrapper_delay

# spam()
















