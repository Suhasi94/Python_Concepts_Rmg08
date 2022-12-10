import time


def delay(func):
    def wrapper(*args, **kwargs):
        time.sleep(3)
        func(*args, **kwargs)

    return wrapper


@delay          #  -->  display = delay(display)
def display():
    print("hai")

# display()

###################################################################################

# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(3)
#         func(*args, **kwargs)
#
#     return wrapper


class Demo:

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            time.sleep(3)
            func(*args, **kwargs)
        return wrapper

#
# d1 = Demo()

# @Demo()               # display = Demo()(display)       --> func --> display, display --> wrapper
# def display():
#     print("hai")

# display()

#########################################################################################
class Demo:

    def __init__(self, a):
        self.a = a

    def __call__(self, *args, **kwargs):
        print("in call method")


# d1 = Demo(10)
# d1()            # objects are not callable
# print(dir(d1))

######################################################################################

# log "hello world" message

class Log:

    def __call__(self):
        print("hello world")


# l = Log()
# l()

class Log:

    def __call__(self, name):
        print(f"hello {name}")


# l = Log()
# l("Ram")

class EvenOdd:

    def __call__(self, num):
        return num % 2 == 0


# e = EvenOdd()
# print(e(2))


class Palindrome:

    def __call__(self, string):
        return string == string[::-1]


# print(Palindrome()("hai"))


class Anagrams:

    def __call__(self, s1, s2):
        return sorted(s1) == sorted(s2)


# print(Anagrams()("fear", "fare"))

##############################################################################

class Log:

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("hello everyone")
            return func(*args, **kwargs)

        return wrapper


@Log()
def add(a, b):
    return a + b


# print(add(1, 2))

################################################################################

class Delay:

    def __init__(self, time_):
        self.time_ = time_

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            time.sleep(self.time_)
            func(*args, **kwargs)
        return wrapper


@Delay(3)
def spam():
    print("hai")


spam()
