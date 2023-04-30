# tuple
is_tuple = (1, 2, 3, 4, 5)
print(type(is_tuple))

# is_tuple[0] = 100 # typeerror tuple object does not support item assignment
# value cannot be changed
print(is_tuple[0]) # 1
print(is_tuple[-1]) # 5
print(is_tuple[2:5]) # 3, 4, 5
print(is_tuple) # 1, 2, 3, 4, 5
print(is_tuple.index(5)) # 4
print(is_tuple.index(2)) # 1
print(is_tuple.count(1)) # 1
# print(help(is_tuple))

is_tuple = ([1, 2, 3], [4, 5, 6]) # ([1, 2, 3], [4, 5, 6])
print(is_tuple)
# is_tuple[0] = [1] # TypeError: 'tuple' object does not support item assignment
is_tuple[0][0] = 100
print(is_tuple) # [100, 2, 3], [4, 5, 6])
is_tuple = 1, 2, 3
print(is_tuple)
is_tuple = (1,) # tuple
print(is_tuple) # (1,)
is_tuple = ('tuple') # str
print(is_tuple, type(is_tuple)) # tuple str
is_tuple = ('tuple',)
print(is_tuple, type(is_tuple)) # tuple tuple
is_tuple = (1, 2, 3) + (4, 5, 6)
print(is_tuple, type(is_tuple))
# is_tuple = is_tuple + 1 # TypeError: can only concatenate tuple (not "int") to tuple
print(is_tuple)