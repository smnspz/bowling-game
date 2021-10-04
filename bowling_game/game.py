import random


class Game:
    frames: dict = {}

    def score(self) -> dict:
        frame_count = 1
        while frame_count <= 10:
            pins_count = 10
            self.frame(frame_count, pins_count)
            frame_count += 1
        return self.frames

    def frame(self, frame_count: int, pins_count: int) -> int:
        round_count = 1
        self.frames[f"frame_number_{frame_count}"] = {}
        while round_count <= 2:
            pins_count = self.round(frame_count, round_count, pins_count)
            round_count += 1
            self.is_strike_or_spare(round_count, pins_count)
        return pins_count

    def round(self, frame_count: int, round_count: int, pins_count: int) -> int:
        roll_result = self.roll(pins_count)
        self.frames[f"frame_number_{frame_count}"].update(
            {f"roll_{round_count}": roll_result}
        )
        pins_count -= roll_result
        return pins_count

    def roll(self, pins_count: int) -> int:
        return random.randint(0, pins_count)

    def is_strike_or_spare(self, round_count, pins_count):
        if round_count == 1 & pins_count == 0:
            print("Strike")
        elif round_count == 2 & pins_count == 0:
            print("Spare")
