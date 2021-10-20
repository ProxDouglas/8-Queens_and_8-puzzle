from queens_8 import Queens_8


def main():
    print('.: N-Queens Problem :.')
    size = 8
    n_queens = Queens_8()
    dfs_solutions = n_queens.dfs_solucoes()
    for i, j in enumerate(dfs_solutions):
        print('DFS Solution %d:' % (i + 1))
        solucao = dfs_solutions[i].pop(1)
        n_queens.print(solucao['solucao'], solucao['estados'], solucao['tempo'])
    print('Total DFS solutions: %d' % len(dfs_solutions))


if __name__ == '__main__':
    main()