# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 13. Composition

# Assignment 13:

# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

# SOLUTION :

# 🚗 Welcome to the Car Engine Simulator! 🚗
# This program demonstrates how a car's engine starts using object-oriented programming.

class Engine:
    """
    Represents a car engine.
    
    Attributes:
        engine_type (str): The type of engine, e.g., 'V8', 'Electric', etc.
    """
    def __init__(self, engine_type):
        self.engine_type = engine_type  # Store engine type

    def start_engine(self):
        """Simulates starting the engine and returns a status message."""
        return f"\n 🚀 The {self.engine_type} engine is now running! 🔥"

class Car:
    """
    Represents a car that contains an engine.
    
    Attributes:
        make (str): Car manufacturer, e.g., 'Ford', 'Tesla'.
        model (str): Car model, e.g., 'Mustang', 'Model S'.
        engine (Engine): An instance of the Engine class.
    """
    def __init__(self, make, model, engine):
        self.make = make  # Store car make
        self.model = model  # Store car model
        self.engine = engine  # Composition: Car contains an Engine object

    def start_car(self):
        """
        Starts the car by triggering the Engine's start method.
        Returns a message indicating the car has started.
        """
        return f"\n 🚗 {self.make} {self.model}: {self.engine.start_engine()} ✅"

# 🎉 Example Usage 🎉
print("\n 🏎️   Welcome to the Car Engine Simulator! 🏎️")
print("\n Experience the thrill of starting your car! 🚗💨\n")

# Create an engine instance
engine = Engine("V8")  # You can change this to 'Electric', 'Hybrid', etc.

# Create a car instance with the engine
car = Car("Ford", "Mustang", engine)

# Start the car and display the result
print(car.start_car())  # Output: 🚗 Ford Mustang: 🚀 The V8 engine is now running! 🔥

# 🎯 Enjoy the ride! 🎯

# ----------------- Assignment 13 Completed -----------------