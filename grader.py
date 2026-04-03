"""
Grader System
Scores agent performance on a 0.0 to 1.0 scale.
"""

from typing import Dict


class Grader:
    """
    Deterministic grader for RL agent performance.
    
    Scoring formula:
        score = optimal_steps / actual_steps
        
    This gives:
        - 1.0 for optimal path
        - Lower scores for longer paths
        - Capped between 0.0 and 1.0
    """
    
    def __init__(self, optimal_steps: int, max_steps: int = 100):
        """
        Initialize the grader.
        
        Args:
            optimal_steps: Minimum steps needed to reach goal
            max_steps: Maximum allowed steps before score = 0
        """
        self.optimal_steps = optimal_steps
        self.max_steps = max_steps
    
    def calculate_score(self, actual_steps: int, goal_reached: bool) -> float:
        """
        Calculate normalized score between 0.0 and 1.0.
        
        Args:
            actual_steps: Number of steps taken by agent
            goal_reached: Whether agent reached the goal
            
        Returns:
            Score between 0.0 and 1.0
        """
        # No score if goal not reached
        if not goal_reached:
            return 0.0
        
        # Prevent division by zero
        if actual_steps <= 0:
            return 0.0
        
        # Calculate score: optimal / actual
        # Perfect path = 1.0, longer paths = lower score
        score = self.optimal_steps / actual_steps
        
        # Clamp between 0.0 and 1.0
        score = max(0.0, min(1.0, score))
        
        return round(score, 2)
    
    def get_grade(self, score: float) -> str:
        """
        Convert numeric score to letter grade.
        
        Args:
            score: Score between 0.0 and 1.0
            
        Returns:
            Letter grade (A, B, C, D, F)
        """
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    
    def generate_report(self, actual_steps: int, goal_reached: bool, 
                       total_reward: int) -> Dict:
        """
        Generate a complete grading report.
        
        Args:
            actual_steps: Steps taken
            goal_reached: Whether goal was reached
            total_reward: Total reward accumulated
            
        Returns:
            Dictionary with grading details
        """
        score = self.calculate_score(actual_steps, goal_reached)
        
        return {
            "optimal_steps": self.optimal_steps,
            "actual_steps": actual_steps,
            "goal_reached": goal_reached,
            "total_reward": total_reward,
            "score": score,
            "grade": self.get_grade(score),
            "efficiency": f"{score * 100:.0f}%"
        }
