"""
Task_9_1
Implement `swap_quotes` function which receives a string and replaces all " symbols with ' and vise versa.
The function should return modified string.

Note:
Usage of built-in or string replacing functions is required.
"""


# def swap_quotes(some_string: str) -> str:
#     text_list = some_string.split("'")
#     for i in range(len(text_list)):
#         text_list[i] = text_list[i].replace('"', "'")
#     return '"'.join(text_list)
    # x01 = b'\x01'.decode("utf-8")
    # return some_string.replace('"', x01).replace("'", '"').replace(x01, "'")


# def swap_quotes_anton(text):
#     text_list = text.split("'")
#     for i in range(len(text_list)):
#         text_list[i] = text_list[i].replace('"', "'")
#     return '"'.join(text_list)

def decode(basic):
    encoded = "abcdefghijklmnkopeqrtkscjabcuvwxykz"
    decoded = "thequickbrownfoxjumpsoverthelazydog"
    dictionary = {}
    result = []
    for i in range(len(encoded)):
        dictionary[encoded[i]] = decoded[i]
    for i in basic:
        if i not in dictionary.keys():
            result.append(i)
        else:
            result.append(dictionary[i])
    return "".join(result)


print(decode("123zkky uegh"))
