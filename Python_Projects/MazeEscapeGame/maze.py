# maze.py

import random

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['#' for _ in range(cols)] for _ in range(rows)]
        self.start_pos = (1, 1)
        self.end_pos = (rows - 2, cols - 2)
        self.treasures = []
        self._generate_maze()       # ✅ First carve paths
        self._place_treasures()     # ✅ Then place treasures


    def _generate_maze(self):
        from collections import deque

        def bfs_path_exists():
            queue = deque([self.start_pos])
            visited = set()
            visited.add(self.start_pos)

            while queue:
                current = queue.popleft()
                if current == self.end_pos:
                    return True

                r, c = current
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    next_pos = (nr, nc)
                    if (
                        0 <= nr < self.rows and
                        0 <= nc < self.cols and
                        self.grid[nr][nc] != '#' and
                        next_pos not in visited
                    ):
                        queue.append(next_pos)
                        visited.add(next_pos)
            return False

        while True:
            # Create random maze
            for i in range(1, self.rows - 1):
                for j in range(1, self.cols - 1):
                    self.grid[i][j] = ' ' if random.random() > 0.3 else '#'

            self.grid[self.start_pos[0]][self.start_pos[1]] = 'S'
            self.grid[self.end_pos[0]][self.end_pos[1]] = 'E'

            if bfs_path_exists():
                break  # ✅ Valid path exists, break out


    def _place_treasures(self, count=5):
        import random
        placed = 0
        while placed < count:
            r = random.randint(1, self.rows - 2)
            c = random.randint(1, self.cols - 2)
            pos = (r, c)
            if self.grid[r][c] == ' ' and pos not in [self.start_pos, self.end_pos] and pos not in self.treasures:
                self.treasures.append(pos)
                placed += 1

    def display(self, player_pos):
        for i in range(self.rows):
            row = ''
            for j in range(self.cols):
                if (i, j) == player_pos:
                    row += 'P'  # Player
                else:
                    row += self.grid[i][j]
            print(row)

    def is_valid_move(self, pos):
        i, j = pos
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.grid[i][j] != '#'
        return False

    def to_dict(self):
        return {
            "rows": self.rows,
            "cols": self.cols,
            "grid": self.grid,
            "start_pos": self.start_pos,
            "end_pos": self.end_pos,
            "treasures": self.treasures
        }

    @classmethod
    def from_dict(cls, data):
        maze = cls(data["rows"], data["cols"])
        maze.grid = data["grid"]
        maze.start_pos = tuple(data["start_pos"])
        maze.end_pos = tuple(data["end_pos"])
        maze.treasures = data.get("treasures", [])
        return maze
    # maze.py (inside class Maze)

    def find_shortest_path(self):
        from collections import deque

        queue = deque()
        visited = set()
        parent = {}

        start = self.start_pos
        end = self.end_pos

        queue.append(start)
        visited.add(start)

        while queue:
            current = queue.popleft()
            if current == end:
                break

            r, c = current
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                next_pos = (nr, nc)

                if self.is_valid_move(next_pos) and next_pos not in visited:
                    queue.append(next_pos)
                    visited.add(next_pos)
                    parent[next_pos] = current

        # Reconstruct path
        path = []
        current = end
        while current != start:
            path.append(current)
            current = parent.get(current)
            if current is None:
                return []  # No path found
        path.reverse()
        return path