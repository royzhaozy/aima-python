"""
Assignment 2 Question 3 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import time

from a2_q1 import *
from a2_q2 import *
from csp import CSP, different_values_constraint, backtracking_search, mrv, forward_checking

# ______________________________________________________________________________
# Erdos-Renyi random graph problem

def edge_count(graph):
    edge = 0
    for i in list(graph.keys()):
        edge += sum(j > i for j in graph[i])
    return edge

def rand_graph_teaming(graph):
    return CSP(list(graph.keys()),
                   {i: list(graph.keys()) for i in range(0, graph.__len__())},
                   graph,
                   different_values_constraint)

def team_count(csp_sol):
    return len(set(csp_sol.values()))

def run_q3():
    graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
              rand_graph(30, 0.4), rand_graph(30, 0.5)]
    # graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
    #           rand_graph(30, 0.4), rand_graph(30, 0.5), rand_graph(30, 0.6),
    #           rand_graph(30, 0.7), rand_graph(30, 0.8), rand_graph(30, 0.9)]
    for g in graphs:
        p = rand_graph_teaming(g)
        start_time = time.time()
        res = backtracking_search(p)
        elapsed_time = time.time() - start_time
        if check_teams(g, res):
            print ("================== Back Tracking ==========================")
            print ("Edges count for random graph:\t\t" + str(edge_count(g)))
            print ("Number of teams in result:\t\t\t" + str(team_count(res)))
            print ("Seconds took solving the problem:\t" + str(elapsed_time))
            print ("Number of assigned  variables: \t\t" + str(p.nassigns))
            print ("Number of un-assigned  variables: \t" + str(max(len(p.variables) - p.nassigns, 0)) + "\n")
        else:
            print ("Result not valid")
        p.nassigns = 0
        start_time = time.time()
        res = backtracking_search(p, select_unassigned_variable=mrv, inference=forward_checking)
        elapsed_time = time.time() - start_time
        if check_teams(g, res):
            print ("========== Back Tracking + forward checking ===============")
            print ("Number of teams in result:\t\t\t" + str(team_count(res)))
            print ("Seconds took solving the problem:\t" + str(elapsed_time))
            print ("Number of assigned  variables: \t\t" + str(p.nassigns))
            print ("Number of un-assigned  variables: \t" + str(max(len(p.variables) - p.nassigns, 0)) + "\n\n\n")
        else:
            print("Result not valid")

if __name__ == '__main__':
    run_q3()
