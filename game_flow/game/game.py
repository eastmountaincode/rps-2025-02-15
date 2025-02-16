from game_flow.game.display_round_number import display_round_number
from game_flow.game.display_start_game import display_start_game
import time

class Game():
    def __init__(self, player1, player2, total_win_rounds):
        self.player1 = player1
        self.player2 = player2
        self.total_win_rounds = total_win_rounds
        self.round_number = 1
        self.outcome_mapping = {
            "rock": {
                "rock": "draw",
                "paper": "lose",
                "scissors": "win"
            },
            "paper": {
                "rock": "win",
                "paper": "draw",
                "scissors": "lose"
            },
            "scissors": {
                "rock": "lose",
                "paper": "win",
                "scissors": "draw"
            }
        }

    def game_loop(self):
        while True:
            self.play_round()
            self.print_game_details()
            if self.check_win():
                break


    def play_round(self):
        display_round_number(self.round_number)

        player1_choice = self.player1.make_choice()
        print(f"{self.player1.name} chose {player1_choice}")
        time.sleep(1)

        player2_choice = self.player2.make_choice()
        print(f"{self.player2.name} chose {player2_choice}")
        time.sleep(1)

        outcome = self.outcome_mapping[player1_choice][player2_choice]

        if outcome == "win":
            print(f"{self.player1.name} wins the round!")
            time.sleep(1)
            self.player1.increment_wins()
        elif outcome == "lose":
            print(f"{self.player2.name} wins the round!")
            time.sleep(1)
            self.player2.increment_wins()
        else:
            print("It's a draw!")
            time.sleep(1)
        self.round_number += 1


    def check_win(self):
        if self.player1.num_wins == self.total_win_rounds:
            print(f"{self.player1.name} wins the game!\n")
            time.sleep(1)
            return True
        elif self.player2.num_wins == self.total_win_rounds:
            print(f"{self.player2.name} wins the game!\n")
            time.sleep(1)
            return True
        return False
    
    def print_game_details(self):
        print(f"Player 1: {self.player1.name} - Wins: {self.player1.num_wins}")
        time.sleep(0.5)
        print(f"Player 2: {self.player2.name} - Wins: {self.player2.num_wins}")
        print("=" * 80)
        time.sleep(0.5)

    def play_game(self):
        display_start_game()
        self.game_loop()
