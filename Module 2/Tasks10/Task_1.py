class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstName = firstname
        self.lastName = lastname
        self.age = age

    def talk(self) -> None:
        print(f'Hello! My name is {self.firstName} {self.lastName} and I am {self.age} years old!')


somePerson = Person('John', 'Johnson', 27)
somePerson.talk()
