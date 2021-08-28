class MyIterable:
    pointer = -1

    def __init__(self, some_string):
        self.some_string = some_string

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.some_string) == self.pointer:
            raise StopIteration
        else:
            self.pointer += 1
            return self.some_string[self.pointer]


nums = MyIterable('0123456789')

iter_nums = iter(nums)
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
