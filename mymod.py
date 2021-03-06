'''This is the first line

This is the second line

This is the third line
'''

__all__ = ['YOU_SHOULD_NEVER_EVER_EVER_USE_IMPORT_STAR']


x = 100

y = [10, 20, 30]


def hello(name):
    """This is a very friendly function"""
    return f'Hello, {name}'


_secret = 'shhhh'

# if not imported, do the following
if __name__ == '__main__':

    # (1) __name__ could be '__main__':
    # - python mymod.py

    # (2) __name__ could be 'mymod'
    # - import mymod
    # - from mymod import x

    print(f"Goodbye from {__name__}!")
    name = input("Enter your name: ").strip()
    print(hello(name))
