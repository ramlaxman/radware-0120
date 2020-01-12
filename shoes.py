#!/usr/bin/env python3

filename = 'shoe-data.txt'


def line_to_dict(one_line):
    # brand, color, size = one_line.strip().split('\t')

    # return {'brand': brand,
    #         'color': color,
    #         'size': size}

    return dict(zip(['brand', 'color', 'size'],
                    one_line.strip().split('\t')))


shoes = [line_to_dict(one_line)
         for one_line in open(filename)]

for one_shoe in shoes:
    print(one_shoe)

# [
#     {'brand': 'Adidas',
#      'color': 'orange',
#      'size': '43'},

#     {'brand': 'Nike',
#      'color': 'black',
#      'size': '41'},


# ]

# [one_line.split(':')[0]
#  for one_line in open('/etc/passwd')
#  if not one_line.startswith("#")]

# files.lerner.co.il --> advanced files link
