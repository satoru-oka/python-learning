# string index and slice
word = 'python'
print(word[0])
print(word[1])
print(word[5])
print(word[-1])
print(word[-6])
print('##########')
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])
print('##########')
print(len(word))
word = 'j' + word[1:]
print(word[:])
n = len(word)
print(n)