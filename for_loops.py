# """
# for ref_var in range(1, 6):
#     print(ref_var)
#
# ####################################################
#
# for num in range(5, 0, -1):
#     print(num)
#
#
# #####################################################
# # traverse through a sequence
#
# string = "hello world"  # list, tuples
#
# for char in string:
#     print(char, end=" ")
#
# print()
#
# string = "hello world"
# for item in range(len(string)):
#     print(string[item], end=" ")
#
# ########################################################
# # traversing through a set
#
# s = {10, 20, 30, 40}
#
# for element in s:
#     print(element)
#
# ##########################################################
# # traversing through a dictionary
#
# d = {"a": 10, "b": 20, "c": 30}
#
# # traversing through keys
# for key in d:      # ["a", "b", "c"]
#     print(key)
#
# # # print values of the dictionary - d[key], d.get(key)
# for key in d:
#     print(d[key])
#
# ##############################################################
# # iterate over string in reversed direction
#
# string = "hello"
# res = ""
#
# # range()
# for item in range(len(string)-1, -1, -1):
#     # print(string[item], end=" ")
#     res += string[item]
# print(res)
#
# # slicing
# res = ""
# for char in string[::-1]:
#     res += char
# print(res)
#
# # reversed() class
# res = ""
# for char in reversed(string):
#     res += char
# print(res)
# """
#
# #######################################################################
# # index and character of string
#
# string = "hello world"
#
# # range()
# for index in range(len(string)):
#     print((index, string[index]), end=" ")
#
# print()
#
# # enumerate() --> (index, item)
# for item in enumerate(string):
#     print(item, end=" ")
#
# print()
#
# # printing only indices
# for item in enumerate(string):
#     print(item[0], end=" ")
#
# print()
#
# # printing only elements
# for item in enumerate(string):
#     print(item[1], end=" ")
#
# print()
#
# # unpacking the item(tuple) inside for loop
# for item in enumerate(string):          # item --> (0, "h")
#     print(item[0], item[1], end=", ",)
#
# print()
#
# # unpacking the item in the for loop definition and printing only index
# for index, element in enumerate(string):        # index, item = (0, "h")
#     print(index, end=" ")
#
# print()
#
# # unpacking the item in the for loop definition and printing only element
# for index, element in enumerate(string):
#     print(element, end=" ")
#

# # zip()
#
# l = [10, 20, 30]
# s = "hai"
#
# for item in zip(l, s):      # [(10, 'h'), (20, 'a'), (30, 'i')] --> item - (10, h)
#     print(item)
#
#
# for ele1, ele2 in zip(l, s):
#     print(ele1, ele2)

###########################################################################################


# traversing through dictionary

# d = {"a": 1, "b": 2, "c": 3}

# # printing only keys in a dictionary
#
# for key in d:
#     print(key, end=" ")
# print()
#
# for key in d.keys():
#     print(key, end=" ")
# print()
#
# for item in d.items():
#     print(item, end=" ")     # tuple
# print()
#
# for key, value in d.items():
#     print(key)


# # printing only values in a dictionary
#
# d = {"a": 1, "b": 2, "c": 3}
#
#
# for key in d:
#     print(d[key], end=" ")
# print()
#
# for value in d.values():
#     print(value, end=" ")
# print()
#
# for key, value in d.items():
#     print(value, end=" ")

#########################################################################################
# character and ascii value pair
#
# s = "hello"
# d = {}
#
# for char in s:
#     d[char] = ord(char)
#
# ##########################################################################################
# # word and length pair
#
# sentence = "python is a programming language"
# words = sentence.split()
#
# word_len = {}
#
# for word in words:
#     word_len[word] = len(word)
# # print(word_len)
#
# #####################################################################################
# # index and element pair
#
# sequence = "hello"
# index_ele = {}
#
# for index, char in enumerate(sequence):
#     index_ele[index] = char

# print(index_ele)

#######################################################################################
# word and its count pair

# sentence = "hai hello hai world hai good morning world hello hello"
# words = sentence.split()
# word_count = {}
#
# # using inbuilt method
# for word in set(words):
#     word_count[word] = words.count(word)         # hello
#
# print(word_count)

# # without using inbuilt method
# sentence = "hai hello hai world hai good morning world hello hello"
# words = sentence.split()
# word_count = {}
#
# for word in words:
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] = word_count[word] + 1

# using default_dict

from collections import defaultdict

# sentence = "hai hello hai world hai good morning world hello hello"
# words = sentence.split()
# word_count = defaultdict(int)
#
# for word in words:
#     word_count[word] = word_count[word] + 1
#
# print(word_count)


