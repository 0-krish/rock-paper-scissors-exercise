# Rock-Paper-Scissors Exercise
#
# Author: Krish Sarawgi
#   Github: "0-krish"
#   NetID: ks1730

# Introducing the Game
print("Welcome to the Rock-Paper-Scissors Game! Lets get started.")

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

# Simulating Computer Selection

# Determining the Winner

# Displaying Results





