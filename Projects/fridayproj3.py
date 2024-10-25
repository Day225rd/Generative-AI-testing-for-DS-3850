import random  # Step 1: Import the random module to use for generating random numbers

# Greeting the user
print("Welcome to the Number Guessing Game!")
play = input("Do you want to play? (yes/no): ").strip().lower()  # Step 2: Ask if the user wants to play

# Check if the user wants to play
if play == 'yes':  # Step 3: If the user says yes
    number_to_guess = random.randint(1, 10)  # Step 4: Generate a random number between 1 and 10
    guess = None  # Step 5: Initialize the variable to store user's guess

    # Loop until the user guesses correctly
    while guess != number_to_guess:  # Step 6: Continue looping until the guess is correct
        try:
            guess = int(input("Guess a number between 1 and 10: "))  # Step 7: Prompt for a guess
            if guess < number_to_guess:  # Step 8: Check if the guess is too low
                print("Too low. Try again!")
            elif guess > number_to_guess:  # Step 9: Check if the guess is too high
                print("Too high. Try again!")
            else:  # Step 10: The guess is correct
                print("Congratulations! You've guessed the number!")
        except ValueError:  # Handle non-integer input
            print("Please enter a valid number.")

else:  # Step 11: If the user says no
    print("Maybe next time!")  # Farewell message when not playing

# Farewell message
print("Thank you for playing! Goodbye!")  # Step 12: End the program with a farewell