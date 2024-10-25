# Define the template for the Mad Lib
mad_lib_template = """
I've had a very [ADJECTIVE] day.
This morning, I dropped a box of [PLURAL NOUN] on my [BODY PART].
Then, at lunch, I went to [RESTAURANT] for their delicious [FIRST FOOD],
but the waiter brought me [SECOND FOOD], which I was not hungry for.
Finally, on my way home, I was cut off by a van with a large [LARGE OBJECT] strapped to the roof.
"""

# Create a function to gather user input
def get_user_input():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:\n")
    
    # Collecting user inputs
    adjective = input("Adjective: ")
    large_object = input("A large object: ")
    plural_noun = input("Large objects (plural): ")
    body_part = input("Body part: ")
    restaurant = input("Restaurant: ")
    first_food = input("Food (first): ")
    second_food = input("Food (second): ")
    
    # Returning a dictionary of user inputs
    return {
        "ADJECTIVE": adjective,
        "LARGE OBJECT": large_object,
        "PLURAL NOUN": plural_noun,
        "BODY PART": body_part,
        "RESTAURANT": restaurant,
        "FIRST FOOD": first_food,
        "SECOND FOOD": second_food,
    }

# Function to replace placeholders in the template with user input
def create_mad_lib(template, words):
    for key, value in words.items():
        template = template.replace(f"[{key}]", value)
    return template

# Main function to run the Mad Lib game
def run_mad_lib():
    user_words = get_user_input()  # Gather user inputs
    completed_story = create_mad_lib(mad_lib_template, user_words)  # Create the story
    print("\nHere's your Mad Lib story:\n")  # Print the story
    print(completed_story)

# Run the Mad Lib game
run_mad_lib()  # Start the game

