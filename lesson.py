# class variable
class Person(object):

    kind = 'human'
    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)

a = Person('A')
a.who_are_you() # A human
b = Person('B')
b.who_are_you() # B human

class T(object):
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

test1 = T()
test1.add_word('add 1')
test1.add_word('add 2')
print(test1)
print(test1.words) # ['add 1', 'add 2']

test2 = T()
test2.add_word('add 3')
test2.add_word('add 4')
print(test2)
print(test2.words) # ['add 3', 'add 4']