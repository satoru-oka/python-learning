# generator inclusion notation
def generator():
    for i in range(10):
        yield i
g = generator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('##### generator 1') # generator
g = (i for i in range(10))
for x in g:
    print(x)

print('##### generator 2')
g = (i for i in range(10) if i % 2 == 0)
for x in g:
    print(x)


print('##### tuple') # tuple
g = tuple(i for i in range(10))
for x in g:
    print(x)
