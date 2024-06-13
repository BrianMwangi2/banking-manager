class User:
    def __init__(self, user_id, name, balance=0.0):
        self.id = user_id
        self.name = name
        self.balance = balance

    def show_balance(self):
        print(f"Hello {self.name}, your balance is ${self.balance:.2f}")

    def deposit(self, amount):
        if amount < 0:
            print("Amount must be a positive number.")
            return
        self.balance += amount
        print(f"${amount:.2f} has been deposited into your account.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        if amount < 0:
            print("Amount must be a positive number.")
            return
        self.balance -= amount
        print(f"${amount:.2f} has been withdrawn from your account.")
