# In and Not
y = [1, 2, 3]
x = 1

if x in y:
    print('in') # in

if 100 not in y:
    print('not in') # not in

is_ok_1 = True

if is_ok_1:
    print(is_ok_1, type(is_ok_1)) # True <class 'bool'>

is_ok_2 = False

if not is_ok_2:
    print(is_ok_2, type(is_ok_2)) # False <class 'bool'>