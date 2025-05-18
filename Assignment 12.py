# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 12. Static Methods

# Assignment 12 :

# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

# 🌡️ Welcome to the Temperature Converter! 🌡️
# This program helps you convert Celsius to Fahrenheit using a simple formula.

# SOLUTION :

class TemperatureConverter:
    """
    A class with a static method to convert Celsius to Fahrenheit.
    No need to create an instance—just call the method directly!
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit using the formula: (C × 9/5) + 32"""
        return (celsius * 9/5) + 32

# 🎉 Example 🎉
print("\n 🔥Welcome to Temperature Converter 🔥")
print("\n Convert Celsius to Fahrenheit with ease!\n")

# User-defined Celsius temperature
celsius_value = 30  # You can change this to any value you like!

# Convert Celsius to Fahrenheit using the class method
fahrenheit_value = TemperatureConverter.celsius_to_fahrenheit(celsius_value)

# Display the result with emojis 😎
print(f"\n 🌡️ {celsius_value}°C is equal to {fahrenheit_value}°F 🌟")

# 🎯 Enjoy your temperature conversions! 🎯

# --------------- ASSIGNMENT 12 ENDS HERE ---------------

