import gym
from gym.envs.registration import register
from env.ScotlandYard_env import ScotlandYardEnv

def main():
    print("hello")
    register(
        id="ScotlandYard-v0",
        entry_point="env.ScotlandYard_env:ScotlandYardEnv",
    )
    env = gym.make("ScotlandYard-v0")

    obs, info = env.reset()
    done = False

    while not done:
        print("running")
        action = env.action_space.sample()  # Random action: (player_id, destination, transport_type)
        obs, reward, done, info = env.step(action)
        env.render()
        print(f"Action: {action}, Reward: {reward}")

    env.close()

if __name__ == "__main__":
    main()
