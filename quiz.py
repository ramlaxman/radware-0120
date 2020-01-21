#!/usr/bin/env python3


print("A")


class Person():
    print("B")

    def __init__(self, name):
        print("C")
        self.name = name

    def greet(self):
        return f'Hello, {self.name}'

    print("D")


print("E")

p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())
