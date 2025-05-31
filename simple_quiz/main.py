print(f"\n<<<---Welcome to Quiz Game--->>>\n")

questions = [
    {
        "question": "What is the keyword used to define a function in Python?",
        "answers": "A"
    },
    {
        "question": "Which data type is **immutable** in Python?",
        "answers": "B"
    },
    {
        "question": "How do you print a message in Python?",
        "answers": "C"
    },
    {
        "question": "Which of the following is used for comments in Python?",
        "answers": "D"
    },
    {
        "question": "What is the output of `len([1, 2, 3, 4])`?",
        "answers": "A"
    },
    {
        "question": "Which loop is used when the number of iterations is unknown?",
        "answers": "B"
    },
    {
        "question": "Which function is used to take user input in Python?",
        "answers": "C"
    },
    {
        "question": "Which of the following is used to handle exceptions in Python?",
        "answers": "D"
    },
    {
        "question": "What will `type(10.5)` return?",
        "answers": "A"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "answers": "B"
    }
]

options = [
    ["A. def", "B. func", "C. function", "D. define"],
    ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
    ["A. echo('Hello')", "B. console.log('Hello')", "C. print('Hello')", "D. display('Hello')"],
    ["A. //", "B. /* */", "C. <!-- -->", "D. #"],
    ["A. 4", "B. 3", "C. 5", "D. Error"],
    ["A. for loop", "B. while loop", "C. do-while loop", "D. switch-case"],
    ["A. get_input()", "B. scan()", "C. input()", "D. read()"],
    ["A. try-do", "B. catch-except", "C. error-handle", "D. try-except"],
    ["A. <class 'float'>", "B. <class 'int'>", "C. <class 'double'>", "D. <class 'decimal'>"],
    ["A. ^", "B. **", "C. //", "D. %"]
]


score = 0

def check_answer(user_guessed, correct_answer):
    if user_guessed == correct_answer:
        return True
    else:
        return False

for question_num in range(len(questions)):
    print("\n************************\n")
    print(questions[question_num]["question"])
    
    for i in options[question_num]:
        print(i)
        
        
    guess = input("Enter your answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess, questions[question_num]["answers"])
    
    if is_correct:
        print("Correct.")
        score += 1 
        
    else:
        print("Incorrect!")   
        print(f"The correct answer was {questions[question_num]["answers"]}")
        
            
print(f"Your final score is {score}")
    