class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine method

# Example usage
engine = Engine()
car = Car(engine)

print(car.start_car())
