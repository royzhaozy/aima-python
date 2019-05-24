"""
Assignment 1 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import time
import random
import numpy
import unittest
from utils import memoize, PriorityQueue
from search import Problem, Node


Manhattan_8pz = numpy.array([[4,3,2,3,2,1,2,1,0],
                             [0,1,2,1,2,3,2,3,4],
                             [1,0,1,2,1,2,3,2,3],
                             [2,1,0,3,2,1,4,3,2],
                             [1,2,3,0,1,2,1,2,3],
                             [2,1,2,1,0,1,2,1,2],
                             [3,2,1,2,1,0,3,2,1],
                             [2,3,4,1,2,3,0,1,2],
                             [3,2,3,2,1,2,1,0,1]])

Manhattan_Ypz = numpy.array([[4,4,3,2,3,2,1,2,0],
                             [0,4,1,2,3,2,3,4,4],
                             [4,0,3,2,1,4,3,2,4],
                             [1,3,0,1,2,1,2,3,3],
                             [2,2,1,0,1,2,1,2,2],
                             [3,1,2,1,0,3,2,1,3],
                             [2,4,1,2,3,0,1,2,2],
                             [3,3,2,1,2,1,0,1,1],
                             [4,2,3,2,1,2,1,0,2]])

def best_first_graph_search(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    poped_node = 0
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        poped_node += 1
        if problem.goal_test(node.state):
            return node, poped_node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None

def astar_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


def astar_manhattan_search(problem, h=None):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(problem.h_manhattan, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n))


class EightPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board,
    where one of the squares is a blank. A state is represented as a tuple of length 9,
    where element at index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))

    def h_manhattan(self, node):
        """ Return the heuristic value for a given state. This heuristic function used is
        h(n) = sum of Manhattan distance """

        # First index finds the right colon, second index finds the distance from goal
        return sum(Manhattan_8pz[node.state[i]][i] for i in node.state)

    def display(self, state):
        """ Prints a neat and readable representation of state """
        for i in range(0, 3):
            for j in range(0, 3):
                if (state[(3 * i) + j] == 0):
                    print("* ", end=" ")
                else:
                    print(str(state[(3 * i) + j]) + " ", end=" ")
            print("")


class YPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a Y shaped board,
    where one of the squares is a blank. A state is represented as a tuple of length 9,
    where element at index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square in [0, 1, 2, 5, 8]:
            possible_actions.remove('LEFT')
        if index_blank_square in [0, 1, 3]:
            possible_actions.remove('UP')
        if index_blank_square in [0, 1, 4, 7, 8]:
            possible_actions.remove('RIGHT')
        if index_blank_square in [5, 7, 8]:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        if blank in [0, 6]:
            delta = {'UP': -3, 'DOWN': 2, 'LEFT': -1, 'RIGHT': 1}
        elif blank in [2, 8]:
            delta = {'UP': -2, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        else:
            delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        # The corners has to be 1,2,7 or * (0)
        if state[0] not in [0, 1] or \
                state[1] not in [0, 2] or \
                state[8] not in [0, 7]:
            return False

        # If the corner is empty, the one below/above it has to be the corresponding tile
        if (state[0] == 0 and state[2] != 1) or \
                (state[1] == 0 and state[4] != 2) or \
                (state[8] == 0 and state[6] != 7):
            return False

        inversion = 0
        for i in range(2, len(state) - 1):
            for j in range(i + 1, len(state) - 1):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))

    def h_manhattan(self, node):
        """ Return the heuristic value for a given state. This heuristic function used is
        h(n) = sum of Manhattan distance """

        # First index finds the right colon, second index finds the distance from goal
        return sum(Manhattan_Ypz[node.state[i]][i] for i in node.state)

    def display(self, state):
        """ Prints a neat and readable representation of state """
        for i in range(len(state)):
            if i == 2 or i == 5 or i == 8:
                print("")
            if i == 1 or i == 8:
                print("  ", end=" ")
            if state[i] == 0:
                print("* ", end=" ")
            else:
                print(str(state[i]) + " ", end=" ")
        print("")

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
    # Question2()
    Question3()
