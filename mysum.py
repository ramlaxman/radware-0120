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


# [master ✗ ~/Consulting/Courses/Python/radware-0120]$ mypy --strict mysum.py
# mysum.py:15: error: Argument 1 to "mysum" has incompatible type "Tuple[int, int, int, int]"; expected "List[Union[int, float]]"
# mysum.py:16: error: List item 1 has incompatible type "str"; expected "float"
# Found 2 errors in 1 file (checked 1 source file)
# [master ✔ ~/Consulting/Courses/Python/radware-0120]$ mypy --strict mysum.py
# mysum.py:16: error: List item 1 has incompatible type "str"; expected "float"
# Found 1 error in 1 file (checked 1 source file)
