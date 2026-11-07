
import random

class Die:
    def __init__(self, max_side=6, sides=None):
        if sides is not None:
            max_side = sides
        self.sides = max_side

    def roll(self):
        return random.randint(1, self.sides)
      