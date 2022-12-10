s = 'hello'

s1 = "hello world"

s2 = """good morning"""

s3 = '''welcome'''

s4 = 'he said "hai everyone"'

s5 = """
hi
everyone
good morning!!!!
"""

#
# word = str("hello")
# print(word)
#
# # empty string
# s6 = ""
# print(s6)
#
# s7 = str()
# print(s7)
#
# # length of string
# print("The length of string s is:", len(s))

# raw strings

# string = r"pytho\n sele\nium"
# print(string)

# name = input("enter a name:")
#
# string = f"my name is {name}"
# print(string)


#########################################################################

# string methods

string = "Hello WorlD"

# print(dir(string))

# lower_case = string.lower()
# print(lower_case)
# print(string)
#
# print()
# upper_case = string.upper()
# print(upper_case)
# print()
#
# swap = string.swapcase()
# print(swap)
#
# #######################################################################
# # count()
#
# count_ = string.count("l")
# print(count_)       # 3
#
# count_ = string.count("l", 4, 9)
# print(count_)       # 0
#
# sentence = "Today is a special day"
# print(sentence.count("day"))        # 2

######################################################################
# find()

# string = "hello world"
#
# print(string.find("e"))
# print(string.find("l"))
# print(string.find("l", 3, 10))
#
# print(string.rfind("l"))
# print(string.rfind("o", 4, 8))
#
# print(string.find("x"))
# print(string.rfind("x"))

##########################################################################
# # index()
#
# string = "hello world"
#
# print(string.index("o"))
# print(string.index("o", 5, 25))
#
# # print(string.index("m"))
#
# print(string.rindex("o"))
# print(string.rindex("j"))


################################################################################
# # replace()
# s = "hello world"
# print(s.replace("world", "universe"))
# print(s)
#
#
# print(s.replace("o", "a"))
#
# print(s.replace("o", "a", 1))
# print(s.replace("z", "a"))


####################################################################################
# s = "hello world"
#
# print(s.startswith("ello"))
# print(s.startswith("lo", 3))
#
# print(s.endswith("ld"))
# print(s.endswith("o"))

###############################################################################
sentence = "python is a programming language"

# print(sentence.split(" "))
# print(sentence.split("o"))

# print(sentence.split(" ", 1))

# print(sentence.split())
# print(sentence.rsplit())
#
# print(sentence.split(" ", 2))
# print(sentence.rsplit(" ", 2))
#
# print(sentence.split("j"))

################################################################################
# word = "hai"
#
# print(",".join(word))
#
# print("hello".join(word))
#
#
# sentence = "python is a programming language"
#
# output = sentence.split()
# print(output)
#
# print("".join(output))
# print(" ".join(output))
# print("#".join(output))

####################################################################################
s = "@@@@@@@hello#########"

print(s.strip("@"))
print(s.strip("#"))
print(s.strip("#@"))

s1 = "*@!#*$hai^%$*"
print(s1.strip("@!#$^%$*"))
print(s1.strip("$"))
print(s1.strip("*"))

s1 = "**$*hai*!$*"
print(s1.lstrip("*"))
print(s1.rstrip("*"))

s2 = "     hello world     "
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())


##########################################################################
s = "hello123"

print(s.isalnum())
print("hello".isalnum())
print("#$%".isalnum())
print("hello world".isalnum())

print()
print(s.isalpha())
print("abc".isalpha())

print()









































































