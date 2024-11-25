import gymnasium as gym
from gymnasium.envs.registration import register
from env.ScotlandYard_env import ScotlandYardEnv
import numpy as np

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
        # Mister X action
        valid_actions = env.unwrapped.get_valid_actions(0)
        action = valid_actions[np.random.randint(len(valid_actions))]  # Random valid action
        print(env.unwrapped.mister_x_position)
        print(action)
        print(*action)
        obs, reward, terminated, truncated, info = env.step((0, *action))
        done = terminated or truncated
        print(f"Mister X took action: {action}, Reward: {reward}")
        env.render()

        if done:
            break

        # Detectives' actions
        for detective_id in range(1, 6):
            valid_actions = env.unwrapped.get_valid_actions(detective_id)
            if valid_actions:  # Ensure there are valid actions
                action = valid_actions[np.random.randint(len(valid_actions))]  # Random valid action
                obs, reward, done, info = env.step((detective_id, *action))
                print(f"Detective {detective_id} took action: {action}, Reward: {reward}")
                env.render()

            if done:
                break

if __name__ == "__main__":
    main()
