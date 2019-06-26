from a2_q1 import *
from time import time
from numpy import arange
from os import system, remove

def make_ice_breaker_sat(graph, k):
    size = len(graph)
    prob = []
    for i in range(1, size + 1):
        prob.append(str(i))
        for j in range (i + size, size * k + 1, size):
            prob[-1] += (" " + str(j))
        prob[-1] += " 0"

    for i in range(size):
        edge = len(graph[i])
        if edge != 0:
            for j in range(edge):
                if i < graph[i][j]:
                    for x in range (k):
                        prob.append(str(-(i + 1 + x * size)) + " " +
                                    str(-(graph[i][j] + 1 + x * size)) + " 0")

    variables = size * k
    clause = len(prob)
    prob.insert(0, "c teaming problem")
    prob.insert(1, "p cnf " + str(variables) + " " + str(clause))
    prob = "\n".join(prob)
    return prob

def find_min_teams(graph):
    size = len(graph)
    process_time = 0
    for k in range (1, size + 1):
        f = open("find_min_teams.txt", "+w")
        f.write(make_ice_breaker_sat(graph, k))
        f.close()
        start_time = time()
        system("minisat find_min_teams.txt found_min_teams.txt > /dev/null 2>&1")
        process_time += time() - start_time
        f = open("found_min_teams.txt", "r")
        result = f.read()
        f.close()
        remove("find_min_teams.txt")
        remove("found_min_teams.txt")
        if "UNSAT" not in result:
            return k, process_time

if __name__ == '__main__':
    size = 10
    for i in arange (0.1, 1, 0.1):
        print("\n" + "Probability is now " + str(i))
        for j in range (10):
            graph  = rand_graph(size, i)
            print(str(j) + " " + str(find_min_teams(graph)))

