"""
Assignment 1 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import time
import random
import numpy
import unittest
from search import Node, EightPuzzle, astar_search, astar_manhattan_search

# Manhattan_8pz = numpy.array([[4,3,2,3,2,1,2,1,0],
#                              [0,1,2,1,2,3,2,3,4],
#                              [1,0,1,2,1,2,3,2,3],
#                              [2,1,0,3,2,1,4,3,2],
#                              [1,2,3,0,1,2,1,2,3],
#                              [2,1,2,1,0,1,2,1,2],
#                              [3,2,1,2,1,0,3,2,1],
#                              [2,3,4,1,2,3,0,1,2],
#                              [3,2,3,2,1,2,1,0,1]])
#
# def h_Manhattan(problem, node):
#     """A* search is best-first graph search with f(n) = g(n)+h(n).
#     You need to specify the h function when you call astar_search, or
#     else in your Problem subclass."""
#     return sum(Manhattan_8pz[problem.initial[i]][i] for i in node.state)

def make_rand_8puzzle():
    """ Returns a new instance of an EightPuzzle problem with a random initial
    state that is solvable """
    tiles = list(range(0,9))
    random.shuffle(tiles)
    puzzle = EightPuzzle(tuple(tiles))
    if(not puzzle.check_solvability(tiles)):
        puzzle = make_rand_8puzzle()
    return puzzle



def display(state):
    """ Prints a neat and readable representation of state """
    for i in range(0, 3):
        for j in range(0, 3):
            if (state[(3 * i) + j] == 0):
                print("* ", end=" ")
            else:
                print(str(state[(3 * i) + j]) + " ", end=" ")
        print("")

class Question1(unittest.TestCase):
    def test_check_solvability(self):
        """ Checks if the generated puzzle is always solvable """
        for i in range (0,10):
            game = make_rand_8puzzle()
            self.assertTrue(game.check_solvability(game.initial))
            print("test " + str(i+1) + " passed")


def Question2():
    for i in range (0,10):
        game = EightPuzzle(tuple([2,0,5,1,6,7,4,8,3]))#make_rand_8puzzle()
        display(game.initial)
        if (not game.check_solvability(game.initial)):
            print("Puzzle Unsolvable")
            exit()
        start = time.time()
        default_search, default_node_removed = astar_search(game)
        default_solution = default_search.solution()
        default_time = time.time() - start
        print("Problem solved with default heuristic in " + str(default_time) + " seconds")
        print("Problem solved with default heuristic in " + str(len(default_solution)) + " steps")
        print("Problem solved with default heuristic with " + str(len(default_node_removed)) + " nodes removed")
        
        start = time.time()
        manhattan_search, manhattan_node_removed = astar_manhattan_search(game)
        manhattan_solution = manhattan_search.solution()
        manhattan_time = time.time() - start
        print("Problem solved with Manhattan heuristic in " + str(manhattan_time) + " seconds\n")
        print("Problem solved with Manhattan heuristic in " + str(len(manhattan_solution)) + " steps")
        print("Problem solved with Manhattan heuristic with " + str(len(manhattan_node_removed)) + " nodes removed")

if __name__ == '__main__':
    #unittest.main()
    Question2()

