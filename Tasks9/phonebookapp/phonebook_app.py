import phonebook_func


user_session_flag = True
while user_session_flag:
    user_choice = int(input('\t****  THIS IS A PHONEBOOK APP ****\nChoose from the list below.\n1. Add a new contact\n'
                            '2. Search by first name\n3. Search by last name\n4. Search by full name\n5.Search by phone'
                            ' number\n6. Search by city or state\n7. Delete a record for a given telephone number\n8. '
                            'Update a record for a given telephone number\n9. Exit\nInput number from 1 to 9: '))
    if user_choice == 1:
        phonebook_func.add_contact()
    elif user_choice == 2:
        phonebook_func.search(user_choice)
    elif user_choice == 3:
        phonebook_func.search(user_choice)
    elif user_choice == 4:
        phonebook_func.search(user_choice)
    elif user_choice == 5:
        phonebook_func.search(user_choice)
    elif user_choice == 6:
        phonebook_func.search(user_choice)
    elif user_choice == 7:
        phonebook_func.del_contact()
