from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method, no implementation

# Rectangle class that implements area
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create a Rectangle object and calculate area
rect = Rectangle(5, 10)
print("Area of Rectangle:", rect.area())
