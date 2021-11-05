# Task 1
import datetime

name = "sashko"
day = datetime.datetime.today().strftime('%d.%m.%Y')
finalString = f'Good day {name.title()}! {day} is a perfect day to learn python'
print(finalString)
# Task 2
firstName = 'oleksandr'
lastName = 'kopiievyi'

message = f'Greeting everyone, I am\
 {firstName.title()}' + ' ' + f'{lastName.title()}'

print(message)
# Task 3
a = 5
b = 2
print(f'a = {a}, b = {b}')
print('Додавання a + b =', a + b)  # Addition
print('Віднімання a - b =', a - b)  # Subtraction
print('Ділення a / b =', a / b)  # Division
print('Множення a * b =', a * b)  # Multiplication
print('Підведення до степеня b числа a =', pow(a, b))  # Exponent (Power)
print('Ділення остачею числа a на b =', a % b)  # Modulus
print('Ділення з відкиданням остачі a на b =', a // b)  # Floor division
