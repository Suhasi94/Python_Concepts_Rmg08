from itertools import islice
from collections import deque, Counter

"""
1. open
2. read/write
3. close
"""

# text_files

# path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\sample.txt"

# open(path, mode)
"""
modes --> read(r), write(w), create(x)
"""

# opening a file for read operations
# file_obj = open(path, "r")

"""
read: 
1. read()       - entire file as a single string
2. readline()   - one line as a string at a time
3. readlines()  - a list of strings/ list of lines in the file
"""

# data = file_obj.read()      # string
# print(type(data))

# data = file_obj.readline()      # file_obj - iterator object
# print(data)
# data = file_obj.readline()
# print(data)
# data = file_obj.readline()
# print(data)
# data = file_obj.readline()
# print(data)
# data = file_obj.readline()
# print(data)

# data = file_obj.readlines()
# print(data)

# # traversing through iterator object
# for line in file_obj:
#     print(line)


# file_obj = open(path, "r")
# # next()
# print(next(file_obj))
# print(next(file_obj))
# print(next(file_obj))
# print(next(file_obj))
# print(next(file_obj))
# print(next(file_obj))       # StopIteration

################################################################################################
# number of characters in each line
# obj = open(path, "r")
# for line in obj:
#     print(line, len(line))

# # number words in each line
# obj = open(path, "r")
#
# for line in obj:        # line --> str
#     words = line.split()        # words --> list
#     print(line, len(words))

# # print first word in each line
# obj = open(path, "r")
#
# for line in obj:
#     if line.strip():    # checks if the line is empty or not
#         words = line.split()    # []
#         print(words[0])
#
#
# obj.close()

# context manager - with keyword

# with open(path, "r") as file:
#     for line in file:
#         if line.strip():  # checks if the line is empty or not
#             words = line.split()  # []
#             print(words[0])
#
#
# print(file.closed)

# read the time from sample.log

log_path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\sample.log"

with open(log_path) as log_file:
    time_count = {}
    for line in log_file:
        if line.strip():
            logs = line.split()     # list
            if logs[1] not in time_count:
                time_count[logs[1]] = 1
            else:
                time_count[logs[1]] += 1

print(time_count)

# counter()

with open(log_path) as file:
    time_list = []
    for line in file:
        if line.strip():
            logs = line.split()
            time_list.append(logs[1])

print(time_list)
print(Counter(time_list))

#################################################################################################
path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\sample3.txt"

# opening a file for write operations - without context manager
# file_obj = open(path, "w")

"""
1. write(string)      
2. writelines(list of strings)
"""

# with open(path, "a") as file:
#     file.write("hello world\n")
#     file.writelines(["hai\n", "hello\n", 'welcome\n'])


# opening a file in create mode
# file_obj = open(path, "x")

# with open(path, "x") as file:
#     print(file.write("hello world"))

####################################################################################
# r/w
# with open(path, "w+") as file:
#     file.write("hai")
#
#     file.seek(0)
#
#     for line in file:
#         print(line)

#####################################################################################
# 5th line

log_path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\sample.log"
expected_line_num = 5

# count variable

# with open(log_path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count == expected_line_num:
#             print(line)
#             break
#
# # enumerate()
#
# with open(log_path) as file:
#
#     for line_no, line in enumerate(file, start=1):
#         if line_no == expected_line_num:
#             print(line)
#             break
#
# # islice()
#
# line_num = 5
# with open(log_path) as file:
#     lines = islice(file, line_num-1, line_num)
#     print(list(lines))
#
# ##########################################################################
#
# # first 3 lines
#
# # islice()
#
# with open(log_path) as file:
#     lines = islice(file, 3)
#     print(list(lines))
#
# #########################################################################
#
# # last 3 lines
# path = r"C:\Users\Vidyashree M C\PycharmProjects\pythonProject1\files\sample1.txt"
#
# with open(path) as file:
#     file_length = 0
#
#     for line in file:
#         file_length += 1
#
#     file.seek(0)
#
#     lines = islice(file, file_length-3, file_length)
#     print(list(lines))
#
#
# # deque()
#
# with open(path) as file:
#     lines = deque(file, 3)
#     print(list(lines))

########################################################################################

s = "hello world"
#
# obj = Counter(s)
# print(obj)      # counter object (dictionary)
# print(obj.most_common())    # list of tuples
# print(obj.most_common(1))

















