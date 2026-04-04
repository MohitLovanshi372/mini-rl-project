from flask import Flask, request, jsonify
from env import GridEnvironment

app = Flask(__name__)

env = GridEnvironment(difficulty="easy", grid_size=5)

@app.route("/reset", methods=["POST"])
def reset_env():
    state = env.reset()
    return jsonify({"observation": state})

@app.route("/step", methods=["POST"])
def step_env():
    data = request.get_json()
    action = data.get("action", 0)

    state, reward, done, info = env.step(action)

    return jsonify({
        "observation": state,
        "reward": reward,
        "done": done
    })

@app.route