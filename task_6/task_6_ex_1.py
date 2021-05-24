"""
Implement function combine_args, which receives a changeable
number of dictionaries (keys - letters, values - integers)
and combines them into one dictionary.

Dict values should be summarized in case of identical keys.

Example:
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_args(dict_1, dict_2)
Result: {'a': 300, 'b': 200, 'c': 300}

combine_args(dict_1, dict_2, dict_3)
Result: {'a': 600, 'b': 200, 'c': 300, 'd': 100}
"""


def combine_dicts(*args):
    result = {}
    for dict in args:
        for key in dict.keys():
            if not key.isalpha() or len(key) != 1:
                raise KeyError
            if not isinstance(dict[key], int):
                raise ValueError
            if key in result:
                result[key] += dict[key]
            else:
                result[key] = dict[key]
    return result
