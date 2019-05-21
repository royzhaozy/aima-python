"""
Assignment 1 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import random
import unittest
from search import Problem, EightPuzzle

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
            game1 = make_rand_8puzzle()
            display(game1.initial)
            self.assertTrue(game1.check_solvability(game1.initial))
            print("test " + str(i+1) + " passed\n")

if __name__ == '__main__':
    unittest.main()

