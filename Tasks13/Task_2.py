def add_number_nine(x):
    return x + 9


def outside_func(f):
    def inside_func(x):
        return f(x)
    return inside_func


result = outside_func(add_number_nine)
print(result(1))
