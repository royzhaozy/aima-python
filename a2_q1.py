"""
Assignment 2 Question 1 for CMPT 310
Summer 2019, Simon Fraser University
Ziyi Zhao, 301244109
"""

import random

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

if __name__ == '__main__':
    print(rand_graph(10, 0.2))