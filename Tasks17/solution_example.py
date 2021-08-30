class Person:
    def __init__(self, firstname: str, lastname: str, year: int):
        self.firstname = firstname
        self.lastname = lastname
        self.year = 2021-year

    def greeting(self):
        return f'My name is {self.firstname} {self.lastname}. I am {self.year} years old.'


class Teacher(Person):
    def __init__(self, firstname: str, lastname: str, year: int, salary: float, groups: list):
        super().__init__(firstname, lastname, year)
        self.salary = round(salary * len(groups), 2)
        self.groups = groups

    def teacher_statistics(self) -> str:
        Person.greeting(self)
        return f'Currently, I have a salary of {self.salary}$ and teaching {self.groups} groups'

    def add_group(self, group):
        self.groups.append(group)

    def remove_group(self, group):
        self.groups.remove(group)

    def salary_correction(self, salary):
        self.salary = salary * len(self.groups)


class Student(Person):
    def __init__(self, firstname, lastname, year, group: int, fav_subjects: list):
        super().__init__(firstname, lastname, year)
        self.group = group
        self.fav_subjects = fav_subjects

    def student_statistics(self) -> str:
        return f'I study in group #{self.group} and my favourite subjects are {self.fav_subjects}'

    def group_change(self) -> None:
        try:
            new_group = int(input(f'Move student {self.firstname} {self.lastname} from group {self.group} to group#: '))
        except ValueError as e:
            print('Error, please input the number of group again later')
        else:
            self.group = new_group




