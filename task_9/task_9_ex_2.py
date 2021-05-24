"""
Write a function that checks whether a string is a palindrome or not.
Return 'True' if it is a palindrome, else 'False'.

Note:
Usage of reversing functions is required.
Raise ValueError in case of wrong data type

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(test_string: str) -> bool:
    if not isinstance(test_string, str):
        raise ValueError
    index = 0
    for i in reversed(test_string):
        if i.isalpha() and test_string[index].isalpha():
            if not i.lower() == test_string[index].lower():
                return False
        return True


    # if test_string.lower().replace(" ", "") == test_string[::-1].lower().replace(" ", ""):
    #     return True
    # return False


print(is_palindrome("Do geese see God"))