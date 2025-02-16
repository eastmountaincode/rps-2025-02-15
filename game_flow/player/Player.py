from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.num_wins = 0
        self.name = name
    def increment_wins(self):
        self.num_wins += 1
    @abstractmethod
    def make_choice(self):
        pass