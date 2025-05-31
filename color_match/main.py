import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
        
    return code


def guess_code():
    while True:
        guess = input("\nGuess: ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} code words!")
            continue
        
        for color in guess:
            if color not in COLORS:
                print("Invalid color! Try again.")
                break
        else:
            break
        
    return guess

def check_code(guess, code):
    color_counts = {}
    correct = 0
    incorrect = 0
    
    for color in code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        
        
    for guess_color, real_color in zip(guess, code):
        if guess_color == real_color:
            correct += 1
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess, code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect += 1
            color_counts[guess_color] -= 1
            
        
    return correct, incorrect


def main():
    print(f"\n<-Welcome to Mastermind. You have {TRIES} tries to guess the code->\n")
    print("The valid colors are: ", *COLORS)
    
    code = generate_code()
    
    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct, incorrect = check_code(guess, code)
        
        if correct == CODE_LENGTH:
            print(f"You guessed the code in {attempt} attempts.")
            break
        
        print(f"\nCorrect Positions: {correct}")
        print(f"Incorrect Positions: {incorrect}\n")
        
    else:
        print("\nYou ran out of tries! The code was", *code)
            
            
if __name__ == "__main__":
    main()