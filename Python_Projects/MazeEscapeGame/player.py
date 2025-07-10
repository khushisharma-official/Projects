# player.py

class Player:
    def __init__(self, start_pos):
        self.position = start_pos
        self.treasure_collected = 0


    def move(self, direction, maze):
        row, col = self.position

        if direction == 'w':
            new_pos = (row - 1, col)
        elif direction == 's':
            new_pos = (row + 1, col)
        elif direction == 'a':
            new_pos = (row, col - 1)
        elif direction == 'd':
            new_pos = (row, col + 1)
        else:
            print("Invalid direction!")
            return

        if maze.is_valid_move(new_pos):
            self.position = new_pos
            if new_pos in maze.treasures:
                maze.treasures.remove(new_pos)
                self.treasure_collected += 1

        else:
            print("🚫 You hit a wall!")

    def to_dict(self):
        return {
            "position": self.position,
            "treasure_collected": self.treasure_collected
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(start_pos=tuple(data["position"]))
        player.treasure_collected = data.get("treasure_collected", 0)
        return player

