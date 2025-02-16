from game_flow.player.HumanPlayer import HumanPlayer
from game_flow.player.ComputerPlayer import ComputerPlayer
"""
Initializes the game by prompting the user to select the player types (human or computer) and the total number of rounds to play.

Returns:
    tuple: A tuple containing the initialized player1, player2, and the total number of rounds.
"""
def game_init():
    # Determine player types
    while True:
        player_type1 = input("Should player1 be human or computer? (human/computer): ").strip().lower()
        if player_type1 in ("human", "computer"):
            break
        else:
            print("Invalid input. Please enter 'human' or 'computer'.")

    while True:
        player_type2 = input("Should player2 be human or computer? (human/computer): ").strip().lower()
        if player_type2 in ("human", "computer"):
            break
        else:
            print("Invalid input. Please enter 'human' or 'computer'.")

    # Initialize players based on input
    player1 = HumanPlayer("Player 1") if player_type1 == "human" else ComputerPlayer("Computer 1")
    player2 = HumanPlayer("Player 2") if player_type2 == "human" else ComputerPlayer("Computer 2")
    
    while True:
        try:
            total_win_rounds = int(input("How many rounds do you need to win to win the game?: "))
            if total_win_rounds <= 0:
                print("Total rounds must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Return initialized players and total rounds
    return player1, player2, total_win_rounds