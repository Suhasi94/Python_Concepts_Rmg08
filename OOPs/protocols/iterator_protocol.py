nums = [1, 2, 3, 4]         # iterable

nums_iterator = enumerate(nums)     # iterator obj

# for item in nums:
#     print(item)

# iterator protocol
iter_ = iter(nums_iterator)         # iter_ = nums_iterator.__iter__()
while True:
    try:
        num = next(iter_)           # num = nums_.__next__()

    except StopIteration as error_msg:
        break

    # else:
    #     print(num)

########################################################################################
# making a class as an iterable
class Sample:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)


s = Sample([1, 2, 3])

# for i in s:
#     print(i)

########################################################################################
# custom iterator class

class Spam:

    def __init__(self):
        self.start = 0

    def __iter__(self):
        return self              # returns an iterator object

    def __next__(self):
        if self.start > 5:
            raise StopIteration

        a = self.start
        self.start += 1
        return a


s = Spam()

for i in s:
    print(i)

# generator function

def range_5():
    start = 0
    for i in range(start, 6):
        yield i


r = range_5()

for item in r:
    print(item)










