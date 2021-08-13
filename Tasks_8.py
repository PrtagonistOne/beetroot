# Task 1
def oops():
    raise KeyError()


def high_func():
    try:
        oops()
    except KeyError:
        print('Gotcha thief!')


'''
def high_func():
    try:
        oops()
    except IndexError:
        print('Gotcha thief!')
'''

high_func()


# Task 2
def simple_calc(a, b) -> float:
    try:
        c = a**2 / b
    except ZeroDivisionError:
        print('Can\'t divide by zero! The second number must not be 0')
    except TypeError:
        print('Please be sure that both arguments on input are numbers!')
    else:
        print(f'All good - the answer is {c}')
        return c


simple_calc(5, 25)
