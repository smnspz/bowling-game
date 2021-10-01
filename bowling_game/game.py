import random


class Game:
    frames = 10
    pins = 10

    def roll(self, pins=random.randint(0, 9)):
        return pins

    def score(self):
        pass
