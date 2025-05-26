
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")

# Create a Car object outside the class definition
my_car = Car("Calola")
print(my_car.brand)

