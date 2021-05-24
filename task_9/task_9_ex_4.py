import string


def chars_in_all(*strings):
    chars = chars_in_one(*strings)
    for i in strings:
        chars = chars.intersection(set(i))
    return chars


def chars_in_one(*strings):
    chars = []
    for i in strings:
        if not isinstance(i, str):
            raise TypeError
        for j in i:
            if j not in chars:
                chars.append(j)
    return set(chars)


# def chars_in_two(*strings):
#     chars = []
#     for i in range(len(strings) - 1):
#         for j in range(i + 1, len(strings)):
#             for char in chars_in_one(strings[i]).intersection(chars_in_one(strings[j])):
#                 chars.append(char)
#     return set(chars)


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError
    dic = {}
    chars = []
    for str_1 in strings:
        if not isinstance(str_1, str):
            raise TypeError
        for char in chars_in_one(str_1):
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
    for key, value in dic.items():
        if value > 1:
            chars.append(key)
    return set(chars)


def not_used_chars(*strings):
    chars = list(chars_in_one(*strings))
    not_used = []
    alphabet = list(string.ascii_lowercase)
    for char in alphabet:
        if char not in chars:
            not_used.append(char)
    return set(not_used)
