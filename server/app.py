from openenv.core.env_server import create_app
from models import Action, Observation
from server.my_env_environment import MyEnvironment

app = create_app(
    MyEnvironment,   # ⚠️ CLASS ONLY
    Action,
    Observation,
    env_name="my_env",
    max_concurrent_envs=1,
)

def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()