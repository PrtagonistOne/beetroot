import json
import unittest
import phonebookapp.phonebook_func


class PhonebookTestCase(unittest.TestCase):
    def setUp(self):
        with open('phonebookapp/phonebook_data.json', 'r') as f:
            self.data = json.load(f)

    def tearDown(self):
        with open('phonebookapp/phonebook_data.json', 'w') as f:
            json.dump([], f, indent=4)

    def test_add_contact_to_phonebook(self):
        test_add_data = phonebookapp.phonebook_func.add_contact('0506762599', 'Sasha', 'Kop', 'Cherniv')
        self.setUp()
        self.assertEqual(test_add_data, self.data)

    def test_update_contact_to_phonebook(self):
        phonebookapp.phonebook_func.add_contact('0506762599', 'Sasha', 'Kop', 'Cherniv')
        test_update_data = phonebookapp.phonebook_func.update_contact('0506762599', 'Sasha', 'Kopiievyi', 'Chern',
                                                                      '0953403406')
        self.setUp()
        self.assertEqual(test_update_data, self.data)


unittest.main()
