# intra-function
def outer(a, b):
    def plus(c, d):
        return c + d
    r1 = plus(a, b) # 3
    r2 = plus(b, a) # 3
    print(r1 + r2) # 3 + 3

outer(1, 2)