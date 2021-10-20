import numpy as np

def pares_rainhas_atacadas(seqs):

    a = np.array([0] * 81)
    a = a.reshape(9, 9)
    n = 0

    for i in range(1, 9):
        if seqs[i-1] != 0:
            a[seqs[i - 1]][i] = 1

    for i in range(1, 9):
        if seqs[i - 1] == 0:
            continue
        for k in list(range(1, i)) + list(range(i + 1, 9)):
            if a[seqs[i - 1]][k] == 1:
                n += 1
        t1 = t2 = seqs[i - 1]
        for j in range(i - 1, 0, -1):
            if t1 != 1:
                t1 -= 1
                if a[t1][j] == 1:
                    n += 1

            if t2 != 8:
                t2 += 1
                if a[t2][j] == 1:
                    n += 1

        t1 = t2 = seqs[i - 1]
        for j in range(i + 1, 9):
            if t1 != 1:
                t1 -= 1
                if a[t1][j] == 1:
                    n += 1

            if t2 != 8:
                t2 += 1
                if a[t2][j] == 1:
                    n += 1
    return int(n/2)

def display_board(seqs):

    board = np.array([0] * 81)
    board = board.reshape(9, 9)

    for i in range(1, 9):
        board[seqs[i - 1]][i] = 1
    print('Tabuleiro correspondente:')
    for i in board[1:]:
        for j in i[1:]:
            print(j, ' ', end="")
        print()
    print('Número de rainhas atacando ' + str(pares_rainhas_atacadas(seqs)))