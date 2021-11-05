def some_func():
    a = 1
    b = 2
    return a + b

print(some_func.__code__.co_nlocals)
