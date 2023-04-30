# tuple unpacking
num_tuple = (10, 20)
print(num_tuple) # (10, 20)

x, y = num_tuple
print(x, y) # 10, 20

min, max = 0, 100
print(min, max) # 0 100
is_tuple = 0, 100, 200
print(type(is_tuple)) # tuple

a, b, c, d, e, f = 'satoru', '1', '1', '1', 'e', 'f'
# best practice
a = 'satoru'
b = '1'

i = 10
j = 20
tmp = i # 10
i = j # 20
j = tmp # 10

print(i, j)

a = 100
b = 200
print(a, b) # 100, 200
a, b = b, a # 200, 100
print(a, b) # 200, 100