def with_index(iterable, start=0):
    n = start
    for value in iterable:
        yield n, value
        n += 1


nums = [i for i in range(0, 20, 2)]
print(nums)
print(list(with_index(nums)))
