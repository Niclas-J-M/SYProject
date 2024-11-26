import gymnasium as gym
from gymnasium.envs.registration import register
from env.ScotlandYard_env import ScotlandYardEnv
import numpy as np

def main():
    register(
        id="ScotlandYard-v0",
        entry_point="env.ScotlandYard_env:ScotlandYardEnv",
    )
    env = gym.make("ScotlandYard-v0")

    obs, info = env.reset()
    done = False

    while not done:
        # Mister X action
        mister_x_pos = env.unwrapped.mister_x_position
        valid_actions = env.unwrapped.get_valid_actions(0)
        action = valid_actions[np.random.randint(len(valid_actions))]  # Random valid action
        obs, reward, terminated, truncated, info = env.step((0, *action))
        done = terminated or truncated
        print(f"Mister X took action: {mister_x_pos} to {action[0]} using {action[1]}, Reward: {reward}")
        

        if done:
            break

        # Detectives' actions
        for detective_id in range(1, 5):
            detective_pos = env.unwrapped.detectives_positions[detective_id]
            print("det pos", detective_pos)
            valid_actions = env.unwrapped.get_valid_actions(detective_id)
            print("valid actions", valid_actions)
            if valid_actions:  # Ensure there are valid actions
                action = valid_actions[np.random.randint(len(valid_actions))]  # Random valid action
                obs, reward, terminated, truncated, info = env.step((detective_id, *action))
                done = terminated or truncated
                print(f"Detective {detective_id} took action: {detective_pos} to {action[0]} using {action[1]}, Reward: {reward}")
                

            if done:
                break

if __name__ == "__main__":
    main()
