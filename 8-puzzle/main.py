import timeit

from view import View
from algoritimo import Algoritimo

def main():
    view = View()
    algoritimo = Algoritimo()
    initial_state = list()

    dados_entrada = view.definir_estado_inicial()

    initial_state = algoritimo.criar_primeiro_estado(dados_entrada.tabuleiro)
    tabuleiro = algoritimo.cria_tabuleiro(initial_state)
    function = algoritimo.function_map[dados_entrada.algorithm]

    # tabuleiro = iniciando_Tabuleiro(dados_entrada['tabuleiro'])
    # function = function_map[dados_entrada['algorithm']]

    start = timeit.default_timer()

    frontier, data = function(algoritimo, initial_state, tabuleiro) #pq preciso de objeto algoritimo?

    stop = timeit.default_timer()

    view.export(frontier, stop - start, data, algoritimo.backtrace(data['node_objetivo'], initial_state))



if __name__ == '__main__':
    main()