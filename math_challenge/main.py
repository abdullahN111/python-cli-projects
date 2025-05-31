import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_prob():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press Enter to start the quiz...")
print("------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_prob()
    while True:
        guess = input(f"Problem #{i+1}: {expression} = ? ")
        if guess == str(answer):
            print("Correct!")
            break
        wrong += 1
    
end_time = time.time()
time_taken = end_time - start_time

print("------------------------")
print(f"Quiz finished in {time_taken}s. You got {TOTAL_PROBLEMS - wrong} out of {TOTAL_PROBLEMS} correct.")