from math import sqrt
from re import split

def sameRoll(index1, index2, N):
    return int((index1 - 1) / N) == int((index2 - 1) / N)
    # If two index are on the same row, then a-1/N should have the same integer
    # part  as b-1/N. Minus 1 because starting from 1.

def sameColon(index1, index2, N):
    return ((index1 - index2) % N) == 0
    # If two index are on the same colon then the difference between the two
    # index should me a integer multiple of N

def Diagonals(N):
    diag = []

    # Diagonals from left to right
    for i in range(1, N * ( N - 1)):
        if (i % N) != 0:
            for j in range (i + N + 1, N**2 + 1, N + 1):
                diag.append(str(-i) + " " + str(-j) + " 0")
                # diag.append([-i, -j, 0])
                if (j % N) == 0:
                    break

    # Diagonals from right to left
    for i in range(1, N * ( N - 1) + 1):
        if (i % N) != 1:
            for j in range (i + N - 1, N**2 + 1, N - 1):
                diag.append(str(-i) + " " + str(-j) + " 0")
                # diag.append([-i, -j, 0])
                if (j % N) == 1:
                    break

    return diag

def Rows(N):
    row = []

    for i in range (1, N ** 2 + 1):
        if (i % N) == 1:
            row.append(str(i))
            # row.append([i])
            for j in range (i + 1, i + N):
                row[-1] += (" " + str(j))
                # row[-1].append(j)
            row[-1] += " 0"
            # row[-1].append(0)

        if (i % N) != 0:
            j = i + 1
            while (j % N) != 1:
                row.append(str(-i) + " " + str(-j) + " 0")
                # row.append([-i, -j, 0])
                j += 1

    return row

def Columns(N):
    column = []

    i = 1

    while (True):
        if i <= N:
            column.append(str(i))
            # column.append([i])
            for j in range (i + N, N ** 2 + 1, N):
                column[-1] += (" " + str(j))
                # column[-1].append(j)
            column[-1] += " 0"
            # column[-1].append(0)

        for j in range (i + N, N ** 2 + 1, N):
            column.append(str(-i) + " " + str(-j) + " 0")
            # column.append([-i, -j, 0])

        if i == (N * (N - 1)):
            break

        elif i > (N * (N - 2)):
            i = (i + (2 * N) + 1) % (N ** 2)

        else:
            i += N

    return column

def make_queen_sat(N):
    if N < 2:
        raise ValueError("Only support N-Queen problem with size greater than 1")
    prob = Rows(N) + Columns(N) + Diagonals(N)
    size = len(prob)
    prob.insert(0, "c " + str(N) + "-queens problem")
    prob.insert(1, "p cnf " + str(N ** 2) + " " + str(size))
    prob = "\n".join(prob)
    return prob

def draw_queen_sat_sol(sol):
    solList = split(' |\n', sol)

    if solList[0] == 'UNSAT':
        print("no solution")
        return

    content = list(map(int, solList[1: -2]))

    if len(content) > 1600:
        raise ValueError("Only support N-Queen problem with size less than 40")
    N = int(sqrt(len(content)))
    for i in range (0, N):
        for j in range (0, N):
            if content[i * N + j] > 0:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print('')

if __name__ == '__main__':
    N = 40
    f = open("../Assignment 3/" + str(N) + "_Queen_test.txt", "+w")
    f.write(make_queen_sat(N))
    f.close()
