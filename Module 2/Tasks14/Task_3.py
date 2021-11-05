from functools import wraps


def arg_rules_dec(type_: type, max_length: int, contains: list):
    def arg_rules_log(func):
        @wraps(func)
        def arg_rules_wrapper(name):
            user_string = func(name)
            if type_ != str:
                print('Please input string like value')
                return False
            elif len(name) > max_length:
                print(f'The maximum length should be {max_length} ')
                return False
            elif type_ == str and len(name) <= max_length:
                nice = []
                for symbol in contains:
                    if symbol in name:
                        nice.append(True)
                    else:
                        nice.append(False)
                if all(nice):
                    return user_string
                else:
                    print('Inputted string does not contain required symbols')
                    return False
        return arg_rules_wrapper
    return arg_rules_log


@arg_rules_dec(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False  # too long message should be printed

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
