# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 3. Public Variables and Methods

# Assignment 3 :

# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.

# SOLUTION :

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
        print("\n 🚗 Welcome! Your car has been created successfully!")

    def start(self):  # Public method
        print(f"\n 🔑 {self.brand} car is starting... 🏁")

# Example
my_car = Car("Carola")  # Creating an instance of the Car class

# Accessing public variable
print("\n 🛠️  Car Brand 🚗 :", my_car.brand)

# Calling public method
my_car.start()

# ------------- Assignment 3 End -------------


