# create a list of squares from the given list numbers
"""
l = [1, 2, 3, 4, 5]

# op = [1, 4, 9, 16, 25]

res = []

for item in l:
    res.append(item ** 2)
print(res)

# comprehension
# [(value to be appended) for loop]
res1 = [item ** 2 for item in l]

###################################################################

# program to create a list of lengths of the words in the given list

names = ["steve", "john", "bob", "alex"]

# normal method
lengths = []

for name in names:
    lengths.append((name, len(name)))
print(lengths)


# comprehension

length_ = [(name, len(name)) for name in names]
print(length_)

#########################################################################
# index and character pair
string = "hello"

# normal method
res = []

for item in enumerate(string):
    res.append(item)

print(res)

# comprehension
res = [item for item in enumerate(string)]
print(res)

######################################################################################
# list of even numbers from 1 to 50

# normal method
evens = []

for num in range(1, 51):
    if num % 2 == 0:
        evens.append(num)

print(evens)

# comprehension

evens = [num for num in range(1, 51) if num % 2 == 0]

print(evens)

##############################################################################
# list of names starting with vowels

names = ['laura', 'steve', 'bill', 'james', 'bob', 'greg', 'scott', 'alex', 'ive']

# normal method
vowels = []

for name in names:
    if name[0].lower() in "aeiou":
        vowels.append(name)

print(vowels)

# comprehension

vow = [name for name in names if name[0].lower() in "aeiou"]
print(vow)

"""
"""
1. list of languages starting with "p"
    languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']

2. list of names starting with consonants
    names = ['laura', 'steve', 'bill', 'james', 'bob', 'greg', 'scott', 'alex', 'ive']
    
3. list of names which are less than 6 characters
    names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']

4. Build a list with only even length string
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

############################################################################################################
# Reverse the item of a list if the item is of odd length string else keep it as it is

names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

# normal method

list_ = []

for name in names:
    if len(name) % 2 != 0:          # bool(len(name) % 2)
        list_.append(name[::-1])
    else:
        list_.append(name)
print(list_)

# comprehension

l = [name[::-1] if len(name) % 2 != 0 else name for name in names]
print(l)
"""
##########################################################################################
"""
elements = ["alex", 12, "13.1", 19.5, "90", [1, 2, 3]]

# normal method

res = []

for ele in elements:
    if isinstance(ele, int):
        value = str(ele)[::-1]
        res.append(int(value))      # int(str(ele)[::-1])
    else:
        res.append(ele)

print(res)

# comprehension

res = [int(str(ele)[::-1]) if isinstance(ele, int) else ele for ele in elements]
print(res)


###########################################################################################
# # check if the given number is prime or not
#
# num = 9
#
# for i in range(2, num):
#     if num % i == 0:
#         print("not a prime")
#         break
#
# else:
#     print("It is a prime")


#########################################################################
# series of prime numbers from 1 - 20

prime = []

for num in range(1, 21):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num, end=" ")
            prime.append(num)

print()
print(prime)

###############################################################################################
# dictionary comprehension - num and square pair

nums = [1, 2, 3, 4, 5]

# normal method
sq = {}

for num in nums:
    sq[num] = num ** 2

print(sq)

# comprehension

squares = {num: num ** 2 for num in nums}
print(squares)

####################################################################################################
# word and its length pair

sentence = "python is a programming language"

# normal method

word_len = {}
words = sentence.split()

for word in words:
    word_len[word] = len(word)

print(word_len)

# comprehension

word_len = {word: len(word) for word in sentence.split()}
print(word_len)

##########################################################################
# Flipping keys and values of the dictionary using dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}

# normal method
res = {}

for key in d:
    value = d[key]
    res[value] = key
print(res)

# d.items()
res = {}
for key, value in d.items():
    res[value] = key

print(res)

# comprehension

res_ = {d[key]: key for key in d}
print(res_)

res_ = {value: key for key, value in d.items()}
print(res_)


#############################################################################################
# character and its count pair

string = "hello world"

char_count = {}

for char in string:
    if string.count(char) > 1:
        char_count[char] = string.count(char)

print(char_count)

# comprehension

char_count = {char: string.count(char) for char in string if string.count(char) > 1}
print(char_count)

"""
######################################################################################
sentence = "python is a programming language"

ind_word = {}

for index, item in enumerate(sentence.split()):
    if index % 2 == 0:
        ind_word[index] = item[::-1]
    else:
        ind_word[index] = item

print(ind_word)

# comprehension

ind_word = {index: item[::-1] if index % 2 == 0 else item for index, item in enumerate(sentence.split())}
print(ind_word)

