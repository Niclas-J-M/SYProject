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

    obs = env.reset()
    done = False

    # Example action for Mister X: Move to node 5 using a taxi
    while not done:
        print("running")
        action = env.action_space.sample()  # Random action
        obs, reward, done, info = env.step(action)
        env.render()

    env.close()

if __name__ == "__main__":
    main()