"""
Write 2 functions:
1. Function 'is_sorted', determining whether a given list of integer values of arbitrary length
is sorted in a given order (the order is set up by enum value SortOrder).
List and sort order are passed by parameters. Function does not change the array, it returns
boolean value.

2. Function 'transform', replacing the value of each element of an integer list with the sum
of this element value and its index, only if the given list is sorted in the given order
(the order is set up by enum value SortOrder). List and sort order are passed by parameters.
To check, if the array is sorted, the function 'is_sorted' is called.

Example for 'transform' function,
For [5, 17, 24, 88, 33, 2] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “ascending” sort order values in the array do not change;
For [15, 10, 3] and “descending” sort order the values in the array are changing to [15, 11, 5]

Note:
Raise TypeError in case of wrong function arguments data type;
"""
from enum import Enum
import operator


class SortOrder(Enum):
    ASCENDING = "ascending"
    DESCENDING = "descending"


def is_sorted(num_list, sort_order):
    if type(num_list) is not list or type(sort_order) is not SortOrder:
        raise TypeError
    for num in num_list:
        if not str(num).isdigit():
            raise TypeError
    comparator = operator.le \
        if sort_order == SortOrder.ASCENDING \
        else operator.ge
    return all(map(comparator, num_list[:-1], num_list[1:]))


def transform(num_list, sort_order):
    if not is_sorted(num_list, sort_order):
        return num_list
    return list(map(operator.add, num_list, range(len(num_list))))
