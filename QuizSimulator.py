import random


questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Pokhara", "B. Kathmandu", "C. Biratnagar", "D. Butwal"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. func"],
        "answer": "C"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the output of 5 + 3 * 2?",
        "options": ["A. 16", "B. 11", "C. 13", "D. 10"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False values?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "Who has won the most FIFA World Cups?",
        "options": ["A. Germany", "B. Brazil", "C. Argentina", "D. Italy"],
        "answer": "B"
    },
    {
        "question": "Who won 2022 World Cup?",
        "options": ["A. Nepal", "B. Argentina", "C. France", "D. Brazil"],
        "answer": "C"
    },
    {
        "question": "Which company created Python?",
        "options": ["A. Microsoft", "B. Google", "C. Apple", "D. None of the above"],
        "answer": "D"
    },
    {
        "question": "Which team does haaland play on?",
        "options": ["A. Man City", "B. Man Utd", "C. FCB", "D. RMA"],
        "answer": "C"
    }
]


print("Welcome to Quiz Simulator")
name = input("Enter your name: ")

score = 0

for question in questions:
    print(question["question"])
    print(question["options"])
    user_ans = input("Enter you choice: ").upper()
    if user_ans == question["answer"]:
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print(f"{name}, your score is {score}")