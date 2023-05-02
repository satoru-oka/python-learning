# class initialization and class variable(property)
class Person(object):
    # holds the value of its own class.
    # constructor
    def __init__(self, name):
        self.name = name
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)
    def run(self, num):
        print('run ' * num)
    #destructor
    def __del__(self):
        print('good bye')

person = Person('satoru')
person.say_something()
# del person
print("@@@@@@@@@@@@@@@")