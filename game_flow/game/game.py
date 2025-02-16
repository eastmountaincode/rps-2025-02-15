from game_flow.game.display_start_game import display_start_game

class Game():
    def __init__(self, player1, player2, total_rounds):
        self.player1 = player1
        self.player2 = player2
        total_rounds = total_rounds

    def game_loop(self):
        pass

    def play_game(self):
        display_start_game()
        self.game_loop()
