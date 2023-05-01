# set
is_set_a = {1, 2, 3, 4, 5, 6, 7, 7, 7}
print(is_set_a, type(is_set_a)) # {1, 2, 3, 4, 5, 6, 7} <class 'set'>
is_set_b = {1, 2, 3, 4, 5, 8, 11, 15}

is_set_result = is_set_a - is_set_b
print(is_set_result) # {6, 7}

is_set_result = is_set_b - is_set_a
print(is_set_result) # {8, 11, 15}

is_set_result = is_set_a & is_set_b
print(is_set_result) # {1, 2, 3, 4, 5}

# is_set_result = is_set_a + is_set_b
# print(is_set_result) # TypeError: unsupported operand type(s) for +: 'set' and 'set'

is_set_result = is_set_a | is_set_b
print(is_set_result) # {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15}

is_set_result = is_set_a ^ is_set_b
print(is_set_result) # {6, 7, 8, 11, 15}