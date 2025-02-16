import random
from game_flow.player.Player import Player
import time

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    def make_choice(self):
        print(f"{self.name} is thinking...")
        time.sleep(1)
        return random.choice(["rock", "paper", "scissors"])