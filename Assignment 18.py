# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 18. Property Decorators: @property, @setter, and @deleter

# Assignment 18:

# Create a class Product with a private attribute _price.
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# SOLUTION:

class Product:
    """
    Represents a product with a name and a price.
    
    Attributes:
        name (str): The name of the product.
        _price (float): Private attribute storing the product's price.
    """
    def __init__(self, name, price):
        self.name = name  # Store product name
        self._price = price  # Store price privately

    @property
    def price(self):
        """
        Getter for price.
        
        Returns the product's price when accessed.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Setter for price.
        
        Ensures price isn't set to a negative value.
        """
        if value < 0:
            print("\n❌ Price cannot be negative!")
        else:
            self._price = value
            print(f"\n✅ Price updated to: ${self._price}")

    @price.deleter
    def price(self):
        """
        Deleter for price.
        
        Deletes the price attribute while displaying a message.
        """
        print(f"\n🗑️  Deleting price of {self.name} is ${self._price} ...")
        del self._price

# 🎉 Example Usage 🎉
print("\n🛒 Welcome to the Python Product Management System! 🛒")
print("\nManage product prices dynamically using property decorators. 🚀\n")

# Create a Product instance
product = Product("Laptop", 500)

# Get the price using @property
print(f"\n💰 Price of {product.name}: ${product.price}")

# Update the price using @price.setter
product.price = 1000
print(f"\n💰 Updated price of {product.name}: ${product.price}")

# Try setting a negative price
product.price = -500  # Will trigger an error message ❌

# Delete the price using @price.deleter

del product.price  
# ------------ Assignment 18 Completed! 🎉 ------------

