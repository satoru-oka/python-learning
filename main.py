is_tuple_1 = (1, 2, 3, 4, 5)
is_tuple_2 = (1, 2, 3, 4, 5)

is_list = []
for i in is_tuple_1:
    is_list.append(i)

print(is_list) # [1, 2, 3, 4, 5]

is_list = [i for i in is_tuple_1]
print(is_list) # [1, 2, 3, 4, 5]

is_list = []
for i in is_tuple_2:
    if i % 2 == 0:
        is_list.append(i)

print(is_list) # [2, 4]

is_list = [i for i in is_tuple_2 if i % 2 == 0]
print(is_list) # [2, 4]

is_list = []
for i in is_tuple_1:
    for j in is_tuple_2:
        is_list.append(i * j)

print(is_list) # 1, 2, 3, 4, 5, 2, 4, 6, 8, 10, 3, 6, 9, 12, 15, 4, 8, 12, 16, 20, 5, 10, 15, 20, 25]

is_list = [i * j for i in is_tuple_1 for j in is_tuple_2]
print(is_list) # 1, 2, 3, 4, 5, 2, 4, 6, 8, 10, 3, 6, 9, 12, 15, 4, 8, 12, 16, 20, 5, 10, 15, 20, 25]