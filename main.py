# dictionary inclusion notation
date = ['mon', 'tue', 'wed']
drink = ['coffee', 'milk', 'water']

is_dict = {}
for x, y in zip(date, drink):
    is_dict[x] = y
print(is_dict) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}

is_dict = {x: y for x, y in zip(date, drink)}
print(is_dict) # {'mon': 'coffee', 'tue': 'milk', 'wed': 'water'}