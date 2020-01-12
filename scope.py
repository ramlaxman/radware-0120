#!/usr/bin/env python3

x = 100
y = [10, 20, 30]


def myfunc():
    global x
    x = 200
    y[0] = '!'
    print(f'In myfunc, x = {x}')


print(f'Before, x = {x}')
myfunc()
print(f'After, x = {x}')


# if in a function, start here
# L Local
# E Enclosing

# if not in a function, start here
# G Global
# B Builtins
