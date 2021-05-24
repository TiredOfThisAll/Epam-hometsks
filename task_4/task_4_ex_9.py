"""
For a positive integer n calculate the result value, which is equal to the sum
of the odd numbers of n.

Example,
n = 1234 result = 4
n = 246 result = 0

Write it as function.

Note:
Raise TypeError in case of wrong data type or negative integer;
Use of 'functools' module is prohibited, you just need simple for loop.
"""


def sum_odd_numbers(n: int) -> int:
    n = str(n)
    if not n.isnumeric():
        raise TypeError
    if int(n) <= 0:
        raise TypeError
    value = 0
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            value += int(n[i])
    return value
