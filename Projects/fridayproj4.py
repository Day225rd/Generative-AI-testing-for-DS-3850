# Step 1: Define a dictionary with trivia questions and their answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "What year did the Titanic sink?": "1912"
}

# Step 2: Loop through the questions in the dictionary
for question, correct_answer in trivia_questions.items():
    print(question)  # Step 3: Display the question to the user
    user_answer = input("Your answer: ").strip()  # Step 4: Prompt the user for their answer

    # Step 5: Check if the user's answer matches the correct answer
    if user_answer.lower() == correct_answer.lower():  # Case insensitive comparison
        print("Correct! 🎉")  # Step 6: Provide positive feedback
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}.")  # Provide the correct answer

# Step 7: End of the quiz message
print("Thank you for playing! Good luck with your studies!")