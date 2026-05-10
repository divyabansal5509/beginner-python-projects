def run_quiz():
    questions = [
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["a) func", "b) define", "c) def", "d) function"],
            "answer": "c"
        },
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["a) .py", "b) .pyt", "c) .pt", "d) .python"],
            "answer": "a"
        },
        {
            "question": "Which data type is used to store multiple items in a single variable?",
            "options": ["a) int", "b) list", "c) float", "d) bool"],
            "answer": "b"
        }
    ]

    score = 0

    print("--- Welcome to the Python Basics Quiz! ---\n")

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
        
        guess = input("Your answer (a, b, c, or d): ").strip().lower()

        if guess == q['answer']:
            print("Correct! ✅\n")
            score += 1
        else:
            print(f"Wrong! ❌ The correct answer was {q['answer']}.\n")

    print(f"Quiz Complete! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()