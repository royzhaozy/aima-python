"""
Assignment 2 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""
import random
from csp import CSP

def rand_graph(n, p):
    if not (n > 1 and p > 0 and p < 1):
        raise ValueError("random graph import not valid: must have more then 1 node and probability between 0~1")
    x = {i: [] for i in range(n)}
    for i in range (0, n - 1):
        for j in range (i + 1, n):
            if random.uniform(0, 1) <= p:
                x[i].append(j)
                x[j].append(i)
    return x

def check_teams(graph, csp_sol):
    if graph.__len__() != csp_sol.__len__():
        return False
    for i in range (0, csp_sol.__len__()):
        for j in range (i + 1, csp_sol.__len__()):
            if csp_sol[i] == csp_sol[j] and (j in graph[i]):
                return False
    return True

if __name__ == '__main__':
    print(rand_graph(10, 0.2))
    g = {0: [1, 2], 1: [0], 2: [0], 3: []}
    X = {0: 0, 1: 1, 2: 2, 3: 0}
    print(check_teams(g, X))