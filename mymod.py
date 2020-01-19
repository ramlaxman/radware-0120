'''This is the first line

This is the second line

This is the third line
'''

__all__ = ['x', 'y']


x = 100

y = [10, 20, 30]


def hello(name):
    """This is a very friendly function"""
    return f'Hello, {name}'


_secret = 'shhhh'

# if not imported, do the following
if __name__ == '__main__':
    print(f"Goodbye from {__name__}!")
