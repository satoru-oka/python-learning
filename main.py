# set inclusion notation
is_set = set()

for i in range(10):
    if i % 2 == 0:
        is_set.add(i)

print(is_set) # {0, 2, 4, 6, 8}

is_set = {i for i in range(10) if i % 2 == 0}
print(is_set) # {0, 2, 4, 6, 8}