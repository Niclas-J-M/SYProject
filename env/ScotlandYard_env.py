import gym
from gym import spaces
import numpy as np
import networkx as nx

class ScotlandYardEnv(gym.Env):
    def __init__(self):
        super(ScotlandYardEnv, self).__init__()

        #The board
        self.board = self.create_board()

        #Actions and observations
        self.action_space = spaces.Discrete(200)
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(500,), dtype=np.float32
        ) 

        self.reset()
    
    def create_board(self):
        # Gragh based representation of the board
        board = nx.Graph()
        board.add_nodes_from(range(1, 200))
        board.add_edge(1, 2, transport="taxi")
        board.add_edge(2, 3, transport="bus")
        board.add_edge(3, 4, transport="subway")

        return board
    
    def reset(self):
        # Reset the environment to its initial state
        self.mister_x_position = np.random.randint(1, 200)
        self.detectives_positions = [np.random.randint(1, 200) for _ in range(5)]
        self.mister_x_tickets = {"taxi": 4, "bus": 3, "subway": 3}
        self.detectives_tickets = [{"taxi": 10, "bus": 8, "subway": 4} for _ in range(5)]
        self.current_turn = 1
        self.done = False
        return self.get_observation()
    
    def step(self, action):
        """
        Process the given action and update the game state.

        Parameters:
            action: A tuple (player_id, destination, transport_type)
                    player_id: 'Mister X' or index of the detective (0-4).
                    destination: The node to which the player wants to move.
                    transport_type: The mode of transport (e.g., 'taxi', 'bus', 'subway').

        Returns:
            observation (array): The updated game state.
            reward (float): The reward for the current action.
            done (bool): Whether the game is finished.
            info (dict): Additional information.
        """
        if self.done:
            raise ValueError("Game has already ended. Reset the environment to start a new game.")

        player_id, destination, transport_type = action

        # Validate action
        if player_id == "Mister X":
            current_position = self.mister_x_position
            tickets = self.mister_x_tickets
        else:
            current_position = self.detectives_positions[player_id]
            tickets = self.detectives_tickets[player_id]

        # Check if the destination is valid
        if not self.board.has_edge(current_position, destination):
            raise ValueError(f"Invalid move: No edge between {current_position} and {destination}.")
        if self.board[current_position][destination]["transport"] != transport_type:
            raise ValueError(f"Invalid transport: {transport_type} not valid between {current_position} and {destination}.")
        if tickets[transport_type] <= 0:
            raise ValueError(f"Insufficient {transport_type} tickets for player {player_id}.")

        # Update position and deduct ticket
        if player_id == "Mister X":
            self.mister_x_position = destination
            self.mister_x_tickets[transport_type] -= 1
        else:
            self.detectives_positions[player_id] = destination
            self.detectives_tickets[player_id][transport_type] -= 1

        # Calculate reward
        reward = self.calculate_reward(player_id, destination)

        # Check if the game is over
        self.current_turn += 1
        self.done = self.check_done()

        # Return updated observation, reward, done, and additional info
        return self.get_observation(), reward, self.done, {"turn": self.current_turn}

    def calculate_reward(self, player, destination):
        # Define a reward system
        if player == "Mister X" and destination == self.mister_x_position:
            return -10  # Penalty for being caught
        elif player != "Mister X" and destination == self.mister_x_position:
            return 10  # Reward for catching Mister X
        return 0  # Neutral for other moves
    
    def get_observation(self):
        # Return the current game state as an observation
        state = {
            "mister_x_position": self.mister_x_position,
            "detectives_positions": self.detectives_positions,
            "tickets": {
                "mister_x": self.mister_x_tickets,
                "detectives": self.detectives_tickets,
            },
            "turn": self.current_turn,
        }
        return self.encode_state(state)
    
    def encode_state(self, state):
        # Encode the state into a numerical format for RL agents
        # Example: Flatten positions, tickets, and turn into a vector
        encoded_state = np.zeros(500)  # Example fixed-size vector
        encoded_state[0] = state["mister_x_position"]
        for i, pos in enumerate(state["detectives_positions"]):
            encoded_state[1 + i] = pos
        return encoded_state
    
    def check_done(self):
        # Check if the game is over
        if any(pos == self.mister_x_position for pos in self.detectives_positions):
            return True  # Mister X caught
        if self.current_turn >= 22:  # End of game
            return True
        return False