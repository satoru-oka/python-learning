# class inheritance
class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self.enable_auto_run = enable_auto_run
    def run(self):
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
tesla_car = TeslaCar()
print(tesla_car.model) # Model S
print(tesla_car.enable_auto_run) # False
tesla_car.run()
tesla_car.auto_run()