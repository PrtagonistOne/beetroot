from typing import Union
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 1
    elif exp < 0:
        raise ValueError('This function works only with exp > 0.')
    return x * to_power(x, exp-1)


print(to_power(2, 3) == 8)
