
def kbc_game():
    print("\n<<<---Welcome to the hot seat of Kon Banega Crorepati--->>>\n")

    start = input("You finally here at the Hot seat of KBC, can we start the game? (yes/no): ").strip().lower() 
    
    if start == "no":
        print("Maybe next time!")
        return

    questions = [
    {"question": "Which year did Pakistan gain independence?",
     "options": ["A) 1945", "B) 1947", "C) 1950", "D) 1952"],
     "answer": "B",
     "money": 1000},

    {"question": "Which one is the National flower of Pakistan?",
     "options": ["A) Jasmine", "B) Rose", "C) Lotus", "D) Sunflower"],
     "answer": "A",
     "money": 2000},

    {"question": "Which Pakistani city is known as the City of Lights?",
     "options": ["A) Lahore", "B) Quetta", "C) Islamabad", "D) Karachi"],
     "answer": "D",
     "money": 4000},

    {"question": "When did Pakistan win their first ever Cricket World Cup?",
     "options": ["A) 2009", "B) 2007", "C) 1992", "D) 1999"],
     "answer": "C",
     "money": 8000},

    {"question": "Who was the first Prime Minister of Pakistan?",
     "options": ["A) Liaquat Ali Khan", "B) Ayub Khan", "C) Zulfikar Ali Bhutto", "D) Benazir Bhutto"],
     "answer": "A",
     "money": 16000},

    {"question": "What is the largest province of Pakistan by area?",
     "options": ["A) Punjab", "B) Sindh", "C) Balochistan", "D) Khyber Pakhtunkhwa"],
     "answer": "C",
     "money": 32000},

    {"question": "Which river is the longest in Pakistan?",
     "options": ["A) Jhelum", "B) Chenab", "C) Ravi", "D) Indus"],
     "answer": "D",
     "money": 64000},

    {"question": "Who wrote the national anthem of Pakistan?",
     "options": ["A) Allama Iqbal", "B) Hafeez Jalandhari", "C) Faiz Ahmed Faiz", "D) Ahmad Faraz"],
     "answer": "B",
     "money": 125000},

    {"question": "Which mountain is the highest peak in Pakistan?",
     "options": ["A) Nanga Parbat", "B) Rakaposhi", "C) K2", "D) Tirich Mir"],
     "answer": "C",
     "money": 250000},

    {"question": "Who is known as the Father of Pakistan's Nuclear Program?",
     "options": ["A) Abdul Qadeer Khan", "B) Dr. Abdus Salam", "C) Zulfikar Ali Bhutto", "D) Munir Ahmad Khan"],
     "answer": "A",
     "money": 500000}
]


    earnings = 0

    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if user_answer == q["answer"]:
            earnings = q["money"]
            print("\nCorrect answer!")
            print(f"You've won {earnings} rupees!!!\n")
        else:
            print(f"\nWrong answer! The correct answer was {q['answer']}.")
            print(f"You won {earnings} rupees in total.")
            break

    print("\nGame Over! Thanks for playing.")


kbc_game()
