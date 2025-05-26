def add_greeting(cls):
    def greet(self):
        return "Hello from name ia junaid!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Alice")
print(p.greet())
