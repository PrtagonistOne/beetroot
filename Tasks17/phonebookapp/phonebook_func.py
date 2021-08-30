import json


def update_contact(phone_num=None, first_name=None, last_name=None, city_state=None, new_phone_num=None):
    data_list = search_read()
    if new_phone_num is None:
        new_phone_num = phone_num
    for index, value in enumerate(data_list):
        if value['Phone number'] == phone_num:
            value['Phone number'] = new_phone_num
            value['First name'] = first_name
            value['Last name'] = last_name
            value['Full name'] = first_name + ' ' + last_name
            value['City or State'] = city_state
            break
    with open('phonebookapp/phonebook_data.json', 'r+') as f:
        json.dump(data_list, f, indent=4)

    return data_list


def search_read():
    with open('phonebookapp/phonebook_data.json', 'r') as f:
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


def add_contact(phone_num=None, first_name=None, last_name=None, city_state=None):
    contact_list = search_read()
    data = {'Phone number': phone_num, 'First name': first_name, 'Last name': last_name, 'City or State': city_state}
    if (data['First name'] is not None) and (data['Last name'] is not None):
        data['Full name'] = data['First name'].title() + ' ' + data['Last name'].title()
    if data['Phone number'] is None or len(data['Phone number']) != 10:
        data.clear()
        print('Contact was not added, try again')
    else:
        print('New contact was added successfully!')

    with open('phonebookapp/phonebook_data.json', 'r+') as f:
        contact_list.append(data)
        json.dump(contact_list, f, indent=4)

    return contact_list
