# Generative-AI-testing

Recreating all of our previous projects done while in DS-3850 using chat GPT. 
Why? To test the effectiveness of chatGPT and other generative AI's with writing basic code in Python. And to see the differences in how we wrote the code VS how AI does it with the provided info. 
Down below are all six projects explained by chatGPT 3.5.

[
Friday Project 1 Madlib.
Explanation of Each Line of Code. 

    Define the Template:
        mad_lib_template: A string that contains the structure of the story with placeholders (like [ADJECTIVE], [PLURAL NOUN], etc.) where user inputs will be inserted.
        
    Function to Gather User Input:
        def get_user_input():: A function that prompts the user for various types of words.
        print(...): Welcomes the user and provides instructions.
        input(...): Collects user responses for each required word.
        The function returns a dictionary with keys matching the placeholders in the template and values being the user-provided words.

    Function to Create the Mad Lib:
        def create_mad lib(template, words):: This function replaces placeholders in the template with the corresponding user inputs.
        for key, value in words.items():: Iterates over the dictionary of user inputs.
        template.replace(...): Substitutes each placeholder in the template with the user’s corresponding input.

    Main Function to Run the Game:
        def run_mad_lib():: Manages the overall game flow.
        user_words = get_user_input(): Calls the input function to gather words.
        completed_story = create_mad_lib(...): Generates the final story by replacing placeholders.
        print(...): Displays the completed Mad Lib story to the user.

         Run the Game:
        run_mad_lib(): Calls the main function to start the game.
]
.
[
Friday project 2 powerball number generator.
Description of Each Line of Code.

    import random: This line imports the random module, which provides functions to generate random numbers.

    print("Welcome to the Lottery Number Generator!"): This prints a welcome message to the user.

    print("This program will generate your lottery numbers for you."): This informs the user about the program's purpose.

    4-8. white_ball_x = random.randint(1, 69): Each of these lines generates a random number between 1 and 69 for the five white balls, storing each in a separate variable.

    red_ball = random.randint(1, 26): This line generates a random number between 1 and 26 for the red ball.

    print(f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5} {red_ball}"): This prints the five white ball numbers, separated by one space, followed by the red ball number with three spaces in between.

    print("Good luck, and may your numbers be lucky!"): This prints a farewell message to the user.
]
.
[
Friday project 3 Number Guessing Game
Description of each line of Code.

    Importing the Random Module: import random allows us to generate a random number for the user to guess.
    
    Greeting the User: The program welcomes the user to the game.
    
    User Input: It asks the user if they want to play. The input is normalized to lowercase for consistency.
    
    Check User Response:
    
    If the user responds with "yes":
    A random number between 1 and 10 is generated and stored in number_to_guess.
    A while loop runs until the user guesses the correct number.
    Inside the loop, the user is prompted to enter their guess.
    The program checks if the guess is too low, too high, or correct and provides appropriate feedback.
    If the input is not a valid number (causing a ValueError), the program informs the user to enter a valid number.
    Handling "No" Response: If the user does not want to play, the program prints a farewell message.
    
    Final Farewell Message: Regardless of whether the user played or not, the program ends with a thank-you message.
]
.
[
Friday project 4 Quiz Bowl.
Description of each line of code.

    Defining the Dictionary:
    
    The questions dictionary contains five trivia questions as keys and their corresponding answers as values.
    Looping Through the Questions:
    
    The for loop iterates over each question and its correct answer in the dictionary.
    Displaying Each Question:
    
    The current question is printed to the console.
    Prompting User Input:
    
    The user is asked to input their answer. The strip() method removes any leading or trailing whitespace.
    Checking the Answer:
    
    The program compares the user's answer (converted to lowercase for case insensitivity) with the correct answer.
    If the answer matches, a success message is displayed. If it does not match, the correct answer is shown.
    Farewell Message:
    
    After all questions have been answered, the program thanks the user for studying.
]
.
[
Friday project 5 Colorful text function.
Description of each line of code.

    Color Functions:
    
    Each function (redText, blueText, greenText, yellowText, brownText) takes a string as input and returns the string formatted with ANSI escape codes to display it in the specified color.
    The ANSI code \033[0m resets the color back to default after the colored text.
    Random Color Function:
    
    The randomColor function randomly selects one of the five color functions and applies it to the input text.
    Main Program Logic:
    
    The program begins by printing examples of each color function.
    A while loop allows the user to input their color choice and text to be displayed in that color.
    The user can choose to exit the program by typing "exit".
    If the user inputs an invalid color choice, the program prompts them to try again.
]
.
[
Friday project 6 Bank Class. 
Description of each line of code.

    Class Definition: class BankAccount: defines a class named BankAccount, which encapsulates the properties and methods related to a bank account.

    Initializer Method:
    
    def __init__(self, account_number): defines the constructor method that initializes the object.
    self.account_number = account_number assigns the provided account number to the instance.
    self.balance = 0.0 initializes the account balance to zero.
    Deposit Method:
    
    def deposit(self, amount): defines a method to deposit money.
    if amount > 0: checks if the deposit amount is positive.
    self.balance += amount adds the deposit amount to the balance.
    print(f"Successfully deposited ${amount:.2f}.") prints a confirmation message, formatted to two decimal places.
    else: print("Deposit amount must be positive.") provides feedback if the deposit amount is invalid.
    Withdraw Method:
    
    def withdraw(self, amount): defines a method to withdraw money.
    if 0 < amount <= self.balance: checks if the withdrawal amount is positive and does not exceed the balance.
    self.balance -= amount subtracts the withdrawal amount from the balance.
    print(f"Successfully withdrew ${amount:.2f}.") prints a confirmation message.
    elif amount > self.balance: print("Insufficient funds.") provides feedback for insufficient funds.
    else: print("Withdrawal amount must be positive.") provides feedback for invalid withdrawal amounts.
    Check Balance Method:
    
    def check_balance(self): defines a method to display the current balance.
    print(f"Current balance: ${self.balance:.2f}") prints the current balance formatted to two decimal places.
    Main Function:
    
    def main(): defines the main function where the program execution starts.
    account_number = input("Enter your account number: ") prompts the user to enter their account number.
    account = BankAccount(account_number) creates an instance of BankAccount using the provided account number.
    Indefinite Loop:
    
    while True: starts an indefinite loop to allow repeated interactions.
    The menu options are displayed using print statements.
    User Input:
    
    choice = input("Enter your choice: ").strip().lower() prompts the user for a choice and normalizes the input.
    Conditionals for User Choices:
    
    The if-elif structure checks the user’s choice and calls the corresponding methods on the account instance.
    The loop continues until the user chooses to exit (choice == 'd'), at which point it prints a farewell message and breaks the loop.
    Script Entry Point:
    
    if __name__ == "__main__": checks if the script is being run directly (not imported).
    main() calls the main function to start the program.
]
