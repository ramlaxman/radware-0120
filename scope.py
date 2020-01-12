#!/usr/bin/env python3

x = 100


def myfunc():
    print(f'In myfunc, x = {x}')
    x = 200


print(f'Before, x = {x}')
myfunc()
print(f'After, x = {x}')


# if in a function, start here
# L Local
# E Enclosing

# if not in a function, start here
# G Global
# B Builtins
