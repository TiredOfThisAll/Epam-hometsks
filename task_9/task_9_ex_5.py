"""
Implement function count_letters, which takes string as an argument and
returns a dictionary that contains letters of given string as keys and a
number of their occurrence as values.

Example:
print(count_letters("Hello world!"))
Result: {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

Note: Pay attention to punctuation.
"""


def count_letters(string):
    if not isinstance(string, str):
        raise TypeError
    dic = {}
    for char in string:
        if char not in dic and char.isalpha():
            dic[char] = 1
        elif char in dic and char.isalpha():
            dic[char] += 1
    return dic
