# techniques for determining the absence of a value

# ng - False, 0, 0.0 '', [], (), {}, None
# ok - -1, 1, [1,], (1,2),{'x': 1}
is_ok = [1, 2, 3, 4, 5]
# is_ok = None,
# is_ok  = {'x': 1, 'y': 2}

if is_ok:
    print('ok')
else:
    print('ng')
