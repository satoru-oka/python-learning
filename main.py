# defult arguments

def test_func(x, l=[]):
    l.append(x)
    return l

y = [1, 2, 3]
r = test_func(100, y)
print(r) # [1, 2, 3, 100]

y = [1, 2, 3]
r = test_func(200, y)
print(r) # [1, 2, 3, 200]

r = test_func(100)
print(r) # [100]

r = test_func(200)
print(r) # [100, 200]

def test_func_r(x, l=None):
    if l is None:
        l = [];
    l.append(x)
    return l

r = test_func_r(100)
print(r) # [100]

r = test_func_r(200)
print(r) # [200]
