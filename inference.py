from flask import Flask, request, jsonify
from env import GridEnvironment

app = Flask(__name__)

env = GridEnvironment(difficulty="easy", grid_size=5)

@app.route("/reset", methods=["POST"])
def reset():
    state = env.reset()
    return jsonify({"state": state})

@app.route("/step", methods=["POST"])
def step():
    data = request.json
    action = data.get("action")

    state, reward, done, info = env.step(action)

    return jsonify({
        "state": state,
        "reward": reward,
        "done": done,
        "info": info
    })

@app.route("/")
def home():
    return "RL Environment Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)