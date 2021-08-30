import unittest
import solution_example


class PersonTestCase(unittest.TestCase):
    def setUp(self):
        self.my_person = solution_example.Person('John', 'Wick', 1991)

    def test_greetings(self):
        self.assertEqual(self.my_person.greeting(), f'My name is John Wick. I am 30 years old.')


class TeacherTestCase(unittest.TestCase):
    def setUp(self):
        self.my_teacher = solution_example.Teacher('Mike', 'Stevens', 1992, 300.20, [341, 141, 244])

    def test_group_add(self):
        self.assertEqual(self.my_teacher.groups, [341, 141, 244])
        self.my_teacher.add_group(144)
        self.assertEqual(self.my_teacher.groups, [341, 141, 244, 144])

    def test_teacher_stats(self):
        self.assertEqual(self.my_teacher.teacher_statistics(), f'Currently, I have a salary of 900.6$ and teaching ['
                                                               f'341, 141, 244] groups')


unittest.main()
