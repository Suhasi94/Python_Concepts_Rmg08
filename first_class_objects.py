def spam():
    print("in spam")


spam()
print(spam)

# monkey patching
display = spam
print(display)
spam()
display()

########################################################################################
# return function's address from a function

def add(a, b):
    print(a + b)
    return add


res = add(1, 2)           # 3
print(res)          # address of add
print(add)          # address of add

##########################################################################
# passing function as an argument


def demo():
    print("in demo")


def sample(func):       # func --> demo
    print("in sample")
    print(func)         # address of demo
    func()              # in demo


sample(demo)
