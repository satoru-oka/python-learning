# class method, static method
def about(year):
    print('about human {}'.format(year))
class Person(object):
    name = 'satoru'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_name(cls):
        return cls.name

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.what_is_your_name()) # satoru
print(a.x) # 100
print(Person.name) # satoru
print(Person.what_is_your_name()) # satoru

Person.about(2023) # about human 2023
about(2023) # about human 2023