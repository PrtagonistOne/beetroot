from functools import wraps


def logger(func):
    @wraps(func)
    def logger_wrapper(*args, **kwargs):
        return f"{func.__name__} called with {str(args)[1:-1]} {str(kwargs)[1:-1]}"
    return logger_wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(5, 5))
print(square_all([1, 2, 3, 4]))

