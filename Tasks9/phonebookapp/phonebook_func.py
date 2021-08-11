import json


def search_read():
    with open('phonebook_data.json', 'r') as f:
        data = json.load(f)
    return data


def del_contact():
    data = search_read()
    phone_num = input('Input phone number to delete: ').strip().title()
    for index, value in enumerate(data['contacts']):
        if value['Phone number'] == phone_num:
            data['contacts'].pop(index)
    with open('phonebook_data.json', 'w') as f:
        json.dump(data, f, indent=4)


def search(option):
    data = search_read()
    if option == 2:
        first_name = input('Input first name: ').strip().title()
        for index, value in enumerate(data['contacts']):
            if value['First name'] == first_name:
                print(value)
    elif option == 3:
        last_name = input('Input last name: ').strip().title()
        for index, value in enumerate(data['contacts']):
            if value['Last name'] == last_name:
                print(value)
    elif option == 4:
        full_name = input('Input full name: ').strip().title()
        for index, value in enumerate(data['contacts']):
            if value['Full name'] == full_name:
                print(value)
    elif option == 5:
        phone_num = input('Input phone number: ').strip()
        for index, value in enumerate(data['contacts']):
            if value['Phone number'] == phone_num:
                print(value)
    elif option == 5:
        city_state = input('Input city or state: ').strip()
        for index, value in enumerate(data['contacts']):
            if value['City or State'] == city_state:
                print(value)


def add_contact():
    print('\tNew contact MUST have at least a PHONE NUMBER and it has to be 10 characters long to be added!')
    data = {'Phone number': None, 'First name': None, 'Last name': None, 'City or State': None}
    for key, value in data.items():
        data[key] = input(f'{key}: ').title()
    if (data['First name'] is not None) and (data['Last name'] is not None):
        data['Full name'] = data['First name'].title() + ' ' + data['Last name'].title()
    if data['Phone number'] is None or len(data['Phone number']) is not 10:
        data.clear()
        print('Contact was not added, try again')
    else:
        book_data = search_read()
        book_data_list = book_data['contacts']
        book_data_list.append(data)
        book_data['contacts'] = book_data_list
        print('New contact was added successfully!')
