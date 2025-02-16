import random
from game_flow.player.Player import Player

class ComputerPlayer(Player):
    def make_choice(self):
        return random.choice(["rock", "paper", "scissors"])