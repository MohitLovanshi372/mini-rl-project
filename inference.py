from env import GridEnvironment

env = GridEnvironment(difficulty="easy", grid_size=5)

def reset():
    state = env.reset()
    return {"state": state}

def step(action):
    state, reward, done, info = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    }

# for testing
if __name__ == "__main__":
    print(reset())
    print(step(3))