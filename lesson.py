# duck typing
import abc
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    @abc.abstractmethod
    def drive(self):
        pass
class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        raise Exception('No drive')
class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError
    def drive(self):
        print('ok')

baby = Baby()
# baby.drive()
adult = Adult()
adult.drive()
class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        # self.enable_auto_run = enable_auto_run # freely rewritable
        self._enable_auto_run = enable_auto_run # explicit access
        # self.__enable_auto_run = enable_auto_run # own class access
        self.passwd = passwd

    @property
    def enabel_auto_run(self):
        return self._enable_auto_run

    @enabel_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError
    def run(self):
        # print(self.__enable_auto_run) # own class access
        print('super fast') # override
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('toyota car ->>>')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model) # Lexus
toyota_car.run()
print('tesla car ->>>')
tesla_car = TeslaCar('model m', passwd='456')
tesla_car.enable_auto_run = True
print(tesla_car.model) # model m
print(tesla_car._enable_auto_run) # True
tesla_car.run() # super fast
tesla_car.auto_run() # auto run

# attention