#the program asks the user questions and doesnt let them continue till they get them correct
import random
import time

operators = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(operators)

    expr = f"{left}  {operator}  {right} "
    
    correct_answer = eval(expr) #the eval function helps me to shorten my code and it takes the string and executes it as a python expression returning the result
    return expr, correct_answer
expr, correct_answer = generate_problem() 

#working on the timing
wrong = 0
input("press enter to start")
print("---------------------------------")
start_time = time.time()

 

for i in range(TOTAL_PROBLEMS):
    expr, correct_answer = generate_problem()
    while True:
        guess = input("Problem #   " + str(i + 1)  + " : "  + expr + " = ")
        if guess == str(correct_answer):
            break
        wrong += 1
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-----------------------------------")
print(f"nice work! You finished in {total_time} seconds")
name = input("What is your name")
with open("scores.txt", "a") as f:#we then store the marks in a file
    f.write(f"{name})  -- TIME:{total_time}seconds ---WRONG_ANSWERS: {wrong} \n")
#here we try using the dictonary way
scores = {}
scores[name] = total_time
print("\nSCORESS")
for player, total_time in scores.items():
    print(player, ":", total_time, "seconds")

    
