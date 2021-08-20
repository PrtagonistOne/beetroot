class Fraction(float):
    def __init__(self, math_expression):
        self.math_expression = math_expression

    def __str__(self):
        return str(self.math_expression)

    def __repr__(self):
        return self.__str__()


x = Fraction(1/2)
y = Fraction(1/4)

print(x + y == Fraction(3/4))

x = Fraction(2 + 4)
y = Fraction(3 + 3)

print(x and y == Fraction(10 - 4))
