# tupling positional arguments
def say_something(word1, word2, word3):
    print(word1)
    print(word2)
    print(word3)

say_something('a', 'b', 'c')

print('##### tupling positional arguments')
def say_something_r(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

say_something_r('Hi!', 'Mike', 'Nance')

name_tuple = ('Mike', 'Nancy')
say_something_r('Hi', *name_tuple)