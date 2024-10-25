import random  # Importing the random module to use the randint function

# Greeting the user
print("Welcome to the Lottery Number Generator!")
print("This program will generate your lottery numbers for you.")

# Generating the first five numbers (white balls) between 1 and 69
white_ball_1 = random.randint(1, 69)  # Generate the first white ball number
white_ball_2 = random.randint(1, 69)  # Generate the second white ball number
white_ball_3 = random.randint(1, 69)  # Generate the third white ball number
white_ball_4 = random.randint(1, 69)  # Generate the fourth white ball number
white_ball_5 = random.randint(1, 69)  # Generate the fifth white ball number

# Generating the last number (red ball) between 1 and 26
red_ball = random.randint(1, 26)  # Generate the red ball number

# Printing the results with the specified spacing
print(f"{white_ball_1} {white_ball_2} {white_ball_3} {white_ball_4} {white_ball_5}   {red_ball}")

# Farewell message
print("Good luck, and may your numbers be lucky!")
