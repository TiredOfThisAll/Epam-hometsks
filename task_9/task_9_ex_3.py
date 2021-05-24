"""
Implement a function get_longest_word(s: str) -> str which returns the
longest word in the given string. The word can contain any symbols
except whitespaces (`,\n,\t and so on). If there are multiple longest
words in the string with a same length return the word that occurs first.

Example:
get_longest_word('Python is simple and effective!')
#output: 'effective'
get_longest_word('Any pythonista like namespaces a lot.')
#output: 'pythonista'

Note:
Raise ValueError in case of wrong data type
Usage of 're' library is required.
"""
import re


def get_longest_word(string):
    if not isinstance(string, str):
        raise ValueError
    regex = re.compile("\w+")
    words_found = regex.findall(string)

    if words_found:
        longest_word = max(words_found, key=lambda word: len(word))
        return longest_word


print(get_longest_word('Python is simple and effective!'))
