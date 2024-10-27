class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def operation(self):
        print("Rides on the road")

class Flight:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def operation(self):
        print("flies on the sky")

p1_car = Car("BMW", "white")
p2_fli = Flight("Indigo", "blue")
for i in (p1_car, p2_fli):
    i.operation()