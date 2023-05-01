# for else statement
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

for call in ['a', 'b', 'c']:
    print('call', call)
else:
    print('call comp')