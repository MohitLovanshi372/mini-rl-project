from flask import Flask, request, jsonify
from env import GridEnvironment

app = Flask(__name__)

env = GridEnvironment(difficulty="easy", grid_size=5)

@app.route("/reset", methods=["POST"])
def reset_env():
    state = env.reset()
    return jsonify({"status": "ok", "observation": state}), 200  #  status + 200

@app.route("/step", methods=["POST"])
def step_env():
    data = request.get_json()
    action = data.get("action", 0)
    state, reward, done, info = env.step(action)
    return jsonify({
        "observation": state,
        "reward": reward,
        "done": done
    }), 200

@app.route("/")
def home():
    return "RL Environment Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  #  8080