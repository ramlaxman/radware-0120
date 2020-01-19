#!/usr/bin/env python3


class Person():
    population = 0              # Person.population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def greet(self):
        return f'Hello, {self.name}'


print(f'Before, population = {Person.population}')
p1 = Person('name1')
p2 = Person('name2')
print(f'After, population = {Person.population}')

print(p1.greet())
print(p2.greet())
