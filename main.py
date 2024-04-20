import random

# Define the possible moves
moves = ["rock", "paper", "scissors"]

while True:  # Main game loop
    # Take user input
    user_action = input("Enter a choice (rock, paper, scissors): ")

# Make the computer choose
    computer_action = random.choice(moves)
    
# Determine the winner
    if user_action == computer_action:
        print(f"Both players chose {user_action}. It's a tie!")
    elif user_action == "rock" or user_action == "Rock":
        if computer_action == "scissors" or "Scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! Computer wins.")
    elif user_action == "paper" or user_action == "Paper":
        if computer_action == "rock" or "Rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cut paper! Computer wins.")
    elif user_action == "scissors" or user_action == "Scissors":
        if computer_action == "paper" or "Paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! Computer wins.")
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")


# want to play again?.
    play_again = input("Do you want to play again [YES/NO]").upper()
    if play_again == "NO":
        break

print("Thanks For playing. Have a great day!")
