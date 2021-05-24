"""
Task04_1_2
Write `is_palindrome` function that checks whether a string is a palindrome or not
Returns 'True' if it is palindrome, else 'False'

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

Note:
Usage of any reversing functions is prohibited.
The function has to ignore special characters, whitespaces and different cases
Raise ValueError in case of wrong data type
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError
    reversed_list = []
    i = 0
    palindrome_list = list(test_string)
    size = len(test_string) - 1
    while i <= size:
        if palindrome_list[size].isalpha():
            reversed_list.append(palindrome_list[size])
            size -= 1
        else:
            del palindrome_list[size]
            size -= 1
    print(palindrome_list, reversed_list)
    test_string = "".join(palindrome_list)
    reversed_string = "".join(reversed_list)
    if test_string.lower() == reversed_string.lower():
        return True
    return False
