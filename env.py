"""
Mini RL Grid Environment
A simple grid world for reinforcement learning experiments.
"""

from enum import IntEnum
from typing import Tuple, Dict, List, Optional


class Action(IntEnum):
    """Available actions for the agent."""
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class GridEnvironment:
    """
    A grid-based RL environment where an agent navigates from Start to Goal.
    
    The grid uses coordinates [row, col] where:
    - Row 0 is the top
    - Col 0 is the left
    
    Cell types:
    - 'S' = Start position
    - 'G' = Goal position
    - 'X' = Obstacle
    - '.' = Empty cell
    """
    
    # Reward constants
    REWARD_GOAL = 10
    REWARD_OBSTACLE = -5
    REWARD_STEP = -1
    
    # Movement deltas: [row_change, col_change]
    ACTION_DELTAS = {
        Action.UP: [-1, 0],
        Action.DOWN: [1, 0],
        Action.LEFT: [0, -1],
        Action.RIGHT: [0, 1]
    }
    
    def __init__(self, difficulty: str = "easy", grid_size: int = 5):
        """
        Initialize the environment.
        
        Args:
            difficulty: "easy", "medium", or "hard"
            grid_size: Size of the grid (grid_size x grid_size)
        """
        self.grid_size = grid_size
        self.difficulty = difficulty.lower()
        
        # Fixed positions for reproducibility
        self.start_pos = [0, 0]
        self.goal_pos = [grid_size - 1, grid_size - 1]
        
        # Set obstacles based on difficulty
        self.obstacles = self._get_obstacles()
        
        # Agent state
        self.agent_pos = None
        self.done = False
        self.total_steps = 0
        self.total_reward = 0
        
    def _get_obstacles(self) -> List[List[int]]:
        """Get obstacle positions based on difficulty level."""
        if self.difficulty == "easy":
            return []
        elif self.difficulty == "medium":
            return [[2, 2]]
        elif self.difficulty == "hard":
            return [[1, 1], [2, 2], [3, 3], [1, 3], [3, 1]]
        else:
            raise ValueError(f"Unknown difficulty: {self.difficulty}")
    
    def reset(self) -> List[int]:
        """
        Reset the environment to initial state.
        
        Returns:
            Initial position of the agent [row, col]
        """
        self.agent_pos = self.start_pos.copy()
        self.done = False
        self.total_steps = 0
        self.total_reward = 0
        return self.agent_pos.copy()
    
    def step(self, action: int) -> Tuple[List[int], int, bool, Dict]:
        """
        Execute one action in the environment.
        
        Args:
            action: Action to take (0=UP, 1=DOWN, 2=LEFT, 3=RIGHT)
            
        Returns:
            Tuple of (new_position, reward, done, info)
        """
        if self.done:
            raise RuntimeError("Episode is done. Call reset() first.")
        
        if self.agent_pos is None:
            raise RuntimeError("Environment not initialized. Call reset() first.")
        
        # Calculate new position
        delta = self.ACTION_DELTAS[Action(action)]
        new_row = self.agent_pos[0] + delta[0]
        new_col = self.agent_pos[1] + delta[1]
        
        # Check boundaries - stay in place if hitting wall
        if 0 <= new_row < self.grid_size and 0 <= new_col < self.grid_size:
            self.agent_pos = [new_row, new_col]
        
        # Calculate reward
        reward = self.REWARD_STEP  # Base step penalty
        
        # Check if hit obstacle
        if self.agent_pos in self.obstacles:
            reward += self.REWARD_OBSTACLE
        
        # Check if reached goal
        if self.agent_pos == self.goal_pos:
            reward += self.REWARD_GOAL
            self.done = True
        
        # Update stats
        self.total_steps += 1
        self.total_reward += reward
        
        info = {
            "steps": self.total_steps,
            "total_reward": self.total_reward
        }
        
        return self.agent_pos.copy(), reward, self.done, info
    
    def render(self) -> str:
        """
        Render the current grid state as a string.
        
        Returns:
            String representation of the grid
        """
        lines = []
        for row in range(self.grid_size):
            line = ""
            for col in range(self.grid_size):
                pos = [row, col]
                if pos == self.agent_pos:
                    line += "A "  # Agent
                elif pos == self.goal_pos:
                    line += "G "  # Goal
                elif pos == self.start_pos and self.agent_pos != pos:
                    line += "S "  # Start
                elif pos in self.obstacles:
                    line += "X "  # Obstacle
                else:
                    line += ". "  # Empty
            lines.append(line)
        return "\n".join(lines)
    
    def get_optimal_steps(self) -> int:
        """
        Get the minimum steps needed to reach goal (Manhattan distance).
        Used for scoring normalization.
        """
        return abs(self.goal_pos[0] - self.start_pos[0]) + \
               abs(self.goal_pos[1] - self.start_pos[1])


def get_action_name(action: int) -> str:
    """Convert action integer to readable name."""
    names = {0: "UP", 1: "DOWN", 2: "LEFT", 3: "RIGHT"}
    return names.get(action, "UNKNOWN")
