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
Description of Each Line of Code

    import random: This line imports the random module, which provides functions to generate random numbers.

    print("Welcome to the Lottery Number Generator!"): This prints a welcome message to the user.

    print("This program will generate your lottery numbers for you."): This informs the user about the program's purpose.

    4-8. white_ball_x = random.randint(1, 69): Each of these lines generates a random number between 1 and 69 for the five white balls, storing each in a separate variable.

    red_ball = random.randint(1, 26): This line generates a random number between 1 and 26 for the red ball.

    print(f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5} {red_ball}"): This prints the five white ball numbers, separated by one space, followed by the red ball number with three spaces in between.

    print("Good luck, and may your numbers be lucky!"): This prints a farewell message to the user.
]