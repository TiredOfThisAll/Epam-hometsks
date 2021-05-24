"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re


def most_common_words(file_path, top_words):
    words_dict = {}
    with open(file_path) as file:
        words = re.split("\s|,|\.", file.read())
    for word in words:
        if word == '':
            continue
        if word.lower() in words_dict:
            words_dict[word.lower()] += 1
        else:
            words_dict[word.lower()] = 1
    final_result = sorted(words_dict, key=lambda word: words_dict[word], reverse=True)
    return final_result[:top_words]


# print(most_common_words("words.txt", 5))
