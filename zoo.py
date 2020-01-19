#!/usr/bin/env python3


class Wolf:
    def __init__(self, color):
        self.color = color
        self.species = 'wolf'
        self.number_of_legs = 4


class Sheep:
    def __init__(self, color):
        self.color = color
        self.species = 'sheep'
        self.number_of_legs = 4


class Snake:
    def __init__(self, color):
        self.color = color
        self.species = 'snake'
        self.number_of_legs = 0


class Parrot:
    def __init__(self, color):
        self.color = color
        self.species = 'parrot'
        self.number_of_legs = 2


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


# c1 = Cage(1)
# c1.add_animals(wolf, sheep1, sheep2)
# print(c1)                        # cage number + animal printouts


# c2 = Cage(2)                    # an ID number, not that important
# c2.add_animals(snake, parrot)
# print(c2)                        # cage number + animal printouts

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
