class Fraction(int):
    def __init__(self, math_expression):
        self.math_expression = math_expression


x = Fraction(1/2)
print(x.math_expression)
