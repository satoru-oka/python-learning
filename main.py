# list operation
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list, type(list)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g'] type - list
print(list[0])
list[0] = 'A'
print(list[0]) # print 'A'
#print(list[2:5]) # ['c', 'd', 'e']
list[2:5] = ['C', 'D', 'E']
print(list) # ['A', 'b', 'C', 'D', 'E', 'f', 'g']
list[2:5] = []
print(list) # ['A', 'b', 'f', 'g']
print(list[:]) #['A', 'b', 'f', 'g']
list[:] = []
print(list) # []
print("########## append, insert, pop, remove")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
n.insert(0, 200)
print(n) # [200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
print(n.pop()) # pop 100
print(n) # [200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n.pop(0)) # 200
print(n) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.remove(3) # remove 3
print(n) # # [1, 2, 4, 5, 6, 7, 8, 9, 10]
print("########## join")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a)
print(b)
x = a + b
print(x) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a += b
print(a) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

