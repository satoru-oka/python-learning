# class inheritance
class Car(object):
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):
    def auto_run(self):
        print('auto run')

car = Car()
car.run()
print('toyota car ->>>')
toyota_car = ToyotaCar()
toyota_car.run()
print('tesla car ->>>')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()