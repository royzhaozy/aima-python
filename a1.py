"""
Assignment 1 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import time
import random
import numpy
import unittest
from search import EightPuzzle, YPuzzle, astar_search, astar_manhattan_search

def make_rand_8puzzle():
    """ Returns a new instance of an EightPuzzle problem with a random initial
    state that is solvable """
    tiles = list(range(0,9))
    random.shuffle(tiles)
    puzzle = EightPuzzle(tuple(tiles))
    while (not puzzle.check_solvability(puzzle.initial)):
        random.shuffle(tiles)
        puzzle = EightPuzzle(tuple(tiles))
    return puzzle


def make_rand_Ypuzzle():
    """ Returns a new instance of an EightPuzzle problem with a random initial
    state that is solvable """
    tiles = list(range(0,9))
    random.shuffle(tiles)
    puzzle = YPuzzle(tuple(tiles))
    while (not puzzle.check_solvability(puzzle.initial)):
        random.shuffle(tiles)
        puzzle = YPuzzle(tuple(tiles))
    return puzzle

class Question1(unittest.TestCase):
    def test_check_solvability(self):
        """ Checks if the generated puzzle is always solvable """
        for i in range (0,10):
            game = make_rand_8puzzle()
            self.assertTrue(game.check_solvability(game.initial))
            print("test " + str(i+1) + " passed")


def Question2():
    for i in range (0,10):
        print("============================== 8 Puzzle " + str(i + 1) +" ===============================")
        game = make_rand_8puzzle()
        game.display(game.initial)
        start_time = time.time()
        default_search, default_node_removed = astar_search(game)
        elapsed_time = time.time() - start_time
        default_solution_len = len(default_search.solution())
        print("\n=========================== Default Heuristic ===========================")
        print("Problem solved with default heuristic in " + str(elapsed_time) + " seconds")
        print("Problem solved with default heuristic in " + str(default_solution_len) + " steps")
        print("Problem solved with default heuristic with " + str(default_node_removed) + " nodes removed")
        
        start_time = time.time()
        manhattan_search, manhattan_node_removed = astar_manhattan_search(game)
        elapsed_time = time.time() - start_time
        manhattan_solution_len = len(manhattan_search.solution())
        print("\n========================== Manhattan Heuristic ==========================")
        print("Problem solved with Manhattan heuristic in " + str(elapsed_time) + " seconds")
        print("Problem solved with Manhattan heuristic in " + str(manhattan_solution_len) + " steps")
        print("Problem solved with Manhattan heuristic with " + str(manhattan_node_removed) + " nodes removed\n\n")


def Question3():
    for i in range(0,10):
        print("============================== Y Puzzle #" + str(i + 1) +" ==============================")
        game = make_rand_Ypuzzle()
        game.display(game.initial)
        start_time = time.time()
        default_search, default_node_removed = astar_search(game)
        elapsed_time = time.time() - start_time
        default_solution_len = len(default_search.solution())
        print("\n=========================== Default Heuristic ===========================")
        print("Problem solved with default heuristic in " + str(elapsed_time) + " seconds")
        print("Problem solved with default heuristic in " + str(default_solution_len) + " steps")
        print("Problem solved with default heuristic with " + str(default_node_removed) + " nodes removed")

        start_time = time.time()
        manhattan_search, manhattan_node_removed = astar_manhattan_search(game)
        elapsed_time = time.time() - start_time
        manhattan_solution_len = len(manhattan_search.solution())
        print("\n========================== Manhattan Heuristic ==========================")
        print("Problem solved with Manhattan heuristic in " + str(elapsed_time) + " seconds")
        print("Problem solved with Manhattan heuristic in " + str(manhattan_solution_len) + " steps")
        print("Problem solved with Manhattan heuristic with " + str(manhattan_node_removed) + " nodes removed\n\n")

if __name__ == '__main__':
    # unittest.main()
    Question2()
    Question3()
