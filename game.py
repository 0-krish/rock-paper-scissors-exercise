#
# game.py
#
# Rock-Paper-Scissors Exercise
#
# Author: Krish Sarawgi
#   Github: "0-krish"
#   NetID: ks1730
#
# this is the file with the main and determine_winner functions

def main():
    # Importing the Environment Variable
    import os
    player_name = os.getenv("PLAYER_NAME", default="Player One")

    # Processing User Inputs
    print("Play your hand: rock, paper, or scissors?")
    user_input = input()

    # Validating User Inputs
    validated_user_input = user_input.lower()
    if ((validated_user_input != "rock") and
        (validated_user_input != "paper") and
        (validated_user_input != "scissors")):
        print("Sorry! Invalid input detected.")
        print("This game accepts only three inputs:",
              "rock, paper, and scissors")
        print("This game will now quit.")
        exit()
    else:
        print("You chose:", validated_user_input)

    # Simulating Computer Selection
    from random import choice
    valid_choices = ["rock", "paper", "scissors"]
    computer_choice = choice(valid_choices)

    # Determining the Winner
    winner = determine_winner(validated_user_input, computer_choice)

    # Displaying Results
    print(winner)

# Function: Determining the Winner
def determine_winner(user_decision, computer_decision):
    winning_player = "user"
    return winning_player

# Running the game through the main function
if __name__ == "__main__":
    print("Welcome to the Rock-Paper-Scissors Game! Lets get started.")
    # The RPS game will now run through the main function
