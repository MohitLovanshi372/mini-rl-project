from flask import Flask, request, jsonify
from env import GridEnvironment

app = Flask(__name__)

env = GridEnvironment(difficulty="easy", grid_size=5)

@app.route("/reset", methods=["GET", "POST"])
def reset_env():
    env.reset()
    state = env.reset()
    return jsonify({"status": "ok", "observation": state}), 200

@app.route("/step", methods=["GET", "POST"])
def step_env():
    data = request.get_json(force=True, silent=True) or {}
    action = data.get("action", 0)
    state, reward, done, info = env.step(action)
    return jsonify({
        "observation": state,
        "reward": reward,
        "done": done
    }), 200

@app.route("/", methods=["GET", "POST"])
def home():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)