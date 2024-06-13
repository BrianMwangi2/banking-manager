#bank/cli

from lib.database import BankDatabase
from lib.user import User

class BankCLI:
    def __init__(self):
        self.db = BankDatabase()
        self.users = self.db.load_users()
        self.current_user = None

    def create_user(self, user_id):
        name = input("Enter your name: ")
        self.db.create_user(user_id, name)
        print("User account created successfully!")
        self.users = self.db.load_users()

    def run(self):
        while True:
            print("\nBanking program")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            user_id = input("Enter your user ID: ")
            if user_id not in self.users:
                create_new_account = input("User ID not found. Do you want to create a new account? (yes/no): ")
                if create_new_account.lower() == 'yes':
                    self.create_user(user_id)
                else:
                    print("Invalid user ID. Please try again or create a new account.")
                    continue

            user_data = self.db.get_user(user_id)
            self.current_user = User(user_data['id'], user_data['name'], user_data['balance'])
            print(f"Welcome, {self.current_user.name}!")

            while True:
                choice = input("Enter the service you want to be rendered (1-4): ")
                if choice == '1':
                    self.current_user.show_balance()
                elif choice == '2':
                    amount = float(input("Enter the amount to be deposited: "))
                    self.current_user.deposit(amount)
                    self.db.update_balance(self.current_user.id, self.current_user.balance)
                elif choice == '3':
                    amount = float(input("Enter the amount to be withdrawn: "))
                    self.current_user.withdraw(amount)
                    self.db.update_balance(self.current_user.id, self.current_user.balance)
                elif choice == '4':
                    print("Thank you for using our services , Have a lovely day!")
                    return
                else:
                    print("Invalid choice")

if __name__ == "__main__":
    BankCLI().run()
