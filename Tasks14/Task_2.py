from functools import wraps


def stop_words_log(words: list):
    def stop_words_dec(func):
        @wraps(func)
        def stop_words_wrapper(*args, **kwargs):
            user_string = ''.join(func(str(args)[2:-3]))  # cut off brackets and commas and marks below
            for word in words:
                user_string = user_string.replace(word, '*')
            return user_string
        return stop_words_wrapper
    return stop_words_dec


@stop_words_log(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
