
import random
import timeit
from functions import pares_rainhas_atacadas, display_board


def main():
    start = timeit.default_timer()
    fila_de_prioridade = [{'unplaced_queens':8, 'pares':28, 'seqs': [0] * 8}]
    solucoes = []
    flag = 0
    nodes = 0

    while fila_de_prioridade:
        estados = fila_de_prioridade.pop(0)
        nodes = nodes + 1
        if estados['pares'] == 0 and estados['unplaced_queens'] == 0:
            solucoes = estados['seqs']
            flag = 1
            break
        nums = list(range(1, 9))
        seqs = estados['seqs']
        if seqs.count(0) == 0:
            continue
        for j in range(8):
            pos = seqs.index(0)
            temp_seqs = list(seqs)
            temp = random.choice(nums)
            temp_seqs[pos] = temp
            nums.remove(temp)
            fila_de_prioridade.append({'unplaced_queens':temp_seqs.count(0), 'pares':pares_rainhas_atacadas(temp_seqs), 'seqs':temp_seqs})
        fila_de_prioridade = sorted(fila_de_prioridade, key=lambda x:(x['pares'] + x['unplaced_queens']))

    if solucoes:

        print('Estados acessados: ' + str(nodes))
        print('Sequencia de Soluções:' + str(solucoes))
        display_board(solucoes)
    else:
        print('Solução não encontrada')

    end = timeit.default_timer()
    print('Tempo: ' + str('%.8f' % (end-start)) + ' s')


if __name__ == '__main__':
    main()