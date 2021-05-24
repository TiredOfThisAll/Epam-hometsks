"""
Task 2_3

You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
There is only one instance of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar). Write a function that returns the maximum weight of gold that fits
into a knapsack's capacity.

The first parameter contains 'capacity' - integer describing the capacity of a knapsack
The next parameter contains 'weights' - list of weights of each gold bar
The last parameter contains 'bars_number' - integer describing the number of gold bars
Output : Maximum weight of gold that fits into a knapsack with capacity of W.

Note:
Use the argparse module to parse command line arguments. You don't need to enter names of parameters (i. e. -capacity)
Raise ValueError in case of false parameter inputs
Example of how the task should be called:
python3 task3_1.py -W 56 -w 3 4 5 6 -n 4
"""
import itertools
import argparse


def safe_int(expression):
    try:
        return int(expression)
    except ValueError:
        return 0


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-W", type=int)
    parser.add_argument("-w", type=int, nargs="*")
    parser.add_argument("-n", type=int)

    args = parser.parse_args()
    capacity = safe_int(args.W)
    weights = list(map(safe_int, args.w))

    n = safe_int(args.n)

    if capacity <= 0 or any(filter(lambda x: x <= 0, weights)) or n <= 0:
        raise ValueError

    max_weight = 0

    lst = []

    for i in range(len(weights) + 1):
        for sublist in itertools.combinations(weights, i):
            lst.append(list(sublist))

    del lst[0]

    for i in lst:
        if capacity >= sum(i) > max_weight:
            max_weight = sum(i)
        if max_weight == capacity:
            break
    print(max_weight)


if __name__ == '__main__':
    main()
