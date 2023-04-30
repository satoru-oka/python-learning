# cross-valued
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)
print(id(j))
print(id(j))

# call by reference
x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]
y[0] = 100
print('y =', y)
print('x =', x)
print(id(y))
print(id(x))