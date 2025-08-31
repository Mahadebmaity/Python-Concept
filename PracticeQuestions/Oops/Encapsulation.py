# 4. Encapsulation
# Create a BankAccount class with private attributes __balance. Add methods to:

# Deposit money.

# Withdraw money (check for insufficient balance).

# Show balance.

# Demonstrate that __balance can’t be accessed directly.

class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def get_balance(self):
        # A method to safely access the private balance if needed
        return self.__balance

account = BankAccount(1000)
# account.show_balance()
account.deposit(500)
# account.show_balance()
account.withdraw(300)
# account.show_balance()


# testing 
# Try to access private variable directly
# try:
    # print(account.__balance)
# except AttributeError as e:
    # print("Error:", e)  # Demonstrates that __balance is private

# Access using name mangling (not recommended, just for learning)
# print("Accessing private variable with name mangling:", account._BankAccount__balance)
# print(account._BankAccount__balance)

