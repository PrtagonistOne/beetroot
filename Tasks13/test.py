def add_five(x):
    return x + 5

def do_twice(f):
    def resulting(x):
        print(x)
        return f(x)
    return resulting

result = do_twice(add_five)
print(result(5))
from functools import reduce

string = ''
print(list(filter(None, string)))
print(list(zip('1234', [0.1, 0.2, 0.3, 0.4], [5, 6, 7, 8, 9])))
help(map)
help(reduce)