
import random
import time
from functions import attacked_queens_pairs, display_board

start = time.time()
frontier_priority_queue = [{'unplaced_queens':8, 'pairs':28, 'seqs':[0] * 8}] # The initial state is 8 zeros, which means that there are no queens on the chessboard; g(n) = the number of queens that have not been placed well, h(n) = the logarithm of queens attacking each other, and h(n)=28, g(n)=8
solution = []
flag = 0 # The representative has not found a solution

while frontier_priority_queue: # If the frontier is not empty, the loop will continue. If the solution is found successfully, the loop will output the solution. If the frontier is empty, the loop will fail
    first = frontier_priority_queue.pop(0)  # Since frontier s are sorted every time, the first sequence is extended
    if first['pairs'] == 0 and first['unplaced_queens'] == 0: # Do the goal test before extending the node: if the sequence h(n)=g(n)=0, then the sequence is the solution sequence
        solution = first['seqs']
        flag = 1  # success
        break
    nums = list(range(1, 9))  # List with elements 1-8
    seqs = first['seqs']
    if seqs.count(0) == 0: # Due to the sorting mechanism in the following code, the node that [8 queens have been placed, i.e. g(n)=0, but the number of queens attacking each other is close to 0, but not 0, i.e. h(n)!=0] may be placed in the first place; and this kind of node certainly does not meet the requirements, but such a node cannot be expanded, because the 8 queens have been placed
        continue # You can only skip this kind of node
    for j in range(8): # In the first position of 0 in the sequence, that is, the leftmost column without queen, select a row to place queen
        pos = seqs.index(0)
        temp_seqs = list(seqs)
        temp = random.choice(nums)  # Select a random row in the column to place the queen
        temp_seqs[pos] = temp # Place the queen on line temp of the column
        nums.remove(temp)  # Remove generated values from nums
        frontier_priority_queue.append({'unplaced_queens':temp_seqs.count(0), 'pairs':attacked_queens_pairs(temp_seqs),'seqs':temp_seqs})
    frontier_priority_queue = sorted(frontier_priority_queue, key=lambda x:(x['pairs']+x['unplaced_queens']))

if solution:
    print('Solution sequence found:' + str(solution))
    display_board(solution)
else:
    print('Algorithm failed, no solution found')

end = time.time()
print('Time' + str('%.2f' % (end-start)) + 's')