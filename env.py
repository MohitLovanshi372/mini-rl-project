class MiniEnv:
    def __init__(self):
        self.grid = [
            ['S', '.', '.'],
            ['.', 'X', '.'],
            ['.', '.', 'G']
        ]
        self.agent_pos = [0, 0]

    def reset(self):
        self.agent_pos = [0, 0]
        return self.agent_pos

    def step(self, action):
        x, y = self.agent_pos

        if action == "UP":
            x -= 1
        elif action == "DOWN":
            x += 1
        elif action == "LEFT":
            y -= 1
        elif action == "RIGHT":
            y += 1

        # boundary check
        x = max(0, min(2, x))
        y = max(0, min(2, y))

        self.agent_pos = [x, y]
        cell = self.grid[x][y]

        if cell == 'G':
            return self.agent_pos, 10, True
        elif cell == 'X':
            return self.agent_pos, -5, False
        else:
            return self.agent_pos, -1, False