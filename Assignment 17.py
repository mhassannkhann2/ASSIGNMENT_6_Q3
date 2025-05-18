# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 17. Class Decorators

# Assignment 17 :

# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". 
# Apply it to a class Person.

# SOLUTION :
# 👋 Welcome to the Python Class Decorator Demonstration! 👋
# This program showcases how class decorators dynamically modify class behavior.

def add_greeting(cls):
    """
    A class decorator that adds a 'greet' method to the decorated class.

    The added method allows instances of the class to return a greeting message.
    """
    def greet(self):
        return "\n🌟 Hello from the Decorator! 🌟"  # Custom greeting message
    
    # Add the 'greet' method to the class
    cls.greet = greet
    return cls

# 🏷️ Applying the decorator to the Person class
@add_greeting
class Person:
    """
    Represents a person with a name.
    
    Attributes:
        name (str): The person's name.
    """
    def __init__(self, name):
        self.name = name  # Store person's name

# 🎉 Example

print("\n 🎭 Welcome to the Class Decorator Showcase! 🎭")
print("\n Enhance classes dynamically with decorators. 🚀\n")

# Create an instance of the decorated Person class
person = Person("Hassan")

# Call the dynamically added 'greet' method
print("\n ✅ Calling the 'greet' method on Person instance:")
print(person.greet())  # Output: 🌟 Hello from the Decorator! 🌟

# ----------------- Assignment 17 Completed! -----------------