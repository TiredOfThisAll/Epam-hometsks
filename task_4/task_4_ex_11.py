def fibonacci_loop(seq):
    for i in seq:
        if isinstance(i, float):
            continue
        if isinstance(i, str):
            break
        print(i, end=" ")
