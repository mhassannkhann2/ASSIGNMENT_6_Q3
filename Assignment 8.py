# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 8. The super() Function

# Assignment 8 :

# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# SOLUTION :

class Person:
    def __init__(self, name):
        self.name = name  # 👤 Public attribute for the person's name
        print(f"\n 👋 Welcome! Person initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # 🧬 Call the constructor of the parent (Person) class
        self.subject = subject  # 📘 Subject the teacher teaches
        print(f"\n 🎓 Teacher {self.name} teaches 📚 {self.subject}")

# 🚀 Example usage
print("\n 🏫  Creating a new Teacher profile...")
t1 = Teacher("Mr hassan", "English")

# ----------------- ASSIGNMENT 8 ENDS HERE -----------------