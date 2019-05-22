"""
Assignment 1 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import time
import random
import unittest
from search import EightPuzzle, astar_search

def make_rand_8puzzle():
    """ Returns a new instance of an EightPuzzle problem with a random initial
    state that is solvable """
    tiles = list(range(0,9))
    random.shuffle(tiles)
    puzzle = EightPuzzle(tiles)
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
    for i in range (0,1):
        game = make_rand_8puzzle()
        display(game.initial)
        if (not game.check_solvability(game.initial)):
            print("Puzzle Unsolvable")
            exit()
        start = time.process_time()
        astar_search(game)
        finish = time.process_time()
        print("Problem solved with A* in " + str(finish - start) + " seconds\n")

if __name__ == '__main__':
    #unittest.main()
    Question2()

