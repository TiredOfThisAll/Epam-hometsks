"""
Task04_3

Implement a function which works the same as str.split

Note:
Usage of str.split method is prohibited
Raise ValueError in case of wrong data type
"""


def split_alternative(str_to_split: str, delimiter=None) -> list:
    if not isinstance(str_to_split, str) or not isinstance(delimiter, str):
        raise ValueError
    split_expression = []
    part_of_expression = []
    for i in str_to_split:
        if i == delimiter and part_of_expression:
            split_expression.append("".join(part_of_expression))
            part_of_expression.clear()
            continue
        elif i == delimiter and not part_of_expression:
            continue
        part_of_expression.append(i)
    split_expression.append("".join(part_of_expression))
    return split_expression
