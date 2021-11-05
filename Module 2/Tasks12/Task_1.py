class Animal:
    def __init__(self, name):
        self.name = name.lower()

    # Abstract
    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print('Woof Woof!')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print('Meow!')


def zoo(animal: Animal) -> None:
    animal.talk()


cat1 = Cat('Fluff')
dog1 = Dog('Snuff')

zoo(cat1)
zoo(dog1)
