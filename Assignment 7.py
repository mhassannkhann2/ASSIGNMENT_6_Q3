# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 7. Access Modifiers: Public, Private, and Protected

# Assignment 7:

# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

# SOLUTION : 

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # 👨‍💼 Public: Can be accessed anywhere
        self._salary = salary     # 💼 Protected: Should be accessed within class or subclass (by convention)
        self.__ssn = ssn          # 🔒 Private: Not directly accessible (name mangling applies)

    def display(self):
        print("\n 📋 Employee Details:")
        print(f"🧑 Name: {self.name}")
        print(f"💰 Salary: {self._salary}")
        print(f"🔐 SSN: {self.__ssn}")

# 🚀 Creating an employee object
emp = Employee("hassan", 50000, "123-45-6789")

print("\n🔍 Accessing Attributes Outside the Class:")

# ✅ Accessing public variable
print("\n 🧑 Public Name:", emp.name)

# ⚠️ Accessing protected variable (allowed but not recommended)
print("\n 💼 Protected Salary:", emp._salary)

# ❌ Trying to access private variable (will raise an error)
try:
    print("🔒 Private SSN:", emp.__ssn)
except AttributeError as e:
    print("\n ❌ Private SSN Access Error:", e)

# ✅ Accessing private variable using name mangling
print("\n 🛠️  Accessing Private SSN via name mangling:", emp._Employee__ssn)

# ------------- ASSIGNMENT 7 ENDS HERE -------------