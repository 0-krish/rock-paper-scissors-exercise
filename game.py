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

# Function: Determining the Winner
def determine_winner(user_decision, computer_decision):

    if user_decision == computer_decision:
        winning_player = None
    elif user_decision == "rock":
        if computer_decision == "paper":
            winning_player = computer_decision
        if computer_decision == "scissors":
            winning_player = user_decision
    elif user_decision == "paper":
        if computer_decision == "rock":
            winning_player = user_decision
        if computer_decision == "scissors":
            winning_player = computer_decision
    elif user_decision == "scissors":
        if computer_decision == "paper":
            winning_player = user_decision
        if computer_decision == "rock":
            winning_player = computer_decision

    return winning_player

if __name__ == "__main__":
    # Importing the Environment Variable
    import os
    player_name = os.getenv("PLAYER_NAME", default="Player One")

    # Welcome player to game
    print("----------")
    print("Welcome to the Rock-Paper-Scissors Game, " + player_name + "! Let's get started.")
    print("----------")

    # Processing User Inputs
    user_input = input("Play your hand: rock, paper, or scissors? ")

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
    print("Computer chose:", computer_choice)

    # Determining the Winner
    winner = determine_winner(validated_user_input, computer_choice)

    # Displaying Results
    print("----------")
    if winner is None:
        print("It's a tie!")
    elif winner == computer_choice:
        print("Oops! Computer won.")
    elif winner == validated_user_input:
        if player_name == "Player One":
            print("Yay! You won.")
        else:
            print("Yay!", player_name, "won.")
    print("----------")
    print("Thanks for playing! Play again soon.")
