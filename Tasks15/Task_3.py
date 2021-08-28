from functools import wraps


class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def to_int_wrapper(value):
            return int(value)

        return to_int_wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def to_str_wrapper(value):
            return str(value)

        return to_str_wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def to_bool_wrapper(value):
            return bool(value)

        return to_bool_wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def to_float_wrapper(value):
            return float(value)

        return to_float_wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
