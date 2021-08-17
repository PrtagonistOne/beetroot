class Person:
    def __init__(self, firstname: str, lastname: str, year: int):
        self.firstname = firstname
        self.lastname = lastname
        self.year = 2021-year

    def greeting(self) -> None:
        print(f'\nGreetings! My name is {self.firstname} {self.lastname}. I am {self.year} years old.')


class Teacher(Person):
    def __init__(self, firstname: str, lastname: str, year: int, salary: float, groups: list):
        super().__init__(firstname, lastname, year)
        self.salary = salary * len(groups)
        self.groups = groups

    def teacher_statistics(self) -> None:
        Person.greeting(self)
        print(f'Currently, I have a salary of {self.salary}$ and teaching {self.groups} groups')

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

    def student_statistics(self) -> None:
        Person.greeting(self)
        print(f'I study in group #{self.group} and my favourite subjects are {self.fav_subjects}')

    def group_change(self) -> None:
        try:
            new_group = int(input(f'Move student {self.firstname} {self.lastname} from group {self.group} to group#: '))
        except ValueError as e:
            print('Error, please input the number of group again later')
        else:
            self.group = new_group


stud1 = Student('Oleksandr', 'Korchevniy', 2001, 341, ['English', 'Mathematics', 'PE'])
stud2 = Student('Vadim', 'Kordon', 2001, 340, ['Java', 'Java-script', 'Computer Design'])
stud3 = Student('Anton', 'Ukrainets', 2000, 141, ['C# programing', 'PE', 'Computer Design'])

students = [stud1, stud2, stud3]
groups = [i.group for i in students]

teacher1 = Teacher('Olena', 'Dvorzhak', 1979, 300, groups)

print('Teacher and student info before change:')
teacher1.teacher_statistics()
[i.student_statistics() for i in students]

stud2.group_change()
teacher1.add_group(444)
teacher1.remove_group(141)
teacher1.salary_correction(350)

print('\nTeacher and stud info after change: \n')
teacher1.teacher_statistics()
[i.student_statistics() for i in students]

