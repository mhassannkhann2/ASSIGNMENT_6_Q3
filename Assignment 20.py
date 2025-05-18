# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 20. Creating a Custom Exception

# Assignment 20:

# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# SOLUTION:

class InvalidAgeError(Exception):
    def __init__(self, age, message="\n🚫 Age must be 18 or older!"):
        self.age = age  # Store the invalid age
        self.message = message  # Store the error message
        super().__init__(self.message)  # Call parent constructor

# 🔍 Function to check age eligibility
def check_age(age):
    """Check if the provided age is valid."""
    if age < 18:
        raise InvalidAgeError(age)  # Raise custom exception
    else:
        print(f"\n ✅ Age {age} is valid. You meet the age requirement!")

# 🎉 Example Usage 🎉
print("\n 🎭 Welcome to the Age Verification System! 🎭")
print("\n Ensure age eligibility using custom exceptions. 🚀\n")

try:
    # 🧐 Get user input for age
    age = int(input("\n🔢 Enter your age: "))

    # Call the check_age function
    check_age(age)

except InvalidAgeError as e:
    # Handle the custom exception if the age is invalid
    print(f"\n❌ Invalid age: {e.age}. {e.message}")

except ValueError:
    # Handle cases where the input isn't a valid number
    print("\n⚠️ Please enter a valid number for age.")

# ------------------ Assignment 20 Completed -----------------