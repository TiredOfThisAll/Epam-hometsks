def get_digits(*args):
    some_digits = []
    for i in args:
        for arg in str(i):
            some_digits.append(int(arg))
    return tuple(some_digits)


print(get_digits(8717, 82911, 99))
