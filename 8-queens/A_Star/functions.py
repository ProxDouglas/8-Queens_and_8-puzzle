import numpy as np

def attacked_queens_pairs(seqs):
    """
    Calculate the queen logarithm of the attack on the chessboard corresponding to the sequence n]
    We only need to check whether there are other queens on the eight queens of the current chessboard in their respective rows and two diagonals, without judging whether there are other queens in the same column
    """
    a = np.array([0] * 81)  # Create a one-dimensional array with 81 zeros
    a = a.reshape(9, 9)  # Change to 9 * 9 two-dimensional array. For the convenience of later use, only the 8 * 8 parts of the last eight rows and columns are used as a blank chessboard
    n = 0  # The number of queens attacking each other is initialized to 0

    for i in range(1, 9):
        if seqs[i-1] != 0: # An element of seqs is 0, which means that no queen should be placed in the corresponding chessboard column
            a[seqs[i - 1]][i] = 1  # Generate the corresponding chessboard sequence, and place it in the order of the first chessboard column

    for i in range(1, 9):
        if seqs[i - 1] == 0:
            continue # If an element of seqs is 0, it represents the corresponding chessboard. If no queen is placed in this column, the next column will be judged directly
        for k in list(range(1, i)) + list(range(i + 1, 9)):  # Check whether there are other queens on each queen's line
            if a[seqs[i - 1]][k] == 1:  # There are other queens
                n += 1
        t1 = t2 = seqs[i - 1]
        for j in range(i - 1, 0, -1):  # Look at the two diagonals in the left half
            if t1 != 1:
                t1 -= 1
                if a[t1][j] == 1:
                    n += 1  # There are other queens on the left half of the diagonal

            if t2 != 8:
                t2 += 1
                if a[t2][j] == 1:
                    n += 1  # There are other queens on the left half of the sub diagonal

        t1 = t2 = seqs[i - 1]
        for j in range(i + 1, 9):  # Look at the two diagonals in the right half
            if t1 != 1:
                t1 -= 1
                if a[t1][j] == 1:
                    n += 1  # There are other queens on the right half of the diagonal

            if t2 != 8:
                t2 += 1
                if a[t2][j] == 1:
                    n += 1  # There are other queens on the right half of the sub diagonal
    return int(n/2)  # Returns n/2, because A attacking B also means B attacking A, so returns half of n

def display_board(seqs):
    """
     Displays the chessboard corresponding to the sequence
    """
    board = np.array([0] * 81)  # Create a one-dimensional array with 81 zeros
    board = board.reshape(9, 9)  # Change to a 9 * 9 two-dimensional array. For the convenience of later use, only the 8 * 8 parts of the last eight rows and columns are used as a blank chessboard

    for i in range(1, 9):
        board[seqs[i - 1]][i] = 1  # According to the sequence, from the first column to the last column, put a queen in the corresponding position to generate the chessboard corresponding to the current sequence
    print('The corresponding chessboard is as follows:')
    for i in board[1:]:
        for j in i[1:]:
            print(j, ' ', end="")  # With end, print doesn't wrap
        print()  # After outputting one line, wrap it. This cannot be print('\n'), otherwise it will be replaced by two lines
    print('The number of queens to attack is' + str(attacked_queens_pairs(seqs)))