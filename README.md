# Generative-AI-testing
Recreating all of our previous projects done while in DS-3850 using chat GPT. 

Why? To test the effectiveness of chatGPT and other generative AI's with writing basic code in Python. And to see the differences in how we wrote the code VS how AI does it with the provided info. 

Down below are all six projects explained by chatGPT 3.5.

[
Friday Project 1 Madlib.
Explanation of Each Part:

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

[
Friday project 2 powerball number generator.

]