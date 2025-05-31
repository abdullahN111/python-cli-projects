

while True:
    start = input("\nPress Enter to start or q to quit: ").lower()
    if start == "q":
        break
    
    print("\n<<<---Calculate your ideas--->>>")
    num1 = input("\nEnter first number: ")
    num2 = input("Enter second number: ")
    if not num1.isdigit() or not num2.isdigit():
        print("\nInvalid input! Please enter a valid number.")
        continue  

    num1 = int(num1)
    num2 = int(num2)
    operator = input("\nSelect operator (+, -, *, /): ")
    
    if operator == "+":
        result = num1 + num2
        print(f"\n{num1} + {num2} = {result}")
        
    elif operator == "-":
        result = num1 - num2
        print(f"\n{num1} - {num2} = {result}")
        
    elif operator == "*":
        result = num1 * num2
        print(f"\n{num1} * {num2} = {result}")
        
    elif operator == "/":
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
        
    else:
        print("\nInvalid operator! Try again.")
        