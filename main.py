# dictionary method
is_dict = {'x': 10, 'y': 20}
print(is_dict)
# help(is_dict) # class dict documents
print(is_dict.keys()) # dict_keys(['x', 'y'])
print(is_dict.values()) # dict_values([10, 20])

is_dict_update = {'x': 1000, 'j': 500}
print(is_dict) # {'x':10, 'y':20}
print(is_dict_update) # {'x': 1000, 'j': 500}
is_dict.update(is_dict_update)
print(is_dict) # {'x': 1000, 'y': 20, 'j': 500}
print(is_dict['x']) # 1000
print(is_dict.get('x')) # 1000
# print(is_dict['z']) # KeyError: 'z'
print(is_dict.get('z')) # None
print(is_dict.pop('x')) # 1000
print(is_dict) # {'y': 20, 'j': 500}
print(is_dict.clear()) # None
print(is_dict) # {}
is_dict = {'a': 100, 'b': 'b'}
print('a' in is_dict) # True
print('j' in is_dict) # False