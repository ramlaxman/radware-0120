#!/usr/bin/env python2.7


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


class Cage(object):
    def __init__(self, cage_number):
        self.cage_number = cage_number
        self.animals = []

    def add_animals(self, *args):
        self.animals += args

    def __repr__(self):
        output = 'Cage {0}\n'.format(self.cage_number)
        output += '\n'.join(['\t{0}'.format(one_animal)
                             for one_animal in self.animals])
        return output


c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)
print(c1)                        # cage number + animal printouts


c2 = Cage(2)                    # an ID number, not that important
c2.add_animals(snake, parrot)
print(c2)                        # cage number + animal printouts

print('---- zoo -----')


class Zoo(object):
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        self.cages += args

    def __repr__(self):
        return '\n'.join([str(one_cage)
                          for one_cage in self.cages])

    def animals_by_color(self, color):
        return '\n'.join([str(one_animal)
                          for one_cage in self.cages
                          for one_animal in one_cage.animals
                          if one_animal.color == color])

    def number_of_legs(self):
        return sum([one_animal.number_of_legs
                    for one_cage in self.cages
                    for one_animal in one_cage.animals])


z = Zoo()
z.add_cages(c1, c2)
print(z)                           # show all cages, all animals

print(z.animals_by_color('black'))
print(z.number_of_legs())
