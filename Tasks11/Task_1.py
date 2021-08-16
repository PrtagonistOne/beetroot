class Person:
    def __init__(self, firstname: str, lastname: str, year: int):
        self.firstname = firstname
        self.lastname = lastname
        self.year = year

    def greeting(self) -> None:
        print(f'My name is {self.firstname} {self.lastname}. I am {self.year} years old.')


class Teacher(Person):
    def __init__(self, firstname: str, lastname: str, year: int, salary: float, groups: str):
        super().__init__(firstname, lastname, year)
        self.salary = salary
        self.groups = groups

    def teacher_statistic(self) -> None:
        Person.greeting()
        print(f'Currently, I have a salary of {self.salary}$ and teaching {self.groups}')
