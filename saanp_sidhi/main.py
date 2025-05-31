import random


WIN_SCORE = 30

def main(): 
    print("\n<---Welcome to Saanp Sidhi Dice Game--->\n")
    
    user_score = 0
    computer_score = 0
    
    
    while True:
        
        
        print("\nRoll a dice..")
        user_input = input("Press enter to roll: ")
        
        computer = random.randint(1,7)
        user = random.randint(1,7)
        
        if user_input == "":
            
            
            print(f"\nYour Dice: {user}")
            print(f"Computer Dice: {computer}")
            
            user_score += user
            computer_score += computer
    
            print(f"\nYour Score: {user_score}, Computer Score: {computer_score}")
            
        if user_score >= WIN_SCORE:
            print("\nCongrats You have won..")
            print(f"\nYour Score: {user_score}, Computer Score: {computer_score}")
            break
            
        if computer_score >= WIN_SCORE:
            print("\nOops You have lost!")
            print(f"\nYour Score: {user_score}, Computer Score: {computer_score}")
            break
            
        if computer_score and user_score >= WIN_SCORE:
            print("\nThe game is a tie.")
            print(f"\nYour Score: {user_score}, Computer Score: {computer_score}")
            break
        
        
        
        

    
        



if __name__ == "__main__":
    main()