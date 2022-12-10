# local scope variables

def display():
    count = 0
    count += 1
    print(count)


# display()
# print(count)

# global variables

a = 10

# using global variable inside local space
def add():
    print(a)


# add()

# re initialize global variable inside local space
b = 100

def add1():
    b = 20
    print(b)


# add1()
# print(b)


###################################################################
# update global variable inside local space
b = 100

def add2():
    b += 20     # b = b + 20        # UnboundLocalError
    print(b)


# add2()
# print(b)


b = 100

def add2():
    global b
    b += 20     # b = b + 20        # UnboundLocalError
    print("inside function", b)


# print("outside function", b)
# add2()


###########################################################################
# using local variable inside nested function
def spam():
    a = 10

    def wrapper():
        print(a)

    wrapper()


# spam()

###############################################################################
# update local variable in nested function

def spam():
    a = 10

    def wrapper():
        a += 1              # UnboundLocalError
        print(a)

    wrapper()


# spam()



def spam():
    a = 10

    def wrapper():
        nonlocal a
        a += 1

    wrapper()

# spam()

############################################################################
def add():
    global x
    x = 5


add()
print(x)


































