def my_abs(x):
    if type(x) == complex:
        return (x.real ** 2 + x.imag ** 2) ** 0.5
    if x == 0:
        return x ** 2
    elif x < 0:
        return -x
    else:
        return x

print(my_abs(3+4j), my_abs(-0.0), my_abs(-5))