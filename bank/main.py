from typing import List
import json

        
        
        
class BankAccount():
    def __init__(self, name: str, pin: int, balance: int) -> None:
        self.name = name
        self.pin = pin
        self.__balance = balance
        
        
    def get_balance(self) -> int:
        return self.__balance
    
    def show_balance(self) -> None:
        print(f"\nYour balance is {self.get_balance()}\n")
    
    def deposit(self, amount: int) -> str:
        if amount < 1:
            return "Invalid Amount\n"
        self.__balance += amount
        return f"\n{amount} deposited successfully. Your new balance is {self.get_balance()}\n"

    def withdraw(self, amount: int) -> str:
        if amount > self.get_balance():
            return "Low Balance! Please enter valid amount.\n"
        
        self.__balance -= amount
        return f"\n{amount} withdrawn successfully. New balance: {self.get_balance()}\n"
    
    
    
class Person(BankAccount):
    def __init__(self, name: str, pin: int, balance: int) -> None:
        super().__init__(name, pin, balance)

with open("users.json", "r") as file:
    users_data = json.load(file)

users: List[Person] = [
  Person(user['name'], user['pin'], user['balance']) for user in users_data
]


actions: list[str] = ["Exit the program", "Check Balance", "Deposit", "Withdraw"]

def main() -> None:
    print("\n<---Welcome to ABD Bank--->")
    print("\n>>> Please enter your name and pin to continue.\n")
    
    matched_user = None
    condition = True
    while condition:
        
        user_name: str = input("Enter your name: ")
        try:
            user_pin: int = int(input("Enter your 4 digit pin: "))
        except ValueError:
            print("\nInvalid input. Pin must be a 4-digit number.\n")
            continue
        
        for user in users:
            if user_name ==  user.name and user_pin == user.pin:
                matched_user = user
                condition = False
                
        if not matched_user:
            print("\nInvalid name or pin.\n")
            continue
        
        
        print(f"\nWelcome {matched_user.name}!\n")

        while True:
            for index, action in enumerate(actions):
                print(f"{index}. {action}")

            try:
                choice = int(input("\nSelect an action (0-3): "))
            except ValueError:
                print("\nInvalid input. Enter a number from 0 to 3.\n")
                continue

            if choice == 0:
                print("\nThank you for using our ATM. Goodbye!\n")
                return
            elif choice == 1:
                matched_user.show_balance()
            elif choice == 2:
                try:
                    amount = int(input("\nEnter amount to deposit: "))
                    print(matched_user.deposit(amount))
                except ValueError:
                    print("\nInvalid input. Amount must be a number.")
            elif choice == 3:
                try:
                    amount = int(input("\nEnter amount to withdraw: "))
                    print(matched_user.withdraw(amount))
                except ValueError:
                    print("\nInvalid input. Amount must be a number.")
            else:
                print("\nInvalid choice. Please select between 0 and 3.\n")


if __name__ == "__main__":
    main()