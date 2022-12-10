# string = "hello"        # ohell, lohel
# n = 2
# l = list(string)        # [h, e, l, l, o]
#
# for ele in range(n):
#     value = l.pop()     # o
#     l.insert(0, value)
#
# # print("".join(l))
#
# ########################################################################################
# # 0, 1, 1, 2, 3, 5, 8, 13....
#
# n1 = 0
# n2 = 1
# n_value = 4
#
# for i in range(n_value-1):
#     next_ = n1 + n2
#     n1 = n2
#     n2 = next_

# print(n1)

#########################################################################################
# nth prime number

# n = 7
# num = 0
# prime_count = 0
#
# while prime_count < n:
#     if num > 1:
#         for i in range(2, num//2):
#             if num % i == 0:
#                 break
#
#         else:
#             prime_count += 1
#             if prime_count == n:
#                 print(num)
#     num += 1

############################################################################################
# longest non-repetitive substring

# sentence = "This is a programming language and programming is fun"
# words = sentence.split()
# d = {}
#
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
#
# print(d)
#
# longest_word = ""
# for key, value in d.items():
#     if value == 1:
#         if len(longest_word) < len(key):
#             longest_word = key
# print(longest_word)

#######################################################################################
# sentence = "this is a programming language and programming is fun"
# words = sentence.split()
# list_ = [word for word in words if words.count(word) == 1]
# print(list_)
#
# # without using inbuilt methods
# longest_word = ""
# for word in list_:
#     if len(longest_word) < len(word):
#         longest_word = word

# print(longest_word)

# max()

# print(max([word for word in words if words.count(word) == 1], key=len))
# print(max(list_, key=len))

########################################################################################
nums = [19, 29, 5, 20, 67, 12, 45]

# sort()
# nums.sort()
# print(nums)

for _ in range(len(nums)-1):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
# print(nums)

##########################################################################################
sentence = "this is a programming language and programming is fun"
words = sentence.split()

for n in range(len(words)-1):
    for i in range(len(words)-1):
        if len(words[i]) < len(words[i+1]):
            words[i], words[i+1] = words[i+1], words[i]

print(words)








































































