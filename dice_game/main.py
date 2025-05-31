import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4")
    else:
        print("Invalid number! Please try again")
            
max_score = 50
player_scores = [0 for _ in range(players)]
game_over = False
winner = None

while not game_over:
    for players_index in range(players):
        print(f"\nPlayer {players_index + 1} turn")
        print(f"Your total score is {player_scores[players_index]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Press enter to roll the dice: ")
            if should_roll != "":
                break
                
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
            
            print(f"Your current score is {current_score}")
        
        player_scores[players_index] += current_score
        print(f"Player {players_index + 1} score is {player_scores[players_index]}")

        if player_scores[players_index] >= max_score:
            game_over = True
            winner = players_index + 1
            break  
    if game_over:
        break

print(f"\nPlayer {winner} wins with {player_scores[winner - 1]} points!")
