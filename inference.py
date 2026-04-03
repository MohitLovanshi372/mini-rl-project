from env import GridEnvironment

def run():
    env = GridEnvironment(difficulty="easy", grid_size=5)
    state = env.reset()

    actions = [3,3,3,3,1,1,1,1]  # RIGHT, RIGHT, DOWN...

    done = False
    steps = 0

    for action in actions:
        state, reward, done, info = env.step(action)
        steps += 1
        if done:
            break

    return {
        "final_position": state,
        "steps": steps,
        "goal_reached": done
    }

if __name__ == "__main__":
    print(run())