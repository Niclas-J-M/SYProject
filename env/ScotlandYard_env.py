import gym
from gym import spaces
import numpy as np
import networkx as nx
from gym.spaces import MultiDiscrete


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
        board.add_edge(107, 136, transport="taxi")

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


        return board
        
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)  # Use the new Gym reset functionality
        self.mister_x_position = np.random.randint(1, 200)
        self.detectives_positions = [np.random.randint(1, 200) for _ in range(5)]
        self.mister_x_tickets = {"taxi": 4, "bus": 3, "subway": 3}
        self.detectives_tickets = [{"taxi": 10, "bus": 8, "subway": 4} for _ in range(5)]
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
        transport_map = {0: "taxi", 1: "bus", 2: "subway"}  # Map transport_type to string
        transport_type = transport_map[transport_type]

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