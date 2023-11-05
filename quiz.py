# Define the questions and answer choices
questions = [
    "What is the largest land animal?",
    "What is the fastest land animal?",
    "Which bird is known for its distinctive laugh-like call?",
    "What is the largest species of shark?",
    "Which mammal can fly and uses echolocation to navigate?"
]

choices = [
    ["a) Elephant", "b) Giraffe", "c) Rhinoceros"],
    ["a) Cheetah", "b) Gazelle", "c) Lion"],
    ["a) Eagle", "b) Owl", "c) Kookaburra"],
    ["a) Great White Shark", "b) Hammerhead Shark", "c) Whale Shark"],
    ["a) Bat", "b) Kangaroo", "c) Sloth"]
]

# Define the correct answers
correct_answers = ["a", "a", "c", "c", "a"]

# Initialize the user's score
score = 0

# Present the questions, collect answers, and calculate the score
for i in range(len(questions)):
    print(questions[i])
    for choice in choices[i]:
        print(choice)
    user_answer = input("Your answer (enter a, b, or c): ").lower()
    if user_answer == correct_answers[i]:
        score += 1

# Display the user's score
print(f"Your score: {score}/{len(questions)}")
