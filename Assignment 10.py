# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 10. Instance Methods

# Assignment 10:

# Create a class Dog with instance variables name and breed.
# Add an instance method bark() that prints a message including the dog's name.

# SOLUTION :

class Dog:
    def __init__(self, name, breed):
        self.name = name    # 🐕 Dog's name
        self.breed = breed  # 🧬 Dog's breed
        print(f"\n 🎉 A new dog named {self.name} ({self.breed}) has been added to the family! 🐾")

    def bark(self):
        # 🔊 Dog makes a barking sound
        print(f"\n 🐶 {self.name} says: Woof woof! 🗣️")

# 🚀 Example usage
print("\n 🐾 Welcome to the Dog House!")

# 🐶 Creating a dog object
dog1 = Dog("Max", "Golden Retriever")

# 🔊 Let the dog bark
dog1.bark()

# --------------- ASSIGNMENT 10 ENDS HERE ---------------

