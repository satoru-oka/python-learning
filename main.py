is_set = {1, 2, 3, 4, 5}
print(is_set, type(is_set)) #{1, 2, 3, 4, 5} <class 'set'>

is_set.add(6)
print(is_set) # {1, 2, 3, 4, 5, 6}

is_set.add(6)
print(is_set) # {1, 2, 3, 4, 5, 6}

is_set.remove(2)
print(is_set) # {1, 3, 4, 5, 6}
# help(set)
is_set.clear()
print(is_set) # set()