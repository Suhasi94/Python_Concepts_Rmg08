# sorting iterables

s = "hello"
print(sorted(s))        # ascending order
print(sorted(s, reverse=True))      # descending order
print()

l = [10, 6, 2, 8, 4, 9]
print(sorted(l))            # ascending order
print(sorted(l, reverse=True))      # descending order
print()

t = (10, 6, 2, 8, 4, 9)
print(sorted(t))            # ascending order
print(sorted(t, reverse=True))      # descending order
print()

set_ = {10, 6, 2, 8, 4, 9}
print(sorted(set_))            # ascending order
print(sorted(set_, reverse=True))      # descending order
print()

d = {"b": 1, "c": 2, "a": 3}
print(sorted(d))
print(sorted(d, reverse=True))
print()
############################################################################
# custom sorting

names = ["steve", "eve", "adani", "bob", "birla", "ambani"]
res = sorted(names)
print(res)

# sorting based on length
res = sorted(names, key=len)
print(res)

# sorting based on last character
def last_char(string):
    return string[-1]


print(sorted(names, key=last_char))

print(sorted(names, key=lambda string: string[-1]))
print()
######################################################################################
# custom sorting on dictionaries

d = {"walmart": 7, "gmail": 5, "google": 6, "flipkart": 8}

# sorting based on keys
print(sorted(d))            # ['flipkart', 'gmail', 'google', 'walmart']
print(sorted(d.items()))    # [('flipkart', 8), ('gmail', 5), ('google', 6), ('walmart', 7)]
print()

# sorting based on length of keys
print(sorted(d, key=len))


def len_keys(item):     # item --> (key, value)
    return len(item[0])


print(sorted(d.items(), key=len_keys))
print(sorted(d.items(), key=lambda item: len(item[0])))
print()

# last character of key

d = {"walmart": 7, "gmail": 5, "google": 6, "flipkart": 8}
print(sorted(d.items(), key=lambda item: item[0][-1]))


#################################################################################
d = {"apple": 10, "google": 7, "yahoo": 2, "rediff": 3}

# sort based on values
print(sorted(d.items(), key=lambda item: item[-1]))

#########################################################################################

# anagrams

string1 = "fare"
string2 = "fear"

# if sorted(string1) == sorted(string2):
#     print("strings are anagrams")
# else:
#     print("not anagrams")

#########################################################################################
items = ["eat", "ate", "listen", "silent", "stressed", "tea", "desserts", "hai", "hello"]

d = {}

for item in items:
    # sorted_value = tuple(sorted(item))        # (a, e, t)
    sorted_value = "".join(sorted(item))
    if sorted_value not in d:
        d[sorted_value] = [item]            # {(a, e, t): [eat]}
    else:
        d[sorted_value].append(item)        # {(a, e, t): [eat, ate]}


# print(d)





























