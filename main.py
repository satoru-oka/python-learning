# for, break, continue statement
some_list = [1, 2, 3, 4, 5]
i = 0

while i < len(some_list):
    print(some_list[i]) # 1 2 3 4 5
    i += 1

print('##########')

for i in some_list:
    print(i)

print('##########')

for s in 'abcde':
    print(s)

print('##########')

for word in ['My', 'name', 'is', 'satoru']:
    if word == 'name':
        continue
    print(word)