from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name):
        self.num_wins = 0
        self.name = name
    @abstractmethod
    def make_choice(self):
        pass