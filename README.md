# OPIM 243: Project 1
## rock-paper-scissors-exercise

### How do I run the game?
- Open the command line interface
- Activate game-specific conda environment with Python 3.8:
  - ```conda create -n rps-env Python=3.8```
  - ```conda activate rps-env```
- Install required packages using pip and "requirements.txt" file:
  - ```pip install -r requirements.txt```
- Run game using command:
  - ```python game.py```
- If you'd like to customize your player name:
  - Pass an environment variable PLAYER_NAME
  - ```PLAYER_NAME="Bulldog Hoya" python game.py```
- Enjoy playing!

### What are the rules of the game?
- Rock beats scissors but loses to paper
- Scissors beat paper but lose to rock
- Paper beats rock but loses to scissors

### Testing

To run tests on the logic that decides the winner of
the game, type the following command into the command 
line interface:
- ```pytest```
