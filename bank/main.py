class BankAccount:
    def __init__(self, name: str, pin: int, balance: int) -> None:
        self.name = name
        self.pin = pin
        self.__balance = balance

    def check_balance(self) -> str:
        return f"\nYour balance is {self.__balance}"

    def deposit(self, amount: int) -> str:
        if amount < 1:
            return "\nInvalid amount"
        self.__balance += amount
        return f"\n{amount} deposited successfully. Your new balance is {self.__balance}\n"

    def withdraw(self, amount: int) -> str:
        if amount > self.__balance:
            return f"\nInsufficient funds! Your balance is {self.__balance}\n"
        self.__balance -= amount
        return f"\n{amount} withdrawn successfully. New balance: {self.__balance}\n"


class Person(BankAccount):
    def __init__(self, name: str, pin: int, balance: int) -> None:
        super().__init__(name, pin, balance)


users: list[Person] = [
    Person("Abdullah", 1111, 100000),
    Person("Rohan", 2222, 20000),
    Person("Uzair", 3333, 80000),
    Person("Sufyan", 4444, 60000)
]

actions: list[str] = ["Exit the program", "Check Balance", "Deposit", "Withdraw"]

def main() -> None:
    print("\n<---Welcome to ABD Bank--->")
    print("Please enter your name and pin to continue.\n")

    while True:
        user_name: str = input("Enter your name: ")
        try:
            user_pin: int = int(input("Enter your 4 digit pin: "))
        except ValueError:
            print("\nInvalid input. Pin must be a 4-digit number.\n")
            continue

        matched_user = None
        for user in users:
            if user.name == user_name and user.pin == user_pin:
                matched_user = user
                break

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
                print("\nThank you for banking with us. Goodbye!\n")
                return
            elif choice == 1:
                print(matched_user.check_balance())
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
