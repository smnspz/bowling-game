import random


class Game:
    pins = 10
    rolls_per_round = 0

    def roll(self, limit):
        return random.randint(0, limit)

    def round(self):
        while self.rolls_per_round <= 1:
            self.pins -= self.roll(self.pins)
            self.rolls_per_round += 1

    def score(self):
        return self.pins
