# class definition
class Person(object):
    # holds the value of its own class.
    def __init__(self, name):
        self.name = name
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)
    def run(self, num):
        print('run ' * num)

person = Person('satoru')
person.say_something()