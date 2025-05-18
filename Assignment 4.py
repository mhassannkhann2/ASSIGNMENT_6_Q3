# Project # 06 Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series

# Created By Hassan Khan

# 4. Class Variables and Class Methods

# Assignment 4:

class Bank:
    bank_name = "HBL "  # 🏦 Class-level bank name shared by all customers

    def __init__(self, customer_name):
        self.customer_name = customer_name  # 🧑‍💼 Each customer has their own name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = f"🏦 {name}"  # 🔄 Update shared bank name using class method

    def display(self):
        # 📋 Show customer info along with current bank name
        print(f"\n 👤 Customer: {self.customer_name} |  Bank: {Bank.bank_name}")

# 🚀 Example 
print("\n 🎉 Welcome to our banking system 🏦 !")

# ✨ Creating customer accounts
c1 = Bank("Hassan")
c2 = Bank("Samad")

# 🕰️ Before changing bank name
print("\n🔍 Showing details before bank name change:")
c1.display()
c2.display()

# 🔧 Changing bank name
Bank.change_bank_name("National Bank Of Pakistan ")

# 🆕 After changing bank name
print("\n✅ Showing updated details after bank name change:")
c1.display()
c2.display()

# ------------- Assignment 4 End -------------