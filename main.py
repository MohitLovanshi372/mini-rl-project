from env import MiniEnv

env = MiniEnv()
state = env.reset()

# Smart path (shortest path)
actions = ["RIGHT", "RIGHT", "DOWN", "DOWN"]

done = False
steps = 0

print(" Smart Agent Running...\n")

for action in actions:
    state, reward, done = env.step(action)
    steps += 1
    print(f"Step {steps}: Action={action}, Position={state}, Reward={reward}")

    if done:
        break

if done:
    print("\nGoal Reached Efficiently!")
else:
    print("\n Failed")

score = 100 - steps if done else 0
print("Final Score:", score)