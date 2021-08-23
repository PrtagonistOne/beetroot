from functools import wraps

def arg_rules_dec(type_: type, max_length: int, contains: list):
    def arg_rules_log(func):
        @wraps(func)
        def arg_rules_wrapper(*args, **kwargs):
            pass


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'