"""
Assignment 2 Question 3 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

from a2_q3 import *
from csp import min_conflicts

if __name__ == '__main__':
    # graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3)]
    graphs = [rand_graph(100, 0.1), rand_graph(100, 0.2), rand_graph(100, 0.3),
              rand_graph(100, 0.4), rand_graph(100, 0.5), rand_graph(100, 0.6),
              rand_graph(100, 0.7), rand_graph(100, 0.8), rand_graph(100, 0.9)]
    for g in graphs:
        p = rand_graph_teaming(g)
        start_time = time.time()
        res = min_conflicts(p)
        elapsed_time = time.time() - start_time
        if check_teams(g, res):
            print ("================== Min Conflicts ==========================")
            print ("Edges count for random graph:\t" + str(edge_count(g)))
            print ("Number of teams in result:\t" + str(team_count(res)))
            print ("Seconds took solving the problem:\t" + str(elapsed_time))
            print ("Number of assigned  variables: \t" + str(p.nassigns))
            print ("Number of un-assigned  variables: \t" + str(max(len(p.variables) - p.nassigns, 0)) + "\n")
        else:
            print ("Result not valid")
