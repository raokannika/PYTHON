# Program 7: Simple Quiz Game

questions = {
    "Capital of France?": "paris",
    "2 + 2 = ?": "4",
    "Python keyword for function?": "def"
}

score = 0
for q, ans in questions.items():
    user = input(q + " ").lower()
    if user == ans:
        score += 1

print("Your score:", score, "/", len(questions))
