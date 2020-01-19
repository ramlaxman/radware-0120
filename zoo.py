#!/usr/bin/env python3


class Animal():
    def __init__(self, color, number_of_legs):
        self.color = color
        self.species = type(self).__name__.lower()
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


wolf = Wolf('black')            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)                      # black wolf, 4 legs
print(sheep1)                    # white sheep, 4 legs
print(sheep2)                    # white sheep, 4 legs
print(snake)                     # brown snake, 0 legs
print(parrot)                    # black parrot, 2 legs


class Cage():
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *args):
        self.animals += args

    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join([str(one_animal)
                             for one_animal in self.animals])
        return output


c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)
print(c1)                        # cage number + animal printouts


c2 = Cage(2)                    # an ID number, not that important
c2.add_animals(snake, parrot)
print(c2)                        # cage number + animal printouts

# print('---- zoo -----')


# z = Zoo()
# z.add_cages(c1, c2)
# print(z)                           # show all cages, all animals

# print(z.animals_by_color('black'))
# print(z.number_of_legs())


# #!/usr/bin/env python3


# class Person():

#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f'Hello, {self.name}'


# p1 = Person('name1')
# p2 = Person('name2')

# print(p1.greet())
# print(p2.greet())
