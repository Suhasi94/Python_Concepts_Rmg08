# # indices of the given elements
#
# names = ["apple", "google", "apple", "yahoo", "yahoo"]
# d = {}
#
# for index, name in enumerate(names):
#     if name not in d:
#         d[name] = [index]
#     else:
#         d[name].append(index)
#
# # print(d)
#
# ##################################################
# d = {"a": "hello", "b": 100, "c": 10.1, "d": "world"}
#
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#     else:
#         d[key] = value
#
# # print(d)
# #################################################################
# names = ["apple", "google", "apple", "yahoo", "yahoo"]
#
# # [("apple", 2), ("google", 1), ("yahoo", 2)]
# d = {}
#
# for name in names:
#     if name not in d:
#         d[name] = 1
#     else:
#         d[name] += 1
#
# # print(d)
#
# l = []
#
# for name in set(names):
#     l.append((name, names.count(name)))
#
# # print(l)
#
# #################################################################################
# list_ = ["food@table", "lily@flower", "human@walk", "being@work", "human@talk"]
# d = {}
#
# for item in list_:
#     key, value = item.split("@")         # ["food", "table"]
#     if key not in d:
#         d[key] = [value]
#     else:
#         d[key] += [value]
#
# # print(d)
#
# list_ = ["food@table", "lily@flower", "human@walk", "being@work"]
#
# d = {item.split("@")[0]: item.split("@")[1] for item in list_}
# # print(d)
#
# #######################################################################
# s = [(4, 56, 78), ("one", "two", "three")]
#
# values, keys = s            # values - (4, 56, 78),         keys - ("one", "two", "three")
# d = {}
#
# for index, item in enumerate(keys):     # index, 0      item - "one"
#     d[item] = values[index]             # values[0] - 4     , {"one": 4, "two": 56}
# print(d)
#
# values, keys = s
# d = {item: values[index] for index, item in enumerate(keys)}
# print(d)
#
#
# # zip()
#
# s = [(4, 56, 78), ("one", "two", "three")]
# values, keys = s
#
# # print(dict(zip(keys, values)))
#
# ###################################################################################
# nums = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]
#
# max_num = max(nums)     # 4
#
# for num in nums:
#     if num == max_num:
#         print(num)
#
# ###################################################################################
# def is_prime(num):      # 4 --> 5
#     while True:
#         if num > 1:
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#             else:
#                 print(f"{num} is a prime number")
#                 break
#             num += 1
#
#
# # is_prime(18)
#
# #############################################################################
# names = ["instagram", "google", "apple", "yahoo", "walmart", "gmail"]
#
# l = [name for name in names if len(name) >= 6]
# # print(l)
#
# ##############################################################################
# s = "she is a very good actor and she knows to sing too"
# words = s.split()
#
# d = {}
# for word in words:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]] += [word]
#
# # print(d)
#
# ###############################################################################
# items = ["apple", 1.2, "google", 12.6, 26, "100"]
# n = 3
#
# for _ in range(n):
#     value = items.pop()
#     items.insert(0, value)
#
# # print(items)

###############################################################
# d = {"k1": "v1", "k2": {"nk1": "v2", "nk2": {"nk3": "v3"}}}
# value = []


# def create_list(iterable):
#     keys = []
#
#     for k, v in iterable.items():
#         if isinstance(v, dict):
#             keys.append(k)
#             value.append(v)
#         else:
#             value.append((k, v))
#     return keys
#
# i = 0
# while i < len(d):
#     keys_list = list(d.keys())
#     if isinstance(d[keys_list[i]], dict):
#         keys = create_list(d[keys_list[i]])
#     else:
#         value.append((keys_list[i], d[keys_list[i]]))
#     i += 1


# dict_ = {"k1": "v1", "k2": {"nk1": "v2", "nk2": {"nk3": "v3"}}}
# i = 0
# def func(d, res=[], k=""):
#     global i
#     for key, value in d.items():
#         if isinstance(value, dict):
#             return func(value, res=res, k=k+key)
#         else:
#             res.append((k + key, value))
#     i += 1
#     if i == len(d):
#         return res
#
# print(func(dict_))

















































