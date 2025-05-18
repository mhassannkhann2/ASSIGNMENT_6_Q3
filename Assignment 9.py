# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 9. Abstract Classes and Methods

# Assignment 9:

# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

# SOLUTION :

from abc import ABC, abstractmethod

# 🧱 Abstract base class for all shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        # 📏 Abstract method that must be implemented by all subclasses
        pass

# 🟥 Rectangle class that implements the Shape interface
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width      # ↔️ Width of the rectangle
        self.height = height    # ↕️ Height of the rectangle
        print("\n 🆕 Rectangle created! ✅")

    def area(self):
        # 📐 Calculate and return area of rectangle
        return self.width * self.height

# 🚀 Example usage
print("\n 🎉 Welcome to the Shape Calculator!")

# 🔨 Creating a rectangle object
rect = Rectangle(2, 8)

# 📊 Calculating and displaying the area
print("\n 📏 Area of the rectangle:", rect.area(), "sq units")

# ----------------- ASSIGNMENT 9 ENDS HERE -----------------

