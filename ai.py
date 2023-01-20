import random
from player import Player

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
    def choose_gesture(self):
       self.selected_gesture = random.choice(self.list_gestures)
       print(f"The computer has chosen {self.selected_gesture}")

