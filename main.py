# dictionary
is_dict = {'x': 10, 'y': 20}
print(is_dict, type(is_dict)) # {'x': 10, 'y': 20} <class 'dict'>
print(is_dict['x']) # 10
print(is_dict['y']) # 20
is_dict['x'] = 'xxxxx'
print(is_dict, type(is_dict)) # {'x': 'xxxxx', 'y': 20} <class 'dict'>
is_dict['z'] = 'zzzzz'
print(is_dict) # {'x': 'xxxxx', 'y': 20, 'z': 'zzzzz'}
is_dict[1] = 10000
print(is_dict) # {'x': 'xxxxx', 'y': 20, 'z': 'zzzzz', 1: 10000}
is_dict = dict(a=10, b=20)
print(is_dict) # {'a': 10, 'b': 20}
is_dict = dict([('a', 10), ('b', 20)])
print(is_dict) # {'a': 10, 'b': 20}