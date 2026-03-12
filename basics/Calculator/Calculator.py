import random

score = 0
rounds = 5

print("🎮 Welcome to the Calculator Game!")
print("You will answer", rounds, "questions.\n")

for i in range(rounds):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(["+", "-", "*"])

    question = f"{num1} {operator} {num2}"

    correct_answer = eval(question)

    user_answer = int(input(f"Question {i+1}: {question} = "))

    if user_answer == correct_answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The answer was {correct_answer}\n")

print("Game Over!")
print("Your score:", score, "/", rounds)
