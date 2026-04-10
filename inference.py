from fastapi import FastAPI, HTTPException
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
    try:
        state = grid.reset()
        return GridObservation(observation=state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/step", response_model=GridObservation)
def step(action: GridAction):
    try:
        state, reward, done, info = grid.step(action.action)
        return GridObservation(observation=state, reward=reward, done=done)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/state", response_model=GridObservation)
def state():
    try:
        if grid.agent_pos is None:
            grid.reset()
        return GridObservation(observation=grid.agent_pos)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

