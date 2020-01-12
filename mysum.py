#!/usr/bin/env python3

from typing import List, Union, Sequence


def mysum(numbers: Sequence[Union[int, float]]) -> Union[int, float]:
    total: Union[int, float] = 0
    for one_number in numbers:
        total += one_number
    return total


print(mysum([10, 20, 30]))
print(mysum([10, 20.3, 30]))
print(mysum((10, 20, 30, 40)))
# print(mysum([10, '20', 30]))
