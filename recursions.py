# for _ in range(3):
#     print("hello")

i = 0
def repeat():
    global i
    if i == 3:
        return
    print("hello")
    i += 1
    repeat()


# repeat()

def repeat_n_times(n):
    if n == 0:
        return

    print("hello")
    repeat_n_times(n-1)     # 2, 1, 0


# repeat_n_times(3)

##########################################################################################
# count down : 10 - 1

def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)

# count_down(10)

#######################################################################################
# counting from 1 - 10

i = 1
def count_(n):
    global i

    if i > n:
        return

    print(i)
    i += 1
    count_(n)

# count_(5)


def count_n(n):
    if n == 0:
        return

    count_n(n-1)
    print(n)


# count_n(3)

########################################################################################
# count the number of digits

num = 9845
count = 0

while num > 0:
    num = num // 10     # 9845, 984, 98, 9, 0
    count += 1          # 1, 2, 3, 4

# print(count)


def count_digits(num, count=0):

    if num <= 0:
        return count

    num = num // 10
    count += 1
    return count_digits(num, count)


print(count_digits(9845))



def no_of_digits(number):       # 9845

    if number == 0:
        return 0

    return 1 + no_of_digits(number // 10)  # 984, 98, 9, 0

# print(no_of_digits(9845))


























