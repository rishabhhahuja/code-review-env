from pydantic import BaseModel

class Observation(BaseModel):
    code: str
    difficulty: str

class Action(BaseModel):
    decision: str

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool


class State(BaseModel):
    episode_id: str = ""
    step_count: int = 0