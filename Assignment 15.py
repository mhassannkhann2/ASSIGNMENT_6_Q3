# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 15. Method Resolution Order (MRO) and Diamond Inheritance

# Assignment 15 :

# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

# SOLUTION :

# 👋 Welcome to the Python Inheritance & MRO Demonstration! 👋
# This program showcases method overriding and the Method Resolution Order (MRO) in Python.

class A:
    """
    Base class A.
    
    Contains a method 'show' that prints a message from class A.
    """
    def show(self):
        print("\n🔹 Method from class A")

class B(A):
    """
    Class B inherits from class A.
    
    Overrides the 'show' method with a unique message.
    """
    def show(self):
        print("\n🔹 Method from class B")

class C(A):
    """
    Class C also inherits from class A.
    
    Overrides the 'show' method with a different message.
    """
    def show(self):
        print("\n 🔹 Method from class C")

class D(B, C):
    """
    Class D inherits from both B and C using multiple inheritance.

    Python uses the Method Resolution Order (MRO) to determine which 'show' method gets called.
    """
    pass  # No new method, so it follows MRO

# 🎉 Example Usage 🎉
print("\n 🐍 Welcome to the Python Inheritance & MRO Demonstration! 🐍")
print("\n Understand how Python resolves methods in multiple inheritance. 🔍\n")

# Create an instance of class D
d = D()

# Call the 'show' method of D, following MRO rules
print("\n🚀 Calling the 'show' method of D:")
d.show()  # Output will follow Python's MRO

# Print the Method Resolution Order (MRO) for class D
print("\n🔍 Method Resolution Order (MRO) for D:")
print(D.__mro__) 

# -------------------- Assignment 15 Completed --------------------
