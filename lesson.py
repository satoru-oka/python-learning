# Built-in Types
is_string = "falkdfjaeioqrgkja,czm,vnajfhaskl;fqierysa:gjakdf" \
            "jaslkfajfkljasjfwqeskjadfaskl;jfdfbkjtio"
is_dict = {}
for x in is_string:
    if x not in is_dict:
        is_dict[x] = 0
    is_dict[x] += 1
print(is_dict)

is_dict = {}
for x in is_string:
    is_dict.setdefault(x, 0)
    is_dict[x] += 1
print(is_dict)

from collections import defaultdict

is_dict = defaultdict(int)
for x in is_string:
    is_dict[x] += 1
print(is_dict)

print(is_dict['f'])