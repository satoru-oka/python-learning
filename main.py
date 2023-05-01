# is none or is not none
is_empty = None

if is_empty is not None:
    print('Not None')
else:
    print('None')

if is_empty is None:
    print('None')

a = 1
b = 2
print(a == True) # true
print(a is True) # false
print(None is None) # true