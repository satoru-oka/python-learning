# generator
def counter(num=10):
    for _ in range(num):
        yield 'run'

def greeting():
    yield 'Good morning'
    # for example
    # for i in range(10000000000000000):
    #     print(i)
    yield 'Good afternoon'
    yield 'Good night'

g = greeting()
c = counter()
print(next(g))
print('@@@@@')

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print('@@@@@')

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))