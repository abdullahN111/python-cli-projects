
acc_data: list = [
    {
        "username": "abdullah",
        "pin": 1111,
        "balance": 100000
    },
    {
        "username": "uzair",
        "pin": 2222,
        "balance": 80000
    },
    {
        "username": "sufyan",
        "pin": 3333,
        "balance": 60000
    },
]

options = ["Withdraw Money", "Check Balance", "Exit"]


def action(balance: int) -> None:
    print("\nSelect an option or press 3 to quit\n")
    for index, option in enumerate(options):
        print(f"{index+1}. {option}")
    while True:
        action: str = input("\nWhat do you want to do? 1 for withdraw, 2 for balance, 3 for exit: ").lower()
    
        if action == "1":
            try:
                amount: int = int(input("Enter amount to withdraw: "))
                
            except Exception as e:
                print(f"Error {e}")
                
            if amount <= balance:
                balance -= amount
                print(f"\nYou have withdrawed {amount} successfully. Your remaining balance is {balance}.")
                continue
            
            else:
                print("\nInsufficient balance!")
                continue
        
        elif action == "2":
            print(f"\nYour balance is {balance}")
            
        elif action == "3":
            print("\n---Thanks for using Demo ATM---")
            exit()
            
        else:
            print("\nInvalid input!")


def main() -> None:
    print("\n---Welcome to Demo Bank ATM---")
    while True:
        try:
            user: str = input("\nPlease enter your username: ").lower()
                    
        except Exception as e:
            print("Error: ", e)
            
        try:
            pin: int = int(input("Please enter your 4-digit pin: "))
            
        except:
            print("\nPin should only contain digits!")
            continue
        
        for account in acc_data:
            
            if user == account["username"] and pin == account["pin"]:
                    print(f"\nWelcome {account["username"].upper()}")
                    action(account["balance"])
                    break
        else:
            print("\nInvalid username or pin!")
            
            
        
main()