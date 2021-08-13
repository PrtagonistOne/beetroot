# Task 1
def simple_function_hello(name: str) -> str:
    print(f'My favorite movie is named {name}')


simple_function_hello('Hardcore')


# Task 2
def make_county(country_name: str, capital: str) -> dict:
    county = {country_name: capital}
    print('\n', county.items())


make_county('Bolivia', 'La Paz')


# Task 3
def make_operation(operation_type: str, *args):
    multiplying_value = 1
    non_multiply_value = args[0]  # take the first value of args as the setting point for the difference(-)operation
    if operation_type == '*':
        for i in range(len(args)):
            multiplying_value *= args[i]
    elif operation_type == '+':
        non_multiply_value = sum(args)
    elif operation_type == '-':
        non_multiply_value -= sum(args[1:])
    else:
        print('Operand type not supported')

    if multiplying_value != 1:
        return multiplying_value
    elif non_multiply_value != 0:
        return non_multiply_value


print('\n', make_operation('-', 5, 5, -10, -20))
print(make_operation('+', 7, 7, 2))
print(make_operation('*', 7, 6))
