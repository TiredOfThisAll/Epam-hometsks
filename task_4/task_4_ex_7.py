"""
Task04_1_7
Implement a function foo(List[int]) -> List[int] which, given a list of integers, returns a new  or modified list
in which every element at index i of the new list is the product of all the numbers in the original array except the one at i.
Example:
`python

foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]`
"""

from typing import List
from math import prod
from copy import deepcopy


def product_array(num_list: List[int]) -> List[int]:
    result = []
    zero_case = []
    for i in range(len(num_list)):
        if num_list[i] == 0:
            zero_case = deepcopy(num_list)
            del zero_case[i]
            result.append(prod(zero_case))
        else:
            result.append(prod(num_list) // num_list[i])
    return result
