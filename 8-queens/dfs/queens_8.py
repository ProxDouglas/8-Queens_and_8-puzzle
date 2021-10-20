from queue import Queue
import timeit


class Queens_8:

    def __init__(self):
        self.size = 8

    def dfs_solucoes(self):
        solucoes = []
        stack = [[]]
        estados = 0
        problem = [{'solucao': [], 'estados': 0, 'tempo': 0}]
        while stack:
            start = timeit.default_timer()
            estados = estados + 1

            solucao = stack.pop()
            if self.conflict(solucao):
                continue
            row = len(solucao)
            if row == self.size:
                end = timeit.default_timer()
                problem.append({'solucao': solucao, 'estados': estados, 'tempo':(end-start)})
                solucoes.append(problem)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solucao.copy()
                queens.append(queen)
                stack.append(queens)
        return solucoes

    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print(self, queens, nodes, tempo):
        print(' ---' * self.size)
        for i in range(self.size):
            for j in range(self.size):
                p = '1' if (i, j) in queens else '0'
                print(' %s ' % p, end='')
            print(' ')
        print(' ---' * self.size)
        print('Estados: ' + str(nodes))
        print('Tempo: ' + str('%.8f' % tempo)+'s')