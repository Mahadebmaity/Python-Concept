from abc import ABC, abstractmethod
import random

# Abstract Class for Payment
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Classes for Different Payment Methods
class CreditCard(PaymentMethod):
    def pay(self, amount):
        transaction_id = f"TXN{random.randint(100000, 999999)}"
        print(f"✅ Paid ₹{amount} using Credit Card. Transaction ID: {transaction_id}")
        return ("Credit Card", transaction_id)

class PayPal(PaymentMethod):
    def pay(self, amount):
        transaction_id = f"TXN{random.randint(100000, 999999)}"
        print(f"✅ Paid ₹{amount} using PayPal. Transaction ID: {transaction_id}")
        return ("PayPal", transaction_id)

class UPI(PaymentMethod):
    def pay(self, amount):
        transaction_id = f"TXN{random.randint(100000, 999999)}"
        print(f"✅ Paid ₹{amount} using UPI. Transaction ID: {transaction_id}")
        return ("UPI", transaction_id)

# BankAccount Class with Private Balance
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ ₹{amount} deposited successfully.")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ ₹{amount} withdrawn successfully.")
        else:
            print("❌ Insufficient balance.")

    def show_balance(self):
        print(f"💰 Current Balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

    def deduct(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

# Make Payment Function
def make_payment(payment_method, amount, account):
    if account.deduct(amount):
        return payment_method.pay(amount)
    else:
        print("❌ Payment failed due to insufficient balance.")
        return None

# Main System
def main():
    account = BankAccount(1000)
    last_transaction = None
    transaction_history = []

    while True:
        print("\n====== 💳 Payment System Menu ======")
        print("1. Make a Payment")
        print("2. Deposit Money")
        print("3. Show Balance")
        print("4. View Last Transaction")
        print("5. Withdraw Money")
        print("6. View All Transactions")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            print("\nSelect Payment Method:")
            print("a. Credit Card")
            print("b. PayPal")
            print("c. UPI")
            method = input("Enter method (a/b/c): ")
            amount = float(input("Enter amount to pay: ₹"))

            if method == 'a':
                result = make_payment(CreditCard(), amount, account)
            elif method == 'b':
                result = make_payment(PayPal(), amount, account)
            elif method == 'c':
                result = make_payment(UPI(), amount, account)
            else:
                print("❌ Invalid payment method.")
                result = None

            if result:
                last_transaction = result
                transaction_history.append(result)

        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)

        elif choice == '3':
            account.show_balance()

        elif choice == '4':
            if last_transaction:
                print(f"📌 Last Transaction — Method: {last_transaction[0]}, Transaction ID: {last_transaction[1]}")
            else:
                print("ℹ️ No transaction made yet.")

        elif choice == '5':
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)

        elif choice == '6':
            if transaction_history:
                print("\n📜 All Transactions This Month:")
                for idx, txn in enumerate(transaction_history, start=1):
                    print(f"{idx}. Method: {txn[0]} | Transaction ID: {txn[1]}")
            else:
                print("ℹ️ No transactions made yet.")

        elif choice == '7':
            print("👋 Exiting the system. Thank you!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# Run the Program
if __name__ == "__main__":
    main()
