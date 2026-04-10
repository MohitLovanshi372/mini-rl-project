from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from env import GridEnvironment

class GridAction(BaseModel):
    action: int = 0

class GridObservation(BaseModel):
    observation: List[int]
    reward: float = 0.0
    done: bool = False

grid = GridEnvironment(difficulty="easy", grid_size=5)
app = FastAPI()

@app.post("/reset", response_model=GridObservation)
def reset():
    state = grid.reset()
    return GridObservation(observation=state)

@app.post("/step", response_model=GridObservation)
def step(action: GridAction):
    state, reward, done, info = grid.step(action.action)
    return GridObservation(observation=state, reward=reward, done=done)

@app.get("/state", response_model=GridObservation)
def state():
    if grid.agent_pos is None:
        grid.reset()
    return GridObservation(observation=grid.agent_pos)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)