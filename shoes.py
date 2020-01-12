[
    {'brand': 'Adidas',
     'color': 'orange',
     'size': '43'},

    {'brand': 'Nike',
     'color': 'black',
     'size': '41'},



]

[one_line.split(':')[0]
 for one_line in open('/etc/passwd')
 if not one_line.startswith("#")]
