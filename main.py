# dictionary copy

x = {'a': 1}
y = x
print(y) # {'a': 1}
y['a'] = 1000
print(x) # {'a': 1000}
print(y) # {'a': 1000}
print(id(x)) # 4297025344
print(id(y)) # 4297025344

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)
print(id(x)) # 4297025600
print(id(y)) # 4297386496