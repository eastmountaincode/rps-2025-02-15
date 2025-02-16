from game_flow.game.display_start_game_details import display_start_game_details
from game_flow.game.game_init import game_init
from game_flow.game.game import Game

def main_loop():
    while True:
        # Ask if the user wants to start a new game
        while True:
            start_game = input("Start a new game? (y/n): ").strip().lower()
            if start_game in ("y", "n"):
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if start_game == "n":
            break

        # Initialize game
        player1, player2, total_rounds = game_init()

        # Display game details
        display_start_game_details(player1, player2, total_rounds)

        # Create and play game
        game = Game(player1=player1, player2=player2, total_rounds=total_rounds)
        game.play_game()
