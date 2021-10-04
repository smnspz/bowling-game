import random


class Game:
    frames: dict = {}
    pins_count: int = 10

    def scoreboard_generator(self) -> None:
        frame_count = 1
        while frame_count <= 10:
            self.frame(frame_count, self.pins_count)
            frame_count += 1

    def frame(self, frame_count: int, pins_count: int) -> None:
        round_count = 1
        self.frames[f"frame_number_{frame_count}"] = {}
        while round_count <= 2:
            self.round(frame_count, round_count, pins_count)
            round_count += 1

    def round(self, frame_count: int, round_count: int, pins_count: int) -> None:
        roll_result = self.roll(pins_count)
        self.frames[f"frame_number_{frame_count}"].update(
            {f"roll_{round_count}": roll_result}
        )

    def roll(self, pins_count: int) -> int:
        pins_hit = random.randint(0, pins_count)
        pins_count -= pins_hit
        return pins_hit
