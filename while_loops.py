# printing numbers from 1 to 5
"""
num = 1

while (num <= 5):
    print(num)
    num = num + 1

######################################################################
# 5 to 1
num = 5

while num >= 1:
    print(num)
    num -= 1

########################################################################
# even numbers till 20

num = 0

while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1

print()

num = 0
while num <= 20:
    print(num, end=" ")
    num += 2


###################################################################
# odd numbers till 20

num = 1

while num <= 20:
    print(num, end=" ")
    num += 2

print()

num = 0

while num <= 20:
    if num % 2 != 0:
        print(num, end=" ")
    num += 1


#####################################################################################
# traversing through the string

string = "hello world"

i = 0

while i < len(string):
    print(string[i])
    i += 1

####################################################################################
# printing alternate characters in a string

string = "hello world"
i = 0

while i < len(string):
    print(string[i], end=" ")
    i += 2

#####################################################################################
# printing the characters in reversed order

string = "hello world"

i = len(string) - 1

while i >= 0:
    print(string[i], end="")
    i -= 1
"""
#####################################################################################
# printing the vowels from a string

string = "hello world"

i = 0

while i < len(string):
    if string[i] in "aeiouAEIOU":
        print(string[i], end=" ")
    i += 1













































