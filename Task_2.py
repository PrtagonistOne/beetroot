class Dog:
    age_factor = 7

    def __init__(self, age: int):
        self.age = age

    def human_age(self) -> float:
        return Dog.age_factor + self.age


doge = Dog(7)
print(doge.human_age())
