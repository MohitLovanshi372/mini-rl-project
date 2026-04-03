"""
Main Demo Script
Runs the RL environment across all difficulty levels with smart paths.
"""

from env import GridEnvironment, Action, get_action_name
from grader import Grader


def get_smart_path(difficulty: str) -> list:
    """
    Get a predefined smart path for each difficulty level.
    These paths navigate from Start [0,0] to Goal [4,4].
    
    Args:
        difficulty: "easy", "medium", or "hard"
        
    Returns:
        List of actions to take
    """
    RIGHT = Action.RIGHT
    DOWN = Action.DOWN
    
    if difficulty == "easy":
        # Direct diagonal path: 4 rights, 4 downs
        # Optimal: 8 steps
        return [RIGHT, RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN, DOWN]
    
    elif difficulty == "medium":
        # Avoid obstacle at [2,2]
        # Go right first, then down, avoiding center
        return [RIGHT, RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN, DOWN]
    
    elif difficulty == "hard":
        # Obstacles at [1,1], [2,2], [3,3], [1,3], [3,1]
        # Navigate around them
        return [
            DOWN,   # [1,0]
            DOWN,   # [2,0]
            RIGHT,  # [2,1]
            DOWN,   # [3,0] - backtrack to avoid [3,1]
            DOWN,   # [4,0]
            RIGHT,  # [4,1]
            RIGHT,  # [4,2]
            RIGHT,  # [4,3]
            RIGHT   # [4,4] - GOAL!
        ]
    
    return []


def run_episode(env: GridEnvironment, actions: list, verbose: bool = True) -> dict:
    """
    Run one episode with given actions.
    
    Args:
        env: The grid environment
        actions: List of actions to execute
        verbose: Whether to print step-by-step output
        
    Returns:
        Episode results dictionary
    """
    position = env.reset()
    
    if verbose:
        print(f"\n{'='*50}")
        print(f"Difficulty: {env.difficulty.upper()}")
        print(f"{'='*50}")
        print(f"Start Position: {position}")
        print(f"Goal Position: {env.goal_pos}")
        print(f"Obstacles: {env.obstacles if env.obstacles else 'None'}")
        print(f"\nInitial Grid:")
        print(env.render())
        print(f"\n{'-'*50}")
        print("Starting navigation...\n")
    
    step_count = 0
    for action in actions:
        position, reward, done, info = env.step(action)
        step_count += 1
        
        if verbose:
            action_name = get_action_name(action)
            print(f"Step {step_count}: Action={action_name}, Position={position}, Reward={reward}")
        
        if done:
            break
    
    if verbose:
        print(f"\n{'-'*50}")
        if done:
            print("🎯 Goal Reached!")
        else:
            print("❌ Goal Not Reached")
        print(f"\nFinal Grid:")
        print(env.render())
    
    return {
        "done": done,
        "steps": step_count,
        "total_reward": info["total_reward"]
    }


def main():
    """Main function - runs all difficulty levels."""
    
    print("\n" + "="*60)
    print("   MINI RL ENVIRONMENT - HACKATHON DEMO")
    print("   Delivery Robot Navigation Simulation")
    print("="*60)
    
    difficulties = ["easy", "medium", "hard"]
    results = {}
    
    for difficulty in difficulties:
        # Create environment
        env = GridEnvironment(difficulty=difficulty, grid_size=5)
        
        # Get smart path for this difficulty
        smart_path = get_smart_path(difficulty)
        
        # Run episode
        episode_result = run_episode(env, smart_path, verbose=True)
        
        # Grade performance
        grader = Grader(optimal_steps=env.get_optimal_steps())
        report = grader.generate_report(
            actual_steps=episode_result["steps"],
            goal_reached=episode_result["done"],
            total_reward=episode_result["total_reward"]
        )
        
        # Print score
        print(f"\n📊 SCORE: {report['score']}")
        print(f"📈 Grade: {report['grade']}")
        print(f"⚡ Efficiency: {report['efficiency']}")
        print(f"💰 Total Reward: {report['total_reward']}")
        
        results[difficulty] = report
    
    # Final summary
    print("\n" + "="*60)
    print("   FINAL SUMMARY")
    print("="*60)
    print(f"\n{'Difficulty':<12} {'Steps':<8} {'Score':<8} {'Grade':<8}")
    print("-" * 40)
    
    total_score = 0
    for diff, report in results.items():
        print(f"{diff.capitalize():<12} {report['actual_steps']:<8} {report['score']:<8} {report['grade']:<8}")
        total_score += report['score']
    
    avg_score = total_score / len(results)
    print("-" * 40)
    print(f"{'AVERAGE':<12} {'':<8} {avg_score:.2f}")
    print("\n✅ All tests completed successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
