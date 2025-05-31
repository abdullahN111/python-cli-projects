name = input("\nEnter your name: ")
print(f"Welcome to this adventure {name}!\n")


print("You are on a dirt road, it has come to an end and you can go left or right.\n")
answer = input("Which way would you like to go? ").lower()

if answer == "left":
    print("You come to a river, you can walk around it or swim across.\n")
    answer = input("Which way would you like to go. Choose walk or swim? ").lower()
    
    if answer == "swim":
        print("You swam across and were eaten by alligator. Game over!\n")
    elif answer == "walk":
        print("You walked for many miles and ran out of water but somehow you managed to survived and won!\n")
        
    else:
        print("Not a valid option. You lose!")
    
elif answer == "right":
    print("You come to a bridge, it looks wobbly.\n")
    answer = input("Do you want to cross it or headback?. Choose cross or back? ").lower()
    
    
    if answer == "cross":
        print("You cross the bridge and meet a stranger.\n")
        answer = input("Do you want to talk to them?. Choose yes or no? ").lower()
        if answer == "yes":
                print("You talk to stranger and and they give you gold. You win!\n")
        elif answer == "no":
                print("You ignored the stranger and they get offended. You lose!\n")
        else:
                print("Not a valid option. You lose!")
        

        
    elif answer == "back":
        print("You go back and lose!\n")
        
    else:
        print("Not a valid option. You lose!")

else:
    print("Not a valid option. You lose!")
    