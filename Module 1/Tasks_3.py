import msvcrt
# Task 1
expected_string = input("Please input string: ").replace(' ', '')

if len(expected_string) < 2:
    print("Empty String")
else:
    print(expected_string[:2] + expected_string[-2:])

# Task 2
msvcrt.getch()
flag = True
while flag:
    phone_number_string = input("\nPlease enter your phone number!\n1) The number must contain only digits\n"
                            "2) The number must be 10 digits long\nYour cellphone number: ").replace(' ', '')

    try:
        expected_phone_number = int(phone_number_string)
    except ValueError:
        print("The number must contain only digits.\n")
        msvcrt.getch()
        continue
    number_length = len(phone_number_string)
    if number_length < 10:
        print('The number is too short.\n')
        msvcrt.getch()
    elif number_length > 10:
        print('The number is too long.\n')
        msvcrt.getch()
    elif number_length == 10:
        print(f'Your number is {expected_phone_number}!')
        flag = False
# Task 3
msvcrt.getch()
stored_name = 'oleksandr'
flag = True
while flag:
    print('\nYour name is Oleksandr.')
    inputted_name = input('Please input the your name: ').lower()
    if inputted_name == stored_name:
        print("\nThe names matched! ", True)
        flag = False
    else:
        print("\nNames doesn't match.")
