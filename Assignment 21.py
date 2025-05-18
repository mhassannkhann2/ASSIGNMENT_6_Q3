# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 21. Make a Custom Class Iterable

# Assignment 21:

# Create a class Countdown that takes a start number.
# Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# SOLUTION:

class Countdown:

    def __init__(self, start):
        """Initialize the countdown with a starting number."""
        self.start = start  # Store the starting number
        self.current = start  # Set the current countdown value

    def __iter__(self):
    
        return self

    def __next__(self):
        
        if self.current <= 0:
            raise StopIteration  # Stop the iteration when reaching 0
        else:
            self.current -= 1  # Decrease the countdown value
            return self.current  # Return the updated countdown value

# 🎉 Example Usage 🎉
print("\n ⏳ Welcome to the Python Countdown Iterator! ⏳")
print("\n Watch the numbers count down dynamically. 🚀\n")

# Create an instance of Countdown with a starting value of 5
countdown = Countdown(5)

# Loop through the countdown iterator and print each number
print("\n📉 Starting countdown:")
for number in countdown:
    print(f"⏳ {number}")  # Display countdown numbers with emojis

print("\n🎯 Countdown complete! 🎯")

# ----------------- Assignment 21 Completed -----------------

