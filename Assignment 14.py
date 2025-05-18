# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 14. Aggregation

# Assignment 14:

# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

# SOLUTION :

# 👋 Welcome to the Employee & Department Manager! 👋
# This program helps organize employees within departments using object-oriented programming.

class Employee:
    """
    Represents an employee in a company.

    Attributes:
        name (str): The employee's name.
        position (str): The employee's job title.
    """
    def __init__(self, name, position):
        self.name = name  # Store employee name
        self.position = position  # Store employee position

    def get_employee_details(self):
        """
        Retrieves employee details.
        Returns a formatted string containing the employee's name and position.
        """
        return f"\n 👤 Name: {self.name}, 🏢 Position: {self.position}"

class Department:
    
    def __init__(self, dept_name):
        self.dept_name = dept_name  # Store department name
        self.employees = []  # Initialize an empty list of employees

    def add_employee(self, employee):
        """
        Adds an Employee object to the department.
        """
        self.employees.append(employee)
        print(f"\n✅ {employee.name} has been added to the {self.dept_name} department!")

    def get_department_info(self):
        """
        Retrieves department details along with its employees.
        Returns a formatted string displaying all employees in the department.
        """
        employee_info = [emp.get_employee_details() for emp in self.employees]
        return f"\n 🏢 Department: {self.dept_name}\n👥 Employees:\n" + "\n".join(employee_info)

# 🎉 Example Usage 🎉
print("\n 🏢 Welcome to the Employee & Department Management System! 🏢")
print("\n Organize and track employees efficiently. 🚀\n")

# Create Employee instances
emp1 = Employee("hassan", "Manager")
emp2 = Employee("khan", "Engineer")

# Create a Department instance and add employees
dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

# Display department information
print("\n📋 Department Details 📋")
print(dept.get_department_info()) 

# --------------- ASSIGNMENT 14 ENDS HERE ---------------
