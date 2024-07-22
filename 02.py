class Vehicle:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def move(self, arrow, meter):
        return f'{self.meter} to {self.arrow}'

class Bicycle(Vehicle):
    def __init__(self, wheel_count=2):
        super().__init__(wheel_count)

class Car(Vehicle):
    def __init__(self, wheel_count=4):
        super().__init__(wheel_count)

class Taxi(Car):
    def __init__(self, price_per_meter, wheel_count=4):
        super().__init__(wheel_count)
        self.price_per_meter = price_per_meter

    def move(self, arrow, meter):
        return f'{self.price_per_meter * meter} for {meter} to {arrow}'

class Truck(Vehicle):
    def __init__(self, wheel_count=10):
        super().__init__(wheel_count)


class Trailer(Vehicle):
    def __init__(self, wheel_count=18):
        super().__init__(wheel_count)

t1 = Taxi(10)
print(t1.move('left', 100))