# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 1. Using self

# Assignment 1:

# Create a class Student with attributes name and marks. Use the self keyword to initialize these values
# via a constructor. Add a method display() that prints student details.

# SOLUTION 

# Define the Student class

class Student:
    def __init__(self, name, marks):
        self.name = name        # 🎓 Initialize name using self
        self.marks = marks      # 📚 Initialize marks using self

    def display(self):
        print("\n 👩‍🎓 Student Name:", self.name)
        print("\n 📈 Marks:", self.marks)

# Example usage

student1 = Student("Muhammad Hassan Khan", 95)
student1.display()

# ------------- Assignment 1 End -------------


