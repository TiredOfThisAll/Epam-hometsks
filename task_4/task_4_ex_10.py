"""
Create a function sum_binary_1 that for a positive integer n
calculates the result value, which is equal to the sum of the
“1” in the binary representation of n otherwise, returns None.

Example,
n = 14 = 1110 result = 3
n = 128 = 10000000 result = 1
"""
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def translation_into_number_systems(given_integer, base):
    if 1 < base > 36:
        raise ValueError
    digits = []
    while given_integer != 0:
        digits.append(alphabet[given_integer % base])
        given_integer = given_integer // base
    if not digits:
        return "0"
    return "".join(list(reversed(digits)))


def sum_binary_1(n: int):
    if not isinstance(n, int):
        return None
    if n <= 0:
        return None
    binary = translation_into_number_systems(n, 2)
    value = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            value += 1
    return value
