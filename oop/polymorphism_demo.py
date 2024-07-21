import math

# Base Class - Shape
class Shape:
    """A class to represent a generic shape."""

    def area(self):
        """Method to calculate the area of the shape. To be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement this method")

# Derived Class - Rectangle
class Rectangle(Shape):
    """A class to represent a rectangle."""

    def __init__(self, length, width):
        """Initialize the Rectangle instance."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    """A class to represent a circle."""

    def __init__(self, radius):
        """Initialize the Circle instance."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
