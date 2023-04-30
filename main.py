# list method
is_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 10]
print(is_list.index(3))
print(is_list.index(9))
print(is_list)
print(is_list.index(3, 3))
print(is_list.count(3))
is_list.sort(reverse=True)
print(is_list)
is_list.sort()
print(is_list)
# split() - specification to whitespace
is_name = 'My name is Satoru'
to_split = is_name.split(' ')
print(to_split)
# join() - # join with
x = ' ######### ' .join(to_split)
print(x)
print(help(list))