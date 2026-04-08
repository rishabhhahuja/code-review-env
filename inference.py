import os
import asyncio
from openenv.core import EnvClient
from models import Action

# ENV variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

class MyClient(EnvClient):   
    pass


async def main():
    try:
        async with MyClient(base_url=API_BASE_URL) as env:

            print("START")

            # RESET
            reset = await env.reset()
            print("Reset done")

            # STEP
            result = await env.step(
                Action(decision="FLAG_BUG")
            )

            print("STEP")
            print("Reward:", result.reward)

            print("END")

    except Exception as e:
        print("ERROR:", str(e))


if __name__ == "__main__":
    asyncio.run(main())