
import random

class Die:
    def __init__(self, max_side=6, sides=None):
        if sides is not None:
            max_side = sides
        self.sides = max_side

    def roll(self):
        return random.randint(1, self.sides)


class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evaluate_roll(self, total):
        if total == 7 or total == 11:
            return "Win"
        elif total == 2 or total == 3 or total == 12:
            return "Lose"
        else:
            return "Roll Again"

    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()
        total = roll1 + roll2
        result = self.evaluate_roll(total)

        return roll1, roll2, total, result
