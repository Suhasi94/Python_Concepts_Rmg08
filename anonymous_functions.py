def last_element(sequence):
    return sequence[-1]


# print(last_element)
# print(last_element("hello"))
# print(last_element())


# lambda args: return_value
res = lambda sequence: sequence[-1]
print(res)
print(res("hello"))
res("hello")

#####################################################################################
# sum of 2 numbers

sum_ = lambda n1, n2: n1 + n2
print(sum_(1, 2))

######################################################################################
# square and cube the given number

def square_cube(num):
    return num ** 2, num ** 3


# print(square_cube(3))

# lambda expression

sq_cube = lambda num: (num ** 2, num ** 3)
print(sq_cube(3))

#######################################################################
# Program to check if the number is even or odd

even_odd = lambda num: "num is even" if num % 2 == 0 else "num is odd"
print(even_odd(5))

########################################################################
# Program to check if the string is palindrome or not

palindrome = lambda string: string == string[::-1]
print(palindrome("mom"))


palindrome = lambda string: f"{string} is palindrome" if string == string[::-1] else f"{string} is not a palindrome"
res = palindrome("dad")
print(res)

###########################################################################
# return first element of a sequence

first_element =  lambda seq: seq[0]
# print(first_element([1, 2, 3]))

############################################################################
# return length of any iterable

length = lambda iterable: len(iterable)
# print(length("hai"))

###############################################################################
# convert the number given to positive number

positive = lambda num: abs(num)
# print(positive(-4))

###############################################################################
# return keys of the dictionary

d = {"apple": 5, "google": 6, "flipkart": 8}

keys_ = lambda dictionary: dictionary.keys()
# print(keys_(d))


keys_ = lambda dict_: [key for key in dict_]
# print(keys_(d))

##############################################################################
# return values from a dictionary

d = {"apple": 5, "google": 6, "flipkart": 8}

values_ = lambda dict_: dict_.values()
# print(values_(d))

values_ = lambda dict_: [dict_[key] for key in dict_]
# print(values_(d))

##############################################################################################
# squares of numbers inside a list

numbers = [1, 2, 3, 4, 5]

# using list comprehenison
squares = lambda iterable: [num ** 2 for num in iterable]
# print(squares(numbers))

# using for loop
squares = lambda num: num ** 2

l = []
for num in numbers:
    res = squares(num)
    l.append(res)

# print(l)

# using map() class
numbers = (1, 2, 3, 4, 5)

op = map(squares, numbers)          # returns an object
# print(list(op))

#######################################################################################
l = ["nayana", "kayak", "mom", "school", "bag", "dad"]


palindrome_ = lambda string: string == string[::-1]
# print(list(map(palindrome_, l)))

def palindrome_(string):
    return string == string[::-1]

# print(list(map(palindrome_, l)))

#######################################################################################
l = ["nayana", "kayak", "mom", "school", "bag", "dad"]

first_char = lambda string: string[0]
# print(list(map(first_char, l)))

#########################################################################################
nums = [1, 2, -4, 1, -7, -45, 10]

positive = lambda num: abs(num)
# print(list(map(positive, nums)))
#
# print(list(map(abs, nums)))

########################################################################################
names = ["steve", "ram", "tata", "shyam"]

res = lambda item: (item, len(item))

def tuple_(item):
    return item, len(item)

# print(list(map(tuple_, names)))
##############################################################
l1 = [1, 2, 3, 4]
l2 = [9, 3, 6]

def add(a, b):
    return a + b


# print(list(map(add, l1, l2)))

######################################################################
nums = [10, 2, 3, 7, 9]

def exponent(number, index):
    return number ** index


# indices = list(range(0, len(nums)))
# print(list(map(exponent, nums, range(0, len(nums)))))

########################################################################################
# even numbers
l = [1, 2, 3, 4, 5, 6]

# using map and lambda
evens = lambda num: num % 2 == 0
# print(list(map(evens, l)))      # [False, True, False, True, False, True,]

# using function and map()
def even(num):
    if num % 2 == 0:
        return num

# print(list(map(even, l)))   # [None, 2, None, 4, None, 6]


# using filter()
def even(num):
    if num % 2 == 0:
        return num

# print(list(filter(even, l)))        # [2, 4, 6]

# using filter and lambda

evens = lambda number: number % 2 == 0
# print(list(filter(evens, l)))       # [2, 4, 6]

###########################################################################3
# even length
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

even_length = lambda string: len(string) % 2 == 0

res = list(filter(even_length, names))
# print(res)

########################################################################################
# words starting with vowels
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

vowels = lambda string: string[0] in "aeiouAEIOU"
# print(list(filter(vowels, names)))

##################################################################################
numbers = [1, -8, -5, 6, 2, 0]

positive = lambda num: num > 0
# print(list(filter(positive, numbers)))

#####################################################################################
# prime numbers from 1 to 20

def prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break

        else:
            return "number is prime"


print(list(filter(prime, range(1, 20))))












































