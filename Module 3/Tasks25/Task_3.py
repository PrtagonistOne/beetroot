def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    elif a < 0 or n < 0:
        raise ValueError('This function only works with positive integers')

    return a + mult(a, n-1)

print(mult(2, 4))
