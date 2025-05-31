

my_balance = 1000000
my_pin = 1122

print("\n---Welcome to Demo Bank ATM---\n")

while True:
    try:
        pin = int(input("Enter your 4-digit PIN: "))
    except ValueError:
        print("\nInvalid input! Please enter numbers only.\n")
        continue

    if pin != my_pin:
        print("\nInvalid PIN!\n")
        continue

            
    print("\nWhat do you want to do? Type withdraw(w) or balance(b)")
    options = input("Withdraw Cash or Check Balance: ").lower()
        
    if options == "withdraw" or options == "w":    
        try:
            amount = int(input("\nEnter amount to withdraw: "))
            if amount > 0 and amount <= my_balance:
                my_balance -= amount
                print(f"\n{amount} withdraw successfully.")
                print(f"Your remaining balance is {my_balance}\n")
            else:
                print("\nInvalid amount! Check your balance or enter a valid number.\n")
        except ValueError:
                    print("\nInvalid input! Please enter numbers only.\n")
        if options == "balance" or options == "b":
            my_balance = my_balance
            print(f"\nYou Have ${my_balance} in your account.")
    
    elif options == "balance" or options == "b":
        print(f"\nYou Have ${my_balance} in your account.")

    else:
        print("\nInvalid option! Please choose again.\n")
        continue
    
    choice = input("\nDo you want to continue? Type 'quit' to exit or Press Enter to continue: ").lower()
    if choice == "quit":
        print("\nThank you for using Demo Bank ATM. Have a nice day!\n")
        break
    if choice == "":
        continue

    break
        

