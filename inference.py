from openenv.core import EnvClient
from models import Action, Observation

class MyClient(EnvClient[Action, Observation]):
    def _step_payload(self, action):
        return {"decision": action.decision}

    def _parse_result(self, payload):
        return payload


def run():
    env = MyClient.from_env("rishabhahuja/code-review-env")

    print("[START]")

    result = env.reset()
    total_reward = 0
    step = 0

    while not result["done"]:
        code = result["observation"]["code"]

        # simple logic
        if "=" in code and "==" not in code:
            decision = "FLAG_BUG"
        elif "password" in code:
            decision = "REJECT"
        elif "range(len" in code:
            decision = "SUGGEST_FIX"
        else:
            decision = "APPROVE"

        print(f"[STEP] step={step} decision={decision}")

        result = env.step(Action(decision=decision))
        total_reward += result["reward"]
        step += 1

    print(f"[END] total_reward={total_reward}")


if __name__ == "__main__":
    run()