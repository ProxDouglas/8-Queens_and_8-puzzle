import datetime
from queue import Queue


class Queens_8:

    def __init__(self, size):
        self.size = size

    def solve_bfs(self):
        nodes = 0
        if self.size < 1:
            return []
        solutions = []
        problem =[{'nodes': 0, 'solution': [], 'tempo': 0 }]
        queue = Queue()
        queue.put([])
        while not queue.empty():
            start = datetime.datetime.now()
            solution = queue.get()
            nodes = nodes + 1
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                end = datetime.datetime.now()
                problem.append({'nodes':nodes, 'solution':solution, 'tempo':(end-start)})
                solutions.append(problem)
                nodes = 0
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                queue.put(queens)
        return solutions

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
        print('nodes: ' + str(nodes))
        print('tempo: ' + str(tempo)+'ms')

