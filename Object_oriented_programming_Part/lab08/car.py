class Car(object):
    num_wheels = 4  # attribute
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        # attribute = input_arg
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    # inside_function / outside_method
    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return self.make + ' ' + self.model + ' cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):  # 爆胎
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return self.make + ' ' + self.model + ' gas level: ' + str(self.gas)


# Construct Start
hilfingers_car = Car('Tesla', 'Model S')
# Construct End
# Use Construct to express Attribution
r = hilfingers_car.color
print(r)
print('No color yet. You need to paint me.')
r = hilfingers_car.paint('black')
print(r)
print('Tesla Model S is now black')
r = hilfingers_car.color
print(r)
print('black')
r = hilfingers_car.model
print(r)
print('Model S')
hilfingers_car.gas = 10
r = hilfingers_car.drive()
print(r)
r = hilfingers_car.fill_gas()
print(r, 'Tesla Model S gas level: 20')
r = hilfingers_car.gas
print(r, 20)
r = Car.gas  # 初始化的值
print(r, 30)
print(Car.headlights, 2)
print(hilfingers_car.headlights, 2)
Car.headlights = 3
print(hilfingers_car.headlights, 3)
hilfingers_car.headlights = 2
print(Car.headlights, 3)
hilfingers_car.wheels = 2
print(hilfingers_car.drive())
# r = Car.drive()
# print(r) TypeError: drive() missing 1 required positional argument: 'self'
print(Car.drive(hilfingers_car))
