import random  # Import random module to generate random math problems

# Introduction to the game
print("Welcome to the Math Quiz Game!")
print("Solve as many math problems as you can. Let's get started!\n")

# Variables to track score
score = 0
        
# Function to generate a random math problem
def generate_problem():
    num1 = random.randint(1, 10)  # Generate a random number between 1 and 10
    num2 = random.randint(1, 10)  # Generate another random number
    operation = random.choice(["+", "-", "*"])  # Randomly choose an operation

    # Calculate the correct answer based on the operation
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    
    # Return the problem as a string and the correct answer
    return f"{num1} {operation} {num2}", correct_answer

# Main game loop
while True:
    # Generate a new problem
    problem, correct_answer = generate_problem()

    # Display the problem and get user's answer
    user_answer = int(input(f"Solve: {problem} = "))  # Input for user's answer
    
    # Check if the answer is correct and update the score
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1  # Increase score for correct answer
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
    
    # Ask if the player wants to continue
    play_again = input("Do you want to solve another problem? (yes/no): ").lower()
    
    # If the player says no, break the loop and end the game
    if play_again != "yes":
        print(f"\nThanks for playing! Your final score is: {score}")
        break  # Exit the loop
