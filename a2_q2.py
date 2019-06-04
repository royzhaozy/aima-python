"""
Assignment 2 Question 2 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

def check_teams(graph, csp_sol):
    if graph.__len__() != csp_sol.__len__():
        return False
    for i in range (0, csp_sol.__len__()):
        for j in range (i + 1, csp_sol.__len__()):
            if csp_sol[i] == csp_sol[j] and (j in graph[i]):
                return False
    return True

if __name__ == '__main__':
    g = {0: [1, 2], 1: [0], 2: [0], 3: []}
    X = {0: 0, 1: 1, 2: 2, 3: 0}
    print(check_teams(g, X))