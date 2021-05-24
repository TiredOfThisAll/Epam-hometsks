def remember_result(fn):
    result = None

    def wrapper(*args):
        nonlocal result
        print(f"Last result = '{result}'")
        result = fn(*args)
        return result

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result
