from math import sqrt

def draw_queen_sat_sol(sol):
    if len(sol) > 1600:
        raise ValueError("Only support N-Queen problem with size less than 40")
    N = int(sqrt(len(sol)))
    for i in range (0, N):
        for j in range (0, N):
            if sol[i * N + j] > 0:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print('')

if __name__ == '__main__':
    sol = [-1, -2, 3, -4, 5, -6, -7, -8, -9, -10, -11, 12, -13, 14, -15, -16]
    draw_queen_sat_sol(sol)