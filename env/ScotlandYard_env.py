import gymnasium as gym
from gymnasium import spaces
import numpy as np
import networkx as nx
from gymnasium.spaces import MultiDiscrete
import matplotlib.pyplot as plt


class ScotlandYardEnv(gym.Env):
    def __init__(self):
        super(ScotlandYardEnv, self).__init__()

        #The board
        self.board = self.create_board()

        #Actions and observations
        # Example action space: (player_id, destination, transport_type)
        self.action_space = MultiDiscrete([6, 200, 3])  # 6 players (Mister X + 5 detectives), 200 locations, 3 transport types

        self.observation_space = spaces.Box(
            low=0, high=1, shape=(500,), dtype=np.float32
        ) 

        self.reset()
    
    def create_board(self):
        # Gragh based representation of the board
        board = nx.Graph()
        board.add_nodes_from(range(1, 200))
        board.add_edge(1, 8, transport="taxi")
        board.add_edge(1, 9, transport="taxi")
        board.add_edge(1, 58, transport="bus")
        board.add_edge(1, 46, transport="bus")
        board.add_edge(1, 46, transport="subway")

        board.add_edge(2, 10, transport="taxi")
        board.add_edge(2, 20, transport="taxi")

        board.add_edge(3, 11, transport="taxi")
        board.add_edge(3, 12, transport="taxi")
        board.add_edge(3, 4, transport="taxi")
        board.add_edge(3, 22, transport="bus")
        board.add_edge(3, 23, transport="bus")

        board.add_edge(4, 13, transport="taxi")
        board.add_edge(4, 3, transport="taxi")

        board.add_edge(5, 15, transport="taxi")
        board.add_edge(5, 16, transport="taxi")

        board.add_edge(6, 29, transport="taxi")
        board.add_edge(6, 7, transport="taxi")

        board.add_edge(7, 6, transport="taxi")
        board.add_edge(7, 17, transport="taxi")
        board.add_edge(7, 42, transport="bus")

        board.add_edge(8, 1, transport="taxi")
        board.add_edge(8, 18, transport="taxi")
        board.add_edge(8, 19, transport="taxi")

        board.add_edge(9, 1, transport="taxi")
        board.add_edge(9, 19, transport="taxi")
        board.add_edge(9, 20, transport="taxi")

        board.add_edge(10, 2, transport="taxi")
        board.add_edge(10, 21, transport="taxi")
        board.add_edge(10, 34, transport="taxi")
        board.add_edge(10, 11, transport="taxi")

        board.add_edge(11, 3, transport="taxi")
        board.add_edge(11, 10, transport="taxi")
        board.add_edge(11, 22, transport="taxi")

        board.add_edge(12, 3, transport="taxi")
        board.add_edge(12, 23, transport="taxi")

        board.add_edge(13, 4, transport="taxi")
        board.add_edge(13, 23, transport="taxi")
        board.add_edge(13, 24, transport="taxi")
        board.add_edge(13, 14, transport="taxi")
        board.add_edge(13, 23, transport="bus")
        board.add_edge(13, 52, transport="bus")
        board.add_edge(13, 14, transport="bus")
        board.add_edge(13, 67, transport="subway")
        board.add_edge(13, 46, transport="subway")
        board.add_edge(13, 89, transport="subway")

        board.add_edge(14, 13, transport="taxi")
        board.add_edge(14, 15, transport="taxi")
        board.add_edge(14, 25, transport="taxi")
        board.add_edge(14, 13, transport="bus")
        board.add_edge(14, 15, transport="bus")

        board.add_edge(15, 14, transport="taxi")
        board.add_edge(15, 5, transport="taxi")
        board.add_edge(15, 26, transport="taxi")
        board.add_edge(15, 16, transport="taxi")
        board.add_edge(15, 14, transport="bus")
        board.add_edge(15, 29, transport="bus")
        board.add_edge(15, 41, transport="bus")

        board.add_edge(16, 5, transport="taxi")
        board.add_edge(16, 15, transport="taxi")
        board.add_edge(16, 28, transport="taxi")
        board.add_edge(16, 29, transport="taxi")

        board.add_edge(17, 7, transport="taxi")
        board.add_edge(17, 30, transport="taxi")

        board.add_edge(18, 8, transport="taxi")
        board.add_edge(18, 31, transport="taxi")
        board.add_edge(18, 43, transport="taxi")
        
        board.add_edge(19, 8, transport="taxi")
        board.add_edge(19, 9, transport="taxi")
        board.add_edge(19, 32, transport="taxi")

        board.add_edge(20, 9, transport="taxi")
        board.add_edge(20, 2, transport="taxi")
        board.add_edge(20, 33, transport="taxi")

        board.add_edge(21, 33, transport="taxi")
        board.add_edge(21, 10, transport="taxi")

        board.add_edge(22, 11, transport="taxi")
        board.add_edge(22, 34, transport="taxi")
        board.add_edge(22, 23, transport="taxi")
        board.add_edge(22, 35, transport="taxi")
        board.add_edge(22, 3, transport="bus")
        board.add_edge(22, 23, transport="bus")
        board.add_edge(22, 34, transport="bus")
        board.add_edge(22, 65, transport="bus")

        board.add_edge(23, 22, transport="taxi")
        board.add_edge(23, 12, transport="taxi")
        board.add_edge(23, 13, transport="taxi")
        board.add_edge(23, 37, transport="taxi")
        board.add_edge(23, 3, transport="bus")
        board.add_edge(23, 22, transport="bus")
        board.add_edge(23, 13, transport="bus")
        board.add_edge(23, 67, transport="bus")

        board.add_edge(24, 13, transport="taxi")
        board.add_edge(24, 37, transport="taxi")
        board.add_edge(24, 38, transport="taxi")

        board.add_edge(25, 38, transport="taxi")
        board.add_edge(25, 14, transport="taxi")
        board.add_edge(25, 39, transport="taxi")
        
        board.add_edge(26, 15, transport="taxi")
        board.add_edge(26, 27, transport="taxi")
        board.add_edge(26, 39, transport="taxi")

        board.add_edge(27, 26, transport="taxi")
        board.add_edge(27, 28, transport="taxi")
        board.add_edge(27, 40, transport="taxi")

        board.add_edge(28, 27, transport="taxi")
        board.add_edge(28, 16, transport="taxi")
        board.add_edge(28, 41, transport="taxi")

        board.add_edge(29, 16, transport="taxi")
        board.add_edge(29, 41, transport="taxi")
        board.add_edge(29, 42, transport="taxi")
        board.add_edge(29, 6, transport="taxi")
        board.add_edge(29, 15, transport="bus")
        board.add_edge(29, 41, transport="bus")
        board.add_edge(29, 55, transport="bus")
        board.add_edge(29, 42, transport="bus")

        board.add_edge(30, 17, transport="taxi")
        board.add_edge(30, 42, transport="taxi")

        board.add_edge(31, 18, transport="taxi")
        board.add_edge(31, 43, transport="taxi")
        board.add_edge(31, 44, transport="taxi")

        board.add_edge(32, 19, transport="taxi")
        board.add_edge(32, 44, transport="taxi")
        board.add_edge(32, 45, transport="taxi")
        board.add_edge(32, 33, transport="taxi")

        board.add_edge(33, 20, transport="taxi")
        board.add_edge(33, 32, transport="taxi")
        board.add_edge(33, 21, transport="taxi")
        board.add_edge(33, 46, transport="taxi")

        board.add_edge(34, 47, transport="taxi")
        board.add_edge(34, 10, transport="taxi")
        board.add_edge(34, 48, transport="taxi")
        board.add_edge(34, 22, transport="taxi")
        board.add_edge(34, 22, transport="bus")
        board.add_edge(34, 46, transport="bus")
        board.add_edge(34, 63, transport="bus")
        
        board.add_edge(35, 22, transport="taxi")
        board.add_edge(35, 48, transport="taxi")
        board.add_edge(35, 36, transport="taxi")
        board.add_edge(35, 65, transport="taxi")

        board.add_edge(36, 35, transport="taxi")
        board.add_edge(36, 49, transport="taxi")
        board.add_edge(36, 37, transport="taxi")

        board.add_edge(37, 36, transport="taxi")
        board.add_edge(37, 23, transport="taxi")
        board.add_edge(37, 50, transport="taxi")
        board.add_edge(37, 24, transport="taxi")

        board.add_edge(38, 24, transport="taxi")
        board.add_edge(38, 25, transport="taxi")
        board.add_edge(38, 50, transport="taxi")
        board.add_edge(38, 51, transport="taxi")
        
        board.add_edge(39, 25, transport="taxi")
        board.add_edge(39, 26, transport="taxi")
        board.add_edge(39, 51, transport="taxi")
        board.add_edge(39, 52, transport="taxi")

        board.add_edge(40, 41, transport="taxi")
        board.add_edge(40, 27, transport="taxi")
        board.add_edge(40, 52, transport="taxi")
        board.add_edge(40, 53, transport="taxi")

        board.add_edge(41, 40, transport="taxi")
        board.add_edge(41, 28, transport="taxi")
        board.add_edge(41, 54, transport="taxi")
        board.add_edge(41, 29, transport="taxi")
        board.add_edge(41, 52, transport="bus")
        board.add_edge(41, 15, transport="bus")
        board.add_edge(41, 29, transport="bus")
        board.add_edge(41, 87, transport="bus")

        board.add_edge(42, 29, transport="taxi")
        board.add_edge(42, 30, transport="taxi")
        board.add_edge(42, 56, transport="taxi")
        board.add_edge(42, 72, transport="taxi")
        board.add_edge(42, 17, transport="bus")
        board.add_edge(42, 29, transport="bus")
        board.add_edge(42, 72, transport="bus")

        board.add_edge(43, 18, transport="taxi")
        board.add_edge(43, 31, transport="taxi")
        board.add_edge(43, 57, transport="taxi")

        board.add_edge(44, 31, transport="taxi")
        board.add_edge(44, 32, transport="taxi")
        board.add_edge(44, 58, transport="taxi")

        board.add_edge(45, 32, transport="taxi")
        board.add_edge(45, 58, transport="taxi")
        board.add_edge(45, 59, transport="taxi")
        board.add_edge(45, 46, transport="taxi")
        board.add_edge(45, 60, transport="taxi")

        board.add_edge(46, 33, transport="taxi")
        board.add_edge(46, 45, transport="taxi")
        board.add_edge(46, 61, transport="taxi")
        board.add_edge(46, 47, transport="taxi")
        board.add_edge(46, 1, transport="bus")
        board.add_edge(46, 58, transport="bus")
        board.add_edge(46, 34, transport="bus")
        board.add_edge(46, 78, transport="bus")
        board.add_edge(46, 1, transport="subway")
        board.add_edge(46, 74, transport="subway")
        board.add_edge(46, 13, transport="subway")
        board.add_edge(46, 79, transport="subway")

        board.add_edge(47, 46, transport="taxi")
        board.add_edge(47, 34, transport="taxi")
        board.add_edge(47, 62, transport="taxi")

        board.add_edge(48, 62, transport="taxi")
        board.add_edge(48, 34, transport="taxi")
        board.add_edge(48, 35, transport="taxi")
        board.add_edge(48, 63, transport="taxi")
        
        board.add_edge(49, 36, transport="taxi")
        board.add_edge(49, 50, transport="taxi")
        board.add_edge(49, 66, transport="taxi")

        board.add_edge(50, 49, transport="taxi")
        board.add_edge(50, 37, transport="taxi")
        board.add_edge(50, 38, transport="taxi")

        board.add_edge(51, 38, transport="taxi")
        board.add_edge(51, 39, transport="taxi")
        board.add_edge(51, 52, transport="taxi")
        board.add_edge(51, 67, transport="taxi")
        board.add_edge(51, 68, transport="taxi")

        board.add_edge(52, 51, transport="taxi")
        board.add_edge(52, 39, transport="taxi")
        board.add_edge(52, 40, transport="taxi")
        board.add_edge(52, 69, transport="taxi")
        board.add_edge(52, 67, transport="bus")
        board.add_edge(52, 86, transport="bus")
        board.add_edge(52, 41, transport="bus")
        board.add_edge(52, 13, transport="bus")

        board.add_edge(53, 40, transport="taxi")
        board.add_edge(53, 54, transport="taxi")
        board.add_edge(53, 69, transport="taxi")

        board.add_edge(54, 41, transport="taxi")
        board.add_edge(54, 53, transport="taxi")
        board.add_edge(54, 70, transport="taxi")
        board.add_edge(54, 55, transport="taxi")

        board.add_edge(55, 54, transport="taxi")
        board.add_edge(55, 71, transport="taxi")
        board.add_edge(55, 29, transport="bus")
        board.add_edge(55, 89, transport="bus")

        board.add_edge(56, 42, transport="taxi")
        board.add_edge(56, 91, transport="taxi")

        board.add_edge(57, 43, transport="taxi")
        board.add_edge(57, 58, transport="taxi")
        board.add_edge(57, 73, transport="taxi")

        board.add_edge(58, 57, transport="taxi")
        board.add_edge(58, 44, transport="taxi")
        board.add_edge(58, 74, transport="taxi")
        board.add_edge(58, 75, transport="taxi")
        board.add_edge(58, 59, transport="taxi")
        board.add_edge(58, 74, transport="bus")
        board.add_edge(58, 1, transport="bus")
        board.add_edge(58, 77, transport="bus")
        board.add_edge(58, 46, transport="bus")

        board.add_edge(59, 45, transport="taxi")
        board.add_edge(59, 58, transport="taxi")
        board.add_edge(59, 76, transport="taxi")

        board.add_edge(60, 45, transport="taxi")
        board.add_edge(60, 76, transport="taxi")
        board.add_edge(60, 61, transport="taxi")
        
        board.add_edge(61, 60, transport="taxi")
        board.add_edge(61, 76, transport="taxi")
        board.add_edge(61, 78, transport="taxi")
        board.add_edge(61, 46, transport="taxi")
        board.add_edge(61, 62, transport="taxi")

        board.add_edge(62, 61, transport="taxi")
        board.add_edge(62, 47, transport="taxi")
        board.add_edge(62, 79, transport="taxi")
        board.add_edge(62, 48, transport="taxi")

        board.add_edge(63, 79, transport="taxi")
        board.add_edge(63, 48, transport="taxi")
        board.add_edge(63, 64, transport="taxi")
        board.add_edge(63, 80, transport="taxi")
        board.add_edge(63, 34, transport="bus")
        board.add_edge(63, 79, transport="bus")
        board.add_edge(63, 65, transport="bus")
        board.add_edge(63, 100, transport="taxi")

        board.add_edge(64, 63, transport="taxi")
        board.add_edge(64, 65, transport="taxi")
        board.add_edge(64, 81, transport="taxi")

        board.add_edge(65, 64, transport="taxi")
        board.add_edge(65, 35, transport="taxi")
        board.add_edge(65, 66, transport="taxi")
        board.add_edge(65, 82, transport="taxi")
        board.add_edge(65, 63, transport="bus")
        board.add_edge(65, 22, transport="bus")
        board.add_edge(65, 67, transport="bus")
        board.add_edge(65, 82, transport="bus")

        board.add_edge(66, 65, transport="taxi")
        board.add_edge(66, 49, transport="taxi")
        board.add_edge(66, 82, transport="taxi")
        board.add_edge(66, 67, transport="taxi")

        board.add_edge(67, 66, transport="taxi")
        board.add_edge(67, 51, transport="taxi")
        board.add_edge(67, 84, transport="taxi")
        board.add_edge(67, 68, transport="taxi")
        board.add_edge(67, 65, transport="bus")
        board.add_edge(67, 82, transport="bus")
        board.add_edge(67, 23, transport="bus")
        board.add_edge(67, 102, transport="bus")
        board.add_edge(67, 52, transport="bus")
        board.add_edge(67, 13, transport="subway")
        board.add_edge(67, 63, transport="subway")
        board.add_edge(67, 111, transport="subway")
        board.add_edge(67, 89, transport="subway")

        board.add_edge(68, 67, transport="taxi")
        board.add_edge(68, 51, transport="taxi")
        board.add_edge(68, 85, transport="taxi")
        board.add_edge(68, 69, transport="taxi")

        board.add_edge(69, 68, transport="taxi")
        board.add_edge(69, 52, transport="taxi")
        board.add_edge(69, 86, transport="taxi")
        board.add_edge(69, 53, transport="taxi")

        board.add_edge(70, 54, transport="taxi")
        board.add_edge(70, 71, transport="taxi")
        board.add_edge(70, 87, transport="taxi")

        board.add_edge(71, 70, transport="taxi")
        board.add_edge(71, 55, transport="taxi")
        board.add_edge(71, 89, transport="taxi")
        board.add_edge(71, 72, transport="taxi")

        board.add_edge(72, 71, transport="taxi")
        board.add_edge(72, 42, transport="taxi")
        board.add_edge(72, 90, transport="taxi")
        board.add_edge(72, 91, transport="taxi")
        board.add_edge(72, 42, transport="bus")
        board.add_edge(72, 105, transport="bus")
        board.add_edge(72, 107, transport="bus")

        board.add_edge(73, 57, transport="taxi")
        board.add_edge(73, 74, transport="taxi")
        board.add_edge(73, 92, transport="taxi")

        board.add_edge(74, 73, transport="taxi")
        board.add_edge(74, 92, transport="taxi")
        board.add_edge(74, 58, transport="taxi")
        board.add_edge(74, 75, transport="taxi")
        board.add_edge(74, 58, transport="bus")
        board.add_edge(74, 94, transport="bus")
        board.add_edge(74, 46, transport="subway")

        board.add_edge(75, 74, transport="taxi")
        board.add_edge(75, 58, transport="taxi")
        board.add_edge(75, 59, transport="taxi")
        board.add_edge(75, 94, transport="taxi")

        board.add_edge(76, 77, transport="taxi")
        board.add_edge(76, 59, transport="taxi")

        board.add_edge(77, 76, transport="taxi")
        board.add_edge(77, 95, transport="taxi")
        board.add_edge(77, 96, transport="taxi")
        board.add_edge(77, 78, transport="taxi")
        board.add_edge(77, 58, transport="taxi")
        board.add_edge(77, 94, transport="taxi")
        board.add_edge(77, 78, transport="taxi")
        board.add_edge(77, 124, transport="taxi")

        board.add_edge(78, 77, transport="taxi")
        board.add_edge(78, 61, transport="taxi")
        board.add_edge(78, 97, transport="taxi")
        board.add_edge(78, 79, transport="taxi")
        board.add_edge(78, 77, transport="bus")
        board.add_edge(78, 61, transport="bus")
        board.add_edge(78, 79, transport="bus")

        board.add_edge(79, 78, transport="taxi")
        board.add_edge(79, 62, transport="taxi")
        board.add_edge(79, 98, transport="taxi")
        board.add_edge(79, 63, transport="taxi")
        board.add_edge(79, 78, transport="bus")
        board.add_edge(79, 63, transport="bus")
        board.add_edge(79, 93, transport="subway")
        board.add_edge(79, 46, transport="subway")
        board.add_edge(79, 111, transport="subway")
        board.add_edge(79, 67, transport="subway")

        board.add_edge(80, 63, transport="taxi")
        board.add_edge(80, 99, transport="taxi")
        board.add_edge(80, 100, transport="taxi")

        board.add_edge(81, 64, transport="taxi")
        board.add_edge(81, 82, transport="taxi")
        board.add_edge(81, 100, transport="taxi")

        board.add_edge(82, 81, transport="taxi")
        board.add_edge(82, 65, transport="taxi")
        board.add_edge(82, 66, transport="taxi")
        board.add_edge(82, 101, transport="taxi")
        board.add_edge(82, 100, transport="taxi")
        board.add_edge(82, 65, transport="taxi")
        board.add_edge(82, 67, transport="taxi")
        board.add_edge(82, 140, transport="taxi")

        board.add_edge(83, 101, transport="taxi")
        board.add_edge(83, 102, transport="taxi")

        board.add_edge(84, 67, transport="taxi")
        board.add_edge(84, 85, transport="taxi")

        board.add_edge(85, 84, transport="taxi")
        board.add_edge(85, 68, transport="taxi")
        board.add_edge(85, 103, transport="taxi")

        board.add_edge(86, 103, transport="taxi")
        board.add_edge(86, 69, transport="taxi")
        board.add_edge(86, 104, transport="taxi")
        board.add_edge(86, 52, transport="bus")
        board.add_edge(86, 102, transport="bus")
        board.add_edge(86, 116, transport="bus")
        board.add_edge(86, 87, transport="bus")

        board.add_edge(87, 70, transport="taxi")
        board.add_edge(87, 88, transport="taxi")
        board.add_edge(87, 86, transport="bus")
        board.add_edge(87, 41, transport="bus")
        board.add_edge(87, 105, transport="bus")

        board.add_edge(88, 87, transport="taxi")
        board.add_edge(88, 104, transport="taxi")
        board.add_edge(88, 117, transport="taxi")
        board.add_edge(88, 105, transport="taxi")
        board.add_edge(88, 89, transport="taxi")

        board.add_edge(89, 88, transport="taxi")
        board.add_edge(89, 71, transport="taxi")
        board.add_edge(89, 105, transport="taxi")
        board.add_edge(89, 55, transport="bus")
        board.add_edge(89, 105, transport="bus")
        board.add_edge(89, 67, transport="subway")
        board.add_edge(89, 140, transport="subway")
        board.add_edge(89, 13, transport="subway")
        board.add_edge(89, 159, transport="subway")

        board.add_edge(90, 72, transport="taxi")
        board.add_edge(90, 105, transport="taxi")
        board.add_edge(90, 91, transport="taxi")
        
        board.add_edge(91, 90, transport="taxi")
        board.add_edge(91, 72, transport="taxi")
        board.add_edge(91, 56, transport="taxi")
        board.add_edge(91, 105, transport="taxi")
        board.add_edge(91, 107, transport="taxi")

        board.add_edge(92, 73, transport="taxi")
        board.add_edge(92, 93, transport="taxi")
        board.add_edge(92, 74, transport="taxi")

        board.add_edge(93, 92, transport="taxi")
        board.add_edge(93, 94, transport="taxi")
        board.add_edge(93, 94, transport="bus")
        board.add_edge(93, 79, transport="subway")

        board.add_edge(94, 93, transport="taxi")
        board.add_edge(94, 95, transport="taxi")
        board.add_edge(94, 93, transport="bus")
        board.add_edge(94, 74, transport="bus")
        board.add_edge(94, 77, transport="bus")

        board.add_edge(95, 94, transport="taxi")
        board.add_edge(95, 122, transport="taxi")
        board.add_edge(95, 77, transport="taxi")

        board.add_edge(96, 77, transport="taxi")
        board.add_edge(96, 97, transport="taxi")
        board.add_edge(96, 109, transport="taxi")

        board.add_edge(97, 96, transport="taxi")
        board.add_edge(97, 78, transport="taxi")
        board.add_edge(97, 109, transport="taxi")
        board.add_edge(97, 98, transport="taxi")

        board.add_edge(98, 97, transport="taxi")
        board.add_edge(98, 79, transport="taxi")
        board.add_edge(98, 99, transport="taxi")
        board.add_edge(98, 110, transport="taxi")

        board.add_edge(99, 98, transport="taxi")
        board.add_edge(99, 80, transport="taxi")
        board.add_edge(99, 110, transport="taxi")

        board.add_edge(100, 80, transport="taxi")
        board.add_edge(100, 81, transport="taxi")
        board.add_edge(100, 101, transport="taxi")
        board.add_edge(100, 112, transport="taxi")
        board.add_edge(100, 113, transport="taxi")
        board.add_edge(100, 63, transport="bus")
        board.add_edge(100, 82, transport="bus")
        board.add_edge(100, 111, transport="bus")

        board.add_edge(101, 82, transport="taxi")
        board.add_edge(101, 83, transport="taxi")
        board.add_edge(101, 100, transport="taxi")
        board.add_edge(101, 114, transport="taxi")

        board.add_edge(102, 83, transport="taxi")
        board.add_edge(102, 103, transport="taxi")
        board.add_edge(102, 115, transport="taxi")
        board.add_edge(102, 67, transport="bus")
        board.add_edge(102, 86, transport="bus")
        board.add_edge(102, 127, transport="bus")

        board.add_edge(103, 85, transport="taxi")
        board.add_edge(103, 86, transport="taxi")
        board.add_edge(103, 102, transport="taxi")

        board.add_edge(104, 86, transport="taxi")
        board.add_edge(104, 88, transport="taxi")
        board.add_edge(104, 116, transport="taxi")

        board.add_edge(105, 88, transport="taxi")
        board.add_edge(105, 89, transport="taxi")
        board.add_edge(105, 90, transport="taxi")
        board.add_edge(105, 106, transport="taxi")
        board.add_edge(105, 118, transport="taxi")
        board.add_edge(105, 87, transport="bus")
        board.add_edge(105, 89, transport="bus")
        board.add_edge(105, 72, transport="bus")
        board.add_edge(105, 118, transport="bus")

        board.add_edge(106, 105, transport="taxi")
        board.add_edge(106, 107, transport="taxi")

        board.add_edge(107, 91, transport="taxi")
        board.add_edge(107, 106, transport="taxi")
        board.add_edge(107, 119, transport="taxi")
        board.add_edge(107, 72, transport="taxi")
        board.add_edge(107, 161, transport="taxi")

        board.add_edge(109, 96, transport="taxi")
        board.add_edge(109, 97, transport="taxi")
        board.add_edge(109, 110, transport="taxi")
        board.add_edge(109, 124, transport="taxi")

        board.add_edge(110, 98, transport="taxi")
        board.add_edge(110, 99, transport="taxi")
        board.add_edge(110, 109, transport="taxi")
        board.add_edge(110, 111, transport="taxi")

        board.add_edge(111, 110, transport="taxi")
        board.add_edge(111, 112, transport="taxi")
        board.add_edge(111, 124, transport="taxi")
        board.add_edge(111, 100, transport="bus")
        board.add_edge(111, 124, transport="bus")
        board.add_edge(111, 79, transport="subway")
        board.add_edge(111, 153, transport="subway")
        board.add_edge(111, 163, transport="subway")

        board.add_edge(112, 100, transport="taxi")
        board.add_edge(112, 111, transport="taxi")
        board.add_edge(112, 125, transport="taxi")

        board.add_edge(113, 100, transport="taxi")
        board.add_edge(113, 114, transport="taxi")
        board.add_edge(113, 125, transport="taxi")

        board.add_edge(114, 101, transport="taxi")
        board.add_edge(114, 113, transport="taxi")
        board.add_edge(114, 115, transport="taxi")
        board.add_edge(114, 126, transport="taxi")
        board.add_edge(114, 131, transport="taxi")
        board.add_edge(114, 132, transport="taxi")

        board.add_edge(115, 102, transport="taxi")
        board.add_edge(115, 114, transport="taxi")
        board.add_edge(115, 126, transport="taxi")
        board.add_edge(115, 127, transport="taxi")

        board.add_edge(116, 104, transport="taxi")
        board.add_edge(116, 117, transport="taxi")
        board.add_edge(116, 127, transport="taxi")
        board.add_edge(116, 128, transport="taxi")
        board.add_edge(116, 86, transport="bus")
        board.add_edge(116, 118, transport="bus")
        board.add_edge(116, 127, transport="bus")
        board.add_edge(116, 142, transport="bus")

        board.add_edge(117, 88, transport="taxi")
        board.add_edge(117, 116, transport="taxi")
        board.add_edge(117, 118, transport="taxi")
        board.add_edge(117, 129, transport="taxi")

        board.add_edge(118, 105, transport="taxi")
        board.add_edge(118, 117, transport="taxi")
        board.add_edge(118, 119, transport="taxi")
        board.add_edge(118, 105, transport="bus")
        board.add_edge(118, 116, transport="bus")
        board.add_edge(118, 135, transport="bus")

        board.add_edge(119, 107, transport="taxi")
        board.add_edge(119, 118, transport="taxi")
        board.add_edge(119, 136, transport="taxi")

        board.add_edge(120, 121, transport="taxi")
        board.add_edge(120, 121, transport="taxi")

        board.add_edge(121, 120, transport="taxi")
        board.add_edge(121, 122, transport="taxi")
        board.add_edge(121, 145, transport="taxi")
        
        board.add_edge(122, 95, transport="taxi")
        board.add_edge(122, 121, transport="taxi")
        board.add_edge(122, 123, transport="taxi")
        board.add_edge(122, 146, transport="taxi")
        board.add_edge(122, 123, transport="bus")
        board.add_edge(122, 144, transport="bus")

        board.add_edge(123, 122, transport="taxi")
        board.add_edge(123, 124, transport="taxi")
        board.add_edge(123, 137, transport="taxi")
        board.add_edge(123, 148, transport="taxi")
        board.add_edge(123, 149, transport="taxi")
        board.add_edge(123, 122, transport="bus")
        board.add_edge(123, 124, transport="bus")
        board.add_edge(123, 144, transport="bus")
        board.add_edge(123, 165, transport="bus")

        board.add_edge(124, 109, transport="taxi")
        board.add_edge(124, 111, transport="taxi")
        board.add_edge(124, 123, transport="taxi")
        board.add_edge(124, 130, transport="taxi")
        board.add_edge(124, 138, transport="taxi")
        board.add_edge(124, 77, transport="bus")
        board.add_edge(124, 111, transport="bus")
        board.add_edge(124, 123, transport="bus")
        board.add_edge(124, 153, transport="bus")

        board.add_edge(125, 112, transport="taxi")
        board.add_edge(125, 113, transport="taxi")
        board.add_edge(125, 131, transport="taxi")

        board.add_edge(126, 114, transport="taxi")
        board.add_edge(126, 115, transport="taxi")
        board.add_edge(126, 140, transport="taxi")

        board.add_edge(127, 115, transport="taxi")
        board.add_edge(127, 116, transport="taxi")
        board.add_edge(127, 133, transport="taxi")
        board.add_edge(127, 134, transport="taxi")
        board.add_edge(127, 102, transport="bus")
        board.add_edge(127, 116, transport="bus")
        board.add_edge(127, 133, transport="bus")

        board.add_edge(128, 116, transport="taxi")
        board.add_edge(128, 129, transport="taxi")
        board.add_edge(128, 134, transport="taxi")
        board.add_edge(128, 142, transport="taxi")

        board.add_edge(129, 117, transport="taxi")
        board.add_edge(129, 128, transport="taxi")
        board.add_edge(129, 135, transport="taxi")
        board.add_edge(129, 142, transport="taxi")
        board.add_edge(129, 143, transport="taxi")

        board.add_edge(130, 124, transport="taxi")
        board.add_edge(130, 131, transport="taxi")
        board.add_edge(130, 139, transport="taxi")

        board.add_edge(131, 114, transport="taxi")
        board.add_edge(131, 125, transport="taxi")
        board.add_edge(131, 130, transport="taxi")

        board.add_edge(132, 114, transport="taxi")
        board.add_edge(132, 140, transport="taxi")

        board.add_edge(133, 127, transport="taxi")
        board.add_edge(133, 140, transport="taxi")
        board.add_edge(133, 141, transport="taxi")
        board.add_edge(133, 127, transport="bus")
        board.add_edge(133, 140, transport="bus")
        board.add_edge(133, 157, transport="bus")

        board.add_edge(134, 127, transport="taxi")
        board.add_edge(134, 128, transport="taxi")
        board.add_edge(134, 141, transport="taxi")
        board.add_edge(134, 142, transport="taxi")

        board.add_edge(135, 129, transport="taxi")
        board.add_edge(135, 136, transport="taxi")
        board.add_edge(135, 143, transport="taxi")
        board.add_edge(135, 161, transport="taxi")
        board.add_edge(135, 118, transport="bus")
        board.add_edge(135, 159, transport="bus")
        board.add_edge(135, 161, transport="bus")

        board.add_edge(136, 119, transport="taxi")
        board.add_edge(136, 135, transport="taxi")
        board.add_edge(136, 162, transport="taxi")

        board.add_edge(137, 123, transport="taxi")
        board.add_edge(137, 147, transport="taxi")

        board.add_edge(138, 124, transport="taxi")
        board.add_edge(138, 150, transport="taxi")
        board.add_edge(138, 152, transport="taxi")

        board.add_edge(139, 130, transport="taxi")
        board.add_edge(139, 140, transport="taxi")
        board.add_edge(139, 153, transport="taxi")
        board.add_edge(139, 154, transport="taxi")

        board.add_edge(140, 126, transport="taxi")
        board.add_edge(140, 132, transport="taxi")
        board.add_edge(140, 133, transport="taxi")
        board.add_edge(140, 139, transport="taxi")
        board.add_edge(140, 154, transport="taxi")
        board.add_edge(140, 156, transport="taxi")
        board.add_edge(140, 82, transport="bus")
        board.add_edge(140, 133, transport="bus")
        board.add_edge(140, 154, transport="bus")
        board.add_edge(140, 156, transport="bus")
        board.add_edge(140, 89, transport="subway")
        board.add_edge(140, 153, transport="subway")
        board.add_edge(140, 159, transport="subway")

        board.add_edge(141, 133, transport="taxi")
        board.add_edge(141, 134, transport="taxi")
        board.add_edge(141, 142, transport="taxi")
        board.add_edge(141, 158, transport="taxi")

        board.add_edge(142, 128, transport="taxi")
        board.add_edge(142, 129, transport="taxi")
        board.add_edge(142, 134, transport="taxi")
        board.add_edge(142, 141, transport="taxi")
        board.add_edge(142, 143, transport="taxi")
        board.add_edge(142, 158, transport="taxi")
        board.add_edge(142, 159, transport="taxi")
        board.add_edge(142, 116, transport="bus")
        board.add_edge(142, 157, transport="bus")
        board.add_edge(142, 159, transport="bus")

        board.add_edge(143, 135, transport="taxi")
        board.add_edge(143, 142, transport="taxi")
        board.add_edge(143, 159, transport="taxi")
        board.add_edge(143, 160, transport="taxi")

        board.add_edge(144, 120, transport="taxi")
        board.add_edge(144, 145, transport="taxi")
        board.add_edge(144, 177, transport="taxi")
        board.add_edge(144, 122, transport="bus")
        board.add_edge(144, 123, transport="bus")
        board.add_edge(144, 163, transport="bus")

        board.add_edge(145, 121, transport="taxi")
        board.add_edge(145, 144, transport="taxi")
        board.add_edge(145, 146, transport="taxi")

        board.add_edge(146, 122, transport="taxi")
        board.add_edge(146, 145, transport="taxi")
        board.add_edge(146, 147, transport="taxi")
        board.add_edge(146, 163, transport="taxi")

        board.add_edge(147, 137, transport="taxi")
        board.add_edge(147, 146, transport="taxi")
        board.add_edge(147, 164, transport="taxi")

        board.add_edge(148, 123, transport="taxi")
        board.add_edge(148, 149, transport="taxi")
        board.add_edge(148, 164, transport="taxi")

        board.add_edge(149, 123, transport="taxi")
        board.add_edge(149, 148, transport="taxi")
        board.add_edge(149, 150, transport="taxi")
        board.add_edge(149, 165, transport="taxi")

        board.add_edge(150, 138, transport="taxi")
        board.add_edge(150, 149, transport="taxi")
        board.add_edge(150, 151, transport="taxi")

        board.add_edge(151, 150, transport="taxi")
        board.add_edge(151, 152, transport="taxi")
        board.add_edge(151, 165, transport="taxi")
        board.add_edge(151, 166, transport="taxi")

        board.add_edge(152, 138, transport="taxi")
        board.add_edge(152, 151, transport="taxi")
        board.add_edge(152, 153, transport="taxi")

        board.add_edge(153, 139, transport="taxi")
        board.add_edge(153, 152, transport="taxi")
        board.add_edge(153, 154, transport="taxi")
        board.add_edge(153, 166, transport="taxi")
        board.add_edge(153, 167, transport="taxi")
        board.add_edge(153, 124, transport="bus")
        board.add_edge(153, 154, transport="bus")
        board.add_edge(153, 180, transport="bus")
        board.add_edge(153, 184, transport="bus")
        board.add_edge(153, 111, transport="subway")
        board.add_edge(153, 140, transport="subway")
        board.add_edge(153, 165, transport="subway")
        board.add_edge(153, 185, transport="subway")

        board.add_edge(154, 139, transport="taxi")
        board.add_edge(154, 140, transport="taxi")
        board.add_edge(154, 153, transport="taxi")
        board.add_edge(154, 155, transport="taxi")
        board.add_edge(154, 140, transport="bus")
        board.add_edge(154, 153, transport="bus")
        board.add_edge(154, 156, transport="bus")

        board.add_edge(155, 154, transport="taxi")
        board.add_edge(155, 156, transport="taxi")
        board.add_edge(155, 167, transport="taxi")
        board.add_edge(155, 168, transport="taxi")

        board.add_edge(156, 140, transport="taxi")
        board.add_edge(156, 155, transport="taxi")
        board.add_edge(156, 157, transport="taxi")
        board.add_edge(156, 169, transport="taxi")
        board.add_edge(156, 140, transport="bus")
        board.add_edge(156, 154, transport="bus")
        board.add_edge(156, 157, transport="bus")
        board.add_edge(156, 184, transport="bus")

        board.add_edge(157, 156, transport="taxi")
        board.add_edge(157, 158, transport="taxi")
        board.add_edge(157, 170, transport="taxi")
        board.add_edge(157, 133, transport="bus")
        board.add_edge(157, 142, transport="bus")
        board.add_edge(157, 156, transport="bus")
        board.add_edge(157, 185, transport="bus")

        board.add_edge(158, 141, transport="taxi")
        board.add_edge(158, 142, transport="taxi")
        board.add_edge(158, 157, transport="taxi")
        board.add_edge(158, 171, transport="taxi")

        board.add_edge(159, 142, transport="taxi")
        board.add_edge(159, 143, transport="taxi")
        board.add_edge(159, 160, transport="taxi")
        board.add_edge(159, 172, transport="taxi")
        board.add_edge(159, 188, transport="taxi")
        board.add_edge(159, 135, transport="bus")
        board.add_edge(159, 142, transport="bus")
        board.add_edge(159, 161, transport="bus")
        board.add_edge(159, 187, transport="bus")
        board.add_edge(159, 199, transport="bus")
        board.add_edge(159, 89, transport="subway")
        board.add_edge(159, 140, transport="subway")
        board.add_edge(159, 185, transport="subway")

        board.add_edge(160, 143, transport="taxi")
        board.add_edge(160, 159, transport="taxi")
        board.add_edge(160, 161, transport="taxi")
        board.add_edge(160, 173, transport="taxi")

        board.add_edge(161, 135, transport="taxi")
        board.add_edge(161, 160, transport="taxi")
        board.add_edge(161, 174, transport="taxi")
        board.add_edge(161, 135, transport="bus")
        board.add_edge(161, 136, transport="bus")
        board.add_edge(161, 159, transport="bus")
        board.add_edge(161, 199, transport="bus")

        board.add_edge(162, 136, transport="taxi")
        board.add_edge(162, 175, transport="taxi")

        board.add_edge(163, 146, transport="taxi")
        board.add_edge(163, 164, transport="taxi")
        board.add_edge(163, 177, transport="taxi")
        board.add_edge(163, 144, transport="bus")
        board.add_edge(163, 176, transport="bus")
        board.add_edge(163, 191, transport="bus")
        board.add_edge(163, 111, transport="subway")
        board.add_edge(163, 153, transport="subway")

        board.add_edge(164, 147, transport="taxi")
        board.add_edge(164, 148, transport="taxi")
        board.add_edge(164, 163, transport="taxi")
        board.add_edge(164, 179, transport="taxi")

        board.add_edge(165, 149, transport="taxi")
        board.add_edge(165, 151, transport="taxi")
        board.add_edge(165, 179, transport="taxi")
        board.add_edge(165, 180, transport="taxi")
        board.add_edge(165, 123, transport="bus")
        board.add_edge(165, 180, transport="bus")
        board.add_edge(165, 191, transport="bus")

        board.add_edge(166, 151, transport="taxi")
        board.add_edge(166, 153, transport="taxi")
        board.add_edge(166, 181, transport="taxi")
        board.add_edge(166, 183, transport="taxi")

        board.add_edge(167, 153, transport="taxi")
        board.add_edge(167, 155, transport="taxi")
        board.add_edge(167, 168, transport="taxi")
        board.add_edge(167, 183, transport="taxi")

        board.add_edge(168, 155, transport="taxi")
        board.add_edge(168, 167, transport="taxi")
        board.add_edge(168, 184, transport="taxi")

        board.add_edge(169, 156, transport="taxi")
        board.add_edge(169, 184, transport="taxi")

        board.add_edge(170, 157, transport="taxi")
        board.add_edge(170, 171, transport="taxi")
        board.add_edge(170, 185, transport="taxi")

        board.add_edge(171, 158, transport="taxi")
        board.add_edge(171, 170, transport="taxi")
        board.add_edge(171, 172, transport="taxi")
        board.add_edge(171, 186, transport="taxi")

        board.add_edge(172, 159, transport="taxi")
        board.add_edge(172, 171, transport="taxi")
        board.add_edge(172, 187, transport="taxi")

        board.add_edge(173, 160, transport="taxi")
        board.add_edge(173, 174, transport="taxi")
        board.add_edge(173, 188, transport="taxi")
        board.add_edge(173, 200, transport="taxi")

        board.add_edge(174, 161, transport="taxi")
        board.add_edge(174, 173, transport="taxi")
        board.add_edge(174, 175, transport="taxi")

        board.add_edge(175, 162, transport="taxi")
        board.add_edge(175, 174, transport="taxi")
        board.add_edge(175, 200, transport="taxi")

        board.add_edge(176, 177, transport="taxi")
        board.add_edge(176, 189, transport="taxi")
        board.add_edge(176, 163, transport="bus")
        board.add_edge(176, 190, transport="bus")

        board.add_edge(177, 144, transport="taxi")
        board.add_edge(177, 163, transport="taxi")
        board.add_edge(177, 176, transport="taxi")

        board.add_edge(178, 164, transport="taxi")
        board.add_edge(178, 189, transport="taxi")
        board.add_edge(178, 191, transport="taxi")

        board.add_edge(179, 164, transport="taxi")
        board.add_edge(179, 165, transport="taxi")
        board.add_edge(179, 191, transport="taxi")

        board.add_edge(180, 165, transport="taxi")
        board.add_edge(180, 181, transport="taxi")
        board.add_edge(180, 193, transport="taxi")
        board.add_edge(180, 165, transport="bus")
        board.add_edge(180, 190, transport="bus")
        board.add_edge(180, 181, transport="bus")
        board.add_edge(180, 184, transport="bus")

        board.add_edge(181, 166, transport="taxi")
        board.add_edge(181, 180, transport="taxi")
        board.add_edge(181, 182, transport="taxi")
        board.add_edge(181, 193, transport="taxi")

        board.add_edge(182, 181, transport="taxi")
        board.add_edge(182, 183, transport="taxi")
        board.add_edge(182, 195, transport="taxi")

        board.add_edge(183, 166, transport="taxi")
        board.add_edge(183, 167, transport="taxi")
        board.add_edge(183, 182, transport="taxi")
        board.add_edge(183, 184, transport="taxi")
        board.add_edge(183, 196, transport="taxi")

        board.add_edge(184, 168, transport="taxi")
        board.add_edge(184, 169, transport="taxi")
        board.add_edge(184, 183, transport="taxi")
        board.add_edge(184, 185, transport="taxi")
        board.add_edge(184, 196, transport="taxi")
        board.add_edge(184, 197, transport="taxi")
        board.add_edge(184, 153, transport="bus")
        board.add_edge(184, 156, transport="bus")
        board.add_edge(184, 180, transport="bus")
        board.add_edge(184, 185, transport="bus")

        board.add_edge(185, 170, transport="taxi")
        board.add_edge(185, 184, transport="taxi")
        board.add_edge(185, 186, transport="taxi")
        board.add_edge(185, 157, transport="bus")
        board.add_edge(185, 184, transport="bus")
        board.add_edge(185, 187, transport="bus")
        board.add_edge(185, 199, transport="bus")
        board.add_edge(185, 153, transport="subway")
        board.add_edge(185, 159, transport="subway")

        board.add_edge(186, 171, transport="taxi")
        board.add_edge(186, 185, transport="taxi")
        board.add_edge(186, 198, transport="taxi")

        board.add_edge(187, 172, transport="taxi")
        board.add_edge(187, 188, transport="taxi")
        board.add_edge(187, 198, transport="taxi")
        board.add_edge(187, 159, transport="bus")
        board.add_edge(187, 185, transport="bus")
        board.add_edge(187, 199, transport="bus")

        board.add_edge(188, 159, transport="taxi")
        board.add_edge(188, 173, transport="taxi")
        board.add_edge(188, 187, transport="taxi")
        board.add_edge(188, 199, transport="taxi")

        board.add_edge(189, 176, transport="taxi")
        board.add_edge(189, 178, transport="taxi")
        board.add_edge(189, 190, transport="taxi")

        board.add_edge(190, 189, transport="taxi")
        board.add_edge(190, 191, transport="taxi")
        board.add_edge(190, 176, transport="bus")
        board.add_edge(190, 180, transport="bus")
        board.add_edge(190, 191, transport="bus")

        board.add_edge(191, 178, transport="taxi")
        board.add_edge(191, 179, transport="taxi")
        board.add_edge(191, 190, transport="taxi")
        board.add_edge(191, 192, transport="taxi")
        board.add_edge(191, 163, transport="bus")
        board.add_edge(191, 165, transport="bus")
        board.add_edge(191, 190, transport="bus")

        board.add_edge(192, 191, transport="taxi")
        board.add_edge(192, 194, transport="taxi")

        board.add_edge(193, 180, transport="taxi")
        board.add_edge(193, 181, transport="taxi")
        board.add_edge(193, 194, transport="taxi")

        board.add_edge(194, 192, transport="taxi")
        board.add_edge(194, 193, transport="taxi")
        board.add_edge(194, 195, transport="taxi")

        board.add_edge(195, 182, transport="taxi")
        board.add_edge(195, 194, transport="taxi")
        board.add_edge(195, 197, transport="taxi")

        board.add_edge(196, 183, transport="taxi")
        board.add_edge(196, 184, transport="taxi")
        board.add_edge(196, 197, transport="taxi")

        board.add_edge(197, 184, transport="taxi")
        board.add_edge(197, 195, transport="taxi")
        board.add_edge(197, 196, transport="taxi")

        board.add_edge(198, 186, transport="taxi")
        board.add_edge(198, 187, transport="taxi")

        board.add_edge(199, 188, transport="taxi")
        board.add_edge(199, 200, transport="taxi")
        board.add_edge(199, 159, transport="bus")
        board.add_edge(199, 161, transport="bus")
        board.add_edge(199, 185, transport="bus")
        board.add_edge(199, 187, transport="bus")

        board.add_edge(200, 173, transport="taxi")
        board.add_edge(200, 175, transport="taxi")
        board.add_edge(200, 199, transport="taxi")
        
        return board
        
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)  # Use the new Gym reset functionality
        valid_nodes = set(self.board.nodes) - {108}

        self.mister_x_position = np.random.choice(list(valid_nodes))
        self.detectives_positions = [np.random.choice(list(valid_nodes)) for _ in range(6)]
        self.mister_x_tickets = {"taxi": 20, "bus": 20, "subway": 20}
        self.detectives_tickets = [{"taxi": 10, "bus": 8, "subway": 4} for _ in range(6)]
        self.current_turn = 1
        self.done = False
        return self.get_observation(), {}  # Return observation and empty info dictionary

    
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

        print(player_id, destination, transport_type)

        # Validate action
        if player_id == 0:
            current_position = self.mister_x_position
            tickets = self.mister_x_tickets
        else:
            current_position = self.detectives_positions[player_id]
            tickets = self.detectives_tickets[player_id]

        valid_moves = [
            (dest, data["transport"])
            for dest, data in self.board[current_position].items()
            if tickets[data["transport"]] > 0
        ]

        # Check if the destination is valid
        if not self.board.has_edge(current_position, destination):
            raise ValueError(f"Invalid move: No edge between {current_position} and {destination}.")
        if self.board[current_position][destination]["transport"] != transport_type:
            raise ValueError(f"Invalid transport: {transport_type} not valid between {current_position} and {destination}.")
        if tickets[transport_type] <= 0:
            raise ValueError(f"Insufficient {transport_type} tickets for player {player_id}.")
            # Check if the action is valid
        if (destination, transport_type) not in valid_moves:
            raise ValueError(
                f"Invalid move for player {player_id}: Cannot move to {destination} via {transport_type} from {current_position}."
            )

        # Update position and deduct ticket
        if player_id == 0:
            self.mister_x_position = destination
            self.mister_x_tickets[transport_type] -= 1
        else:
            self.detectives_positions[player_id - 1] = destination
            self.detectives_tickets[player_id - 1][transport_type] -= 1

        # Calculate reward
        reward = self.calculate_reward(player_id, destination)

        # Check if the game is over
        if player_id == 5:  # Last detective
            self.current_turn += 1

        self.done = self.check_done()

        observation = self.get_observation()
        reward = self.calculate_reward(player_id, destination)

        # Split done into terminated and truncated
        terminated = self.done  # Ended because of success/failure
        truncated = self.current_turn >= 22  # Ended because max turns reached

        return observation, reward, terminated, truncated, {"turn": self.current_turn}

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
        encoded_state = self.encode_state(state)
    
        # Normalize positions to fit within [0, 1] if observation_space expects it
        encoded_state /= 200  # Assuming max location index is 200
        return encoded_state
    
    def encode_state(self, state):
        # Encode the state into a numerical format for RL agents
        # Example: Flatten positions, tickets, and turn into a vector
        encoded_state = np.zeros(500, dtype=np.float32)  # Example fixed-size vector
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
    
    def get_valid_actions(self, player_id):
        """
        Get all valid actions for a player based on their current position.

        Parameters:
            player_id: 0 for Mister X, 1-5 for detectives.

        Returns:
            List of valid actions as (destination, transport_type).
        """
        if player_id == 0:  # Mister X
            current_position = self.mister_x_position
            tickets = self.mister_x_tickets
        else:  # Detective
            current_position = self.detectives_positions[player_id]
            print("cur pos", current_position)
            tickets = self.detectives_tickets[player_id]

        # Get all valid moves from the current position
        valid_moves = [
            (dest, data["transport"])
            for dest, data in self.board[current_position].items()
            if tickets[data["transport"]] > 0
        ]

        return valid_moves
    
    def render(self, mode="human"):
        """
        Visualize the current state of the board and agent positions.

        Parameters:
            mode: The rendering mode (default is "human").
        """
        # Create a color map for transportation types
        if mode is None:
            mode = self.render_mode

        if mode == "human":
            # Render using matplotlib as visual output
            color_map = {"taxi": "yellow", "bus": "blue", "subway": "green"}
            edge_colors = [
                color_map[self.board[u][v]["transport"]] for u, v in self.board.edges
            ]

            # Draw the graph
            pos = nx.spring_layout(self.board, seed=42)  # Fixed layout for consistency
            plt.figure(figsize=(12, 8))
            nx.draw(
                self.board,
                pos,
                node_size=200,
                with_labels=True,
                edge_color=edge_colors,
                edge_cmap=plt.cm.Paired,
            )

            # Highlight the positions of Mister X and detectives
            nx.draw_networkx_nodes(
                self.board,
                pos,
                nodelist=[self.mister_x_position],
                node_color="black",
                node_size=300,
                label="Mister X",
            )
            nx.draw_networkx_nodes(
                self.board,
                pos,
                nodelist=self.detectives_positions,
                node_color="red",
                node_size=300,
                label="Detectives",
            )

            # Add legend
            plt.legend(
                ["Taxi", "Bus", "Subway", "Mister X", "Detectives"], loc="upper left"
            )
            plt.title(f"Turn: {self.current_turn}")
            plt.show()

