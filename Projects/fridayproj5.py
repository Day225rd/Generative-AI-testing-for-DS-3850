import random  # Importing random module for random color function

# Step 1: Define functions for different colors
def redText(text):
    return f"\033[31m{text}\033[0m"  # ANSI code for red text

def greenText(text):
    return f"\033[32m{text}\033[0m"  # ANSI code for green text

def blueText(text):
    return f"\033[34m{text}\033[0m"  # ANSI code for blue text

def yellowText(text):
    return f"\033[33m{text}\033[0m"  # ANSI code for yellow text

def brownText(text):
    return f"\033[35m{text}\033[0m"  # ANSI code for magenta (brownish appearance)

# Step 2: Define a function for random color
def randomColor(text):
    colors = [redText, greenText, blueText, yellowText, brownText]  # List of color functions
    return random.choice(colors)(text)  # Randomly choose a color function and apply it

# Step 3: Main Program Logic
def main():
    # Print examples of each color
    print(redText("This is red text."))
    print(greenText("This is green text."))
    print(blueText("This is blue text."))
    print(yellowText("This is yellow text."))
    print(brownText("This is brown text."))

    while True:  # Loop to continue taking user input
        color_choice = input("Choose a color (red, green, blue, yellow, brown, random) or type 'exit' to quit: ").strip().lower()

        if color_choice == 'exit':
            print("Goodbye!")
            break  # Exit the loop and end the program

        user_text = input("Enter the text you want to color: ")

        # Step 4: Apply the chosen color
        if color_choice == 'red':
            print(redText(user_text))
        elif color_choice == 'green':
            print(greenText(user_text))
        elif color_choice == 'blue':
            print(blueText(user_text))
        elif color_choice == 'yellow':
            print(yellowText(user_text))
        elif color_choice == 'brown':
            print(brownText(user_text))
        elif color_choice == 'random':
            print(randomColor(user_text))
        else:
            print("Invalid color choice. Please try again.")

# Step 5: Run the main function
if __name__ == "__main__":
    main()