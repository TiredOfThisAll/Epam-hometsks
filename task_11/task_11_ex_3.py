def call_once(func):
    called = False
    result = None

    def wrapper(*args):
        nonlocal called
        nonlocal result
        if not called:
            called = True
            result = func(*args)
        return result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b
