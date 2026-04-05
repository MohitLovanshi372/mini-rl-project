from openenv.core.env_server import Environment, create_fastapi_app
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

class MyEnv(Environment):
    def reset(self) -> GridObservation:
        state = grid.reset()
        return GridObservation(observation=state)

    def step(self, action: GridAction) -> GridObservation:
        state, reward, done, info = grid.step(action.action)
        return GridObservation(observation=state, reward=reward, done=done)

env = MyEnv()
app = create_fastapi_app(env, GridAction, GridObservation)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)