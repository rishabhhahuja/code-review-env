import random
from models import Observation, StepResult, Action

TASKS = [
    {"code": "if x = 5: print(x)", "label": "FLAG_BUG", "difficulty": "easy"},
    {"code": "for i in range(len(arr)): print(arr[i])", "label": "SUGGEST_FIX", "difficulty": "medium"},
    {"code": "password = input(); if password == '1234': login()", "label": "REJECT", "difficulty": "hard"}
]

VALID_ACTIONS = ["APPROVE", "REJECT", "FLAG_BUG", "SUGGEST_FIX"]


class MyEnvironment:

    def __init__(self):
        self.current = None
        self.episode_id = "episode_1"
        self.step_count = 0

    # RESET
    def reset(self):
        self.current = random.choice(TASKS)
        self.step_count = 0

        return StepResult(
            observation=Observation(
                code=self.current["code"],
                difficulty=self.current["difficulty"]
            ),
            reward=0.0,
            done=False
        )

    # STEP
    def step(self, action: Action):
        self.step_count += 1

        decision = action.decision
        correct = self.current["label"]

        if decision == correct:
            reward = 1.0
        elif decision == "FLAG_BUG" and correct == "REJECT":
            reward = 0.5
        else:
            reward = -0.5

        return StepResult(
            observation=Observation(
                code=self.current["code"],
                difficulty=self.current["difficulty"]
            ),
            reward=reward,
            done=True
        )

    # ✅ FIXED STATE (CRITICAL)
    def state(self):
        return {
            "episode_id": self.episode_id,
            "step_count": self.step_count
        }

    # ASYNC
    async def reset_async(self):
        return self.reset()

    async def step_async(self, action: Action):
        return self.step(action)

    async def state_async(self):
        return self.state()

    async def close(self):
        pass