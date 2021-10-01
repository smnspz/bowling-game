import random


class Game:
    frames = {}
    pins_count = 10

    def scoreboard_generator(self):
        frame_count = 1
        while frame_count <= 10:
            self.frame(frame_count, self.pins_count)
            frame_count += 1

    def frame(self, frame_count, pins_count):
        round_count = 1
        self.frames[f"frame_number_{frame_count}"] = {}
        while round_count <= 2:
            self.round(frame_count, round_count, pins_count)
            round_count += 1

    def round(self, frame_count, round_count, pins_count):
        roll_result = self.roll(pins_count)
        self.frames[f"frame_number_{frame_count}"].update(
            {f"roll_{round_count}": roll_result}
        )

    def roll(self, pins_count):
        pins_hit = random.randint(0, pins_count)
        pins_count -= pins_hit
        return pins_hit
