from game_flow.player.Player import Player

class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    def make_choice(self):
        move = ""
        validMove = False
        while validMove == False:
            move = input(f"{self.name}, enter your move (rock, paper, scissors): ").strip().lower()
            if move in ["rock", "paper", "scissors"]:
                validMove = True
            else:
                print("Invalid move. Please enter rock, paper, or scissors.")
        return move