# even or odd
"""
num = int(input())

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# inline if - else statement
print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd")
print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")

###################################################################################
# palindrome

s = "hello"

if s == s[::-1]:
    print(f"{s} is a palindrome")

if s == s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

#################################################################################
# check if the number is a palindrome or not
num = 1221
str_num = str(num)

if str_num == str_num[::-1]:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

##################################################################################
# check if a character is an alphabet or digit or a special character
char = "a"

if char.isalpha():
    print("char is an alphabet")
elif char.isdigit():
    print("char is a number")
else:
    print("char is a special character")

##################################################################################
# check if the character is a vowel or not
char = "h"

if char in "aeiouAEIOU":
    print("char is a vowel")
else:
    print("char is a consonent")

##################################################################################
# check if the character is an alphabet or not without using inbuilt methods
char = "L"

if (ord("a") <= ord(char) <= ord("z")) or (ord("A") <= ord(char) <= ord("Z")):
    print("char is an alphabet")
else:
    print("char is not an alphabet")


##################################################################################
# check if the given string starts with a vowel or not

s = "hello"

if s[0] in "aeiouAEIOU":
    print("the string starts with vowel")
else:
    print("the string does not starts with vowel")


##################################################################################
# convert lower case to upper case and vice-versa

char = "d"

if ord("a") <= ord(char) <= ord("z"):
    print(chr(ord(char) - 32))

elif ord("A") <= ord(char) <= ord("Z"):
    print(chr(ord(char) + 32))

else:
    print("Character is not an alphabet")

############################################################################
# check if the iterable is empty or not
iterable = [1, 2, 3]

if iterable:        # bool(iterable)
    print("iterable is not empty")
else:
    print("iterable is empty")

###########################################################################
# check if the iterable has even number of elements
iterable = {1, 2, 3, 4, 5}

if len(iterable) % 2 == 0:
    print("iterable has even number of elements")

###########################################################################
# check if the iterable is a sequence and reverse it if it is a sequence or else keep it as is
iterable = {1, 2, 3}

if isinstance(iterable, (str, list, tuple)):
    print(iterable[::-1])
else:
    print(iterable)

##############################################################################
#check the number of keys in the dictionary, if the number is odd print the dictionary
# as it is, else add a new key to make it odd and print it

d = {"a": 1, "b": 2}

if len(d) % 2 == 0:
    d["c"] = 3
    print(d)
else:
    print(d)

#################################################################################
# largest of 3 numbers
a = 10
b = 15
c = 8

if a > b and a > c:
    print("a is greater")

elif b > a and b > c:
    print("b is greater")

else:
    print("c is greater")

###################################################################################
# check if the first digit of the given number is even or odd

num = 123
str_num = str(num)

if int(str_num[0]) % 2 == 0:
    print("the digit is even")
else:
    print("the digit is odd")
"""
##################################################################################

num = 8

sqrt_ = num ** 0.5

if sqrt_ ** 2 == num:
    print("perfect square")
else:
    print("not a perfect sqaure")

####################################################################
import calendar

print(calendar.isleap(2020))
print(calendar.isleap(2021))











