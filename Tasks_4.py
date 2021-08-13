from random import randint, shuffle
from msvcrt import getch

# Task 1
flag = True
flag_skip = False
while flag:
    if not flag_skip:
        print("\nLet's play a GUESSING GAME against the computer!\nJust input a number between 1 and 10!\n")
        random_number = randint(1, 10)
        user_number = int(input("Your guess: "))
    if user_number == random_number:
        print('\nYou guessed right! Congratulations!')
        flag = False
    else:
        user_choice = input(f"\nYou guessed WRONG!\nThe number is {random_number}"
                            f"\nWould you like another round? [Yes or No]: ").lower().strip()
        if user_choice == 'yes':
            flag_skip = False
            continue
        elif user_choice == 'no':
            print("\nSee you next time!")
            flag = False
        else:
            print('\nError. Please type yes or no.')
            getch()
            flag_skip = True
# Task 2
name = input('\nWhat is your name?\nYour name: ').lower()
age = int(input('\nWhat is your age?\nYour age (enter the number): '))
print(f'\nHello {name.title()}, on your next birthday you\'ll be {age + 1} years old ')


# Task 3

def rand_unique_generator(b):
    nums = list(range(b))
    shuffle(nums)
    return nums


flag = True
while flag:
    word = input('\nLet\'s play WORDS COMBINATION!\nPlease enter a word to create 5 random strings!\nThe word: ') \
        .lower().strip()
    output_string = ''
    for k in range(5):
        random_order_nums = rand_unique_generator(len(word))
        output_string = ''
        for i in range(len(word)):
            # print(random_order_nums, random_order_nums[i], len(word))
            output_string = output_string + word[random_order_nums[i]]
        print(f'{k + 1}) {output_string.title()}')
    if k == 4:
        flag = False
# Task 4

flag = True
flag_skip = False
while flag:
    x = randint(1, 10)
    y = randint(1, 10)
    math_expression = x * y
    if not flag_skip:
        user_input = int(input(f'\nLet\'s play THE MATH QUIZ!\nResolve a math expression to win 1 BILLION dollars!\n'
                               f'How much will be {x} * {y} = '))
    if user_input == math_expression:
        print('\n Congratulations! Your answer is right! You won a BILLION dollars!')
        flag = False
    else:
        user_choice = input('\nUnfortunately, your answer is FALSE, would you like another try? '
                            '\nType [Yes or No]: ').lower()
        if user_choice == "yes":
            flag_skip = False
            continue
        elif user_choice == "no":
            flag = False
        else:
            print('\nError. Enter yes or no.')
            flag_skip = True
