import random


class Game:
    frames: dict = {}

    def score(self) -> dict:
        frame_count = 1
        while frame_count <= 10:
            self.frame(frame_count)
            frame_count += 1
        return self.frames

    def frame(self, frame_count: int):
        round_count = 1
        pins_left = 10
        self.dict_builder(frame_count, {})
        while round_count <= 2:
            pins_left = self.round(frame_count, round_count, pins_left)
            round_count += 1
        else:
            self.dict_builder(frame_count, {"score: ": 10 - pins_left})

    def round(self, frame_count: int, round_count: int, pins_left: int) -> int:
        pins_left = self.roll(pins_left, round_count, frame_count)
        self.is_strike_or_spare(round_count, pins_left)
        return pins_left

    def roll(self, pins_left: int, round_count: int, frame_count: int) -> int:
        roll_result = random.randint(0, pins_left)
        self.dict_builder(frame_count, {f"roll_{round_count}": roll_result})
        pins_left -= roll_result
        return pins_left

    def dict_builder(self, frame_count: int, payload: dict) -> None:
        try:
            self.frames[f"frame_number_{frame_count}"].update(payload)
        except KeyError:
            self.frames[f"frame_number_{frame_count}"] = payload

    def is_strike_or_spare(self, round_count: int, pins_left: int):
        if round_count == 1 & pins_left == 0:
            return True
        elif round_count == 2 & pins_left == 0:
            return False
