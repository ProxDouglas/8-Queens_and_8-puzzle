from queens_8 import Queens_8


def main():
    print(': N-Queens Problem :')
    size = 8 #mudar para 8
    n_queens = Queens_8(size)
    bfs_solutions = n_queens.solve_bfs()
    for i, j in enumerate(bfs_solutions):
        print('BFS Solution %d:' % (i + 1))
        solucao = bfs_solutions[i].pop(1)
        n_queens.print(solucao['solution'], solucao['nodes'], solucao['tempo'])
    print('Total BFS solutions: %d' % len(bfs_solutions))


if __name__ == '__main__':
    main()