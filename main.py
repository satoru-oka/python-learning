# Processing dictionaries with for statements.
is_dict = {'x': 100, 'y': 200}

print(is_dict.items())

for k, v in is_dict.items():
    print(k, ':', v)

help(is_dict)