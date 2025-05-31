import random

input("Press enter to start.")

print("\n<<<---Welcome to the Cinephile Quotes, where every line spoken is a piece of cinematic gold--->>>")

movies_quotes = [
    "“I'm gonna make him an offer he can't refuse. ~ Vito Corleone” - 'The Godfather'",

    "“I think the only thing behind the mask is pain. ~ Batman” - The Dark Knight",

    "“Vengeance won't change the past, mine or anyone else's. I have to become more. People need hope. ~ Batman” - 'The Batman'",

    "“The hardest choices require the strongest wills. ~ Thanos” - 'Avengers: Infinity War'",

    "“When I was sixteen, I won a great victory. I felt in that moment I would live to be a hundred. Now I know I shall not see thirty. ~ Baldwin IV” - 'Kingdom of Heaven'",

    "“Hope is a good thing, maybe the best of thing and no good thing ever dies. ~ Stephen King” - 'The Shawshank Redemption'",
    
    "“The only thing we can count on is ourselves. ~ Cooper” - 'Interstellar'",
    
    "“Dreams feel real while we're in them. It's only when we wake up that we realize something was actually strange. ~ Dom Cobb” - 'Inception'",
    
    "“Our lives are defined by opportunities, even the ones we miss. ~ Benjamin Button” - 'Curious Case of Benjamin Button'",
    
    "“And they found you amusing for a while, the people of this city, but the one thing they love more then a hero... is to see a hero fail. ~ Green Goblin” - 'Spiderman'",

    "“Amateurs seeks the sun and get eaten. Power stays in the shadows. ~ Lewis Strauss” - 'Oppenheimer'",

    "“Pray for the best, prepare for the worst. ~ Detective Loki” - 'Prisoners'",

    "“It ain't about how hard you hit. It's about how hard you can get hit and keep moving forward. ~ Rocky” - 'Rocky Balboa'",
]

shows_quotes = [
     
    "“Every sacrifice we make needs to be for the greater good. ~ Rick Grimes” - 'The Walking Dead'",
    
    "“Everybody works for points. You work, you live. You don't work, well, you don't live. ~ Negan Smith” - 'The Walking Dead'",

    "“You either run from things, or you face them. ~ Jesse Pinkman” - 'Breaking Bad'",

    "“Sometimes, to get what you want, you have to do things you never thought you would.. ~ Thomas Shelby” - 'Peaky Blinders'",

    "“There's always a way. You just have to find it. ~ Michael Scofield” - 'Prison Break'",
    
    "“Power is only given to those who are prepared to lower themselves to pick it up. ~ Ragnar Lothbrok” - 'Vikings'",

    "“Alone is what I have. Alone protects me. ~ Sherlock Holmes” - 'Sherlock'",

    "“When you play the game of thrones, you win or you die. ~ Cersie Lannister” - 'Games Of Thrones'",
    
    "“The night is dark and full of terrors. ~ Melisandre” - 'Games Of Thrones'",
    
    "Chaos is a ladder, many who try to climb it fail and never get to try again. ~ Petyr Baelish” - 'Games Of Thrones'",
    
    "I wish i was the monster you think i am. ~ Tyrion Lannister” - 'Games Of Thrones'",

    
]

while True:
    print("\n1. Movies Quotes\n2. Shows Quotes\n3. Exit")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        print("\n", random.choice(movies_quotes))
        
    elif choice == 2:
        print("\n", random.choice(shows_quotes))
    
    elif choice == 3:
        print("\n“For me, this is the end of a beautiful friendship. ~ Neil” - 'Tenet'")
        break
    
    else:
        print("Invalid choice. Please try again.")