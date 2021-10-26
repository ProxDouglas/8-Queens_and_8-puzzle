
import timeit
from collections import deque
from state import State
from tabuleiro import Tabuleiro
from view import View
from heapq import heappush, heappop, heapify
import itertools

estado_objetivo = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def bfs(start_state, tabuleiro):
    node_objetivo = State
    profundidade_alcancada = 0
    max_frontier_size = 0
    estados_expandidos = 0

    explored, queue = set(), deque([State(start_state, None, None, 0, 0, 0)])

    while queue:

        node = queue.popleft()

        explored.add(node.map)

        if node.state == estado_objetivo:
            node_objetivo = node

            analise_data = {'node_objetivo': node_objetivo, 'profundidade_alcancada': profundidade_alcancada,
                            'max_frontier_size': max_frontier_size, 'estados_expandidos': estados_expandidos}

            return queue, analise_data

        neighbors = expand(node, tabuleiro)
        estados_expandidos += 1

        for neighbor in neighbors:
            if neighbor.map not in explored:
                queue.append(neighbor)
                explored.add(neighbor.map)

                if neighbor.depth > profundidade_alcancada:
                    profundidade_alcancada += 1

        if len(queue) > max_frontier_size:
            max_frontier_size = len(queue)


def dfs(start_state, tabuleiro):
    node_objetivo = State
    profundidade_alcancada = 0
    max_frontier_size = 0
    estados_expandidos = 0

    explored, stack = set(), list([State(start_state, None, None, 0, 0, 0)])

    while stack:

        node = stack.pop()

        explored.add(node.map)

        if node.state == estado_objetivo:
            node_objetivo = node

            analise_data = {'node_objetivo': node_objetivo, 'profundidade_alcancada': profundidade_alcancada,
                            'max_frontier_size': max_frontier_size, 'estados_expandidos': estados_expandidos}

            return stack, analise_data

        neighbors = reversed(expand(node, tabuleiro))
        estados_expandidos += 1

        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)

                if neighbor.depth > profundidade_alcancada:
                    profundidade_alcancada += 1

        if len(stack) > max_frontier_size:
            max_frontier_size = len(stack)

def ast(start_state, tabuleiro):
    node_objetivo = State
    profundidade_alcancada = 0
    max_frontier_size = 0
    estados_expandidos = 0

    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

    key = verificador(start_state, tabuleiro, estado_objetivo)

    root = State(start_state, None, None, 0, 0, key)

    entry = (key, 0, root)

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == estado_objetivo:
            node_objetivo = node[2]

            analise_data = {'node_objetivo': node_objetivo, 'profundidade_alcancada': profundidade_alcancada,
                            'max_frontier_size': max_frontier_size, 'estados_expandidos': estados_expandidos}

            return heap, analise_data

        neighbors = expand(node[2], tabuleiro)
        estados_expandidos += 1

        for neighbor in neighbors:

            neighbor.key = neighbor.cost + verificador(neighbor.state, tabuleiro, estado_objetivo)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

                if neighbor.depth > profundidade_alcancada:
                    profundidade_alcancada += 1

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)

        if len(heap) > max_frontier_size:
            max_frontier_size = len(heap)


def expand(node, tabuleiro):

    neighbors = list()

    neighbors.append(State(move(node.state, 1, tabuleiro), node, 1, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 2, tabuleiro), node, 2, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 3, tabuleiro), node, 3, node.depth + 1, node.cost + 1, 0))
    neighbors.append(State(move(node.state, 4, tabuleiro), node, 4, node.depth + 1, node.cost + 1, 0))

    nodes = [neighbor for neighbor in neighbors if neighbor.state]

    return nodes


def move(state, position, tabuleiro):
    new_state = state[:]

    index = new_state.index(0)

    if position == 1:  # Up

        if index not in range(0, tabuleiro.getTabuleiro_perimetro()):

            temp = new_state[index - tabuleiro.getTabuleiro_perimetro()]
            new_state[index - tabuleiro.getTabuleiro_perimetro()] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 2:  # Down

        if index not in range(tabuleiro.getTabuleiro_len() - tabuleiro.getTabuleiro_perimetro(),
                              tabuleiro.getTabuleiro_len()):

            temp = new_state[index + tabuleiro.getTabuleiro_perimetro()]
            new_state[index + tabuleiro.getTabuleiro_perimetro()] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 3:  # Left

        if index not in range(0, tabuleiro.getTabuleiro_len(), tabuleiro.getTabuleiro_perimetro()):

            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 4:  # Right

        if index not in range(tabuleiro.getTabuleiro_perimetro() - 1, tabuleiro.getTabuleiro_len(),
                              tabuleiro.getTabuleiro_perimetro()):

            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None


def verificador(state, tabuleiro, estado_objetivo):
    return sum(abs(b % tabuleiro.getTabuleiro_perimetro() - g % tabuleiro.getTabuleiro_perimetro()) + abs(
        b // tabuleiro.getTabuleiro_perimetro() - g // tabuleiro.getTabuleiro_perimetro())
               for b, g in ((state.index(i), estado_objetivo.index(i)) for i in range(1, tabuleiro.getTabuleiro_len())))


def backtrace(node_objetivo, initial_state):
    moves = list()
    current_node = node_objetivo

    while initial_state != current_node.state:

        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'

        moves.insert(0, movement)
        current_node = current_node.parent

    return moves


def criar_primeiro_estado(configuration):
    initial_state = list()
    data = configuration.split(",")
    for element in data:
        initial_state.append(int(element))

    return initial_state

def cria_tabuleiro(initial_state):
    return Tabuleiro(len(initial_state), int(len(initial_state) ** 0.5))


def main():
    view = View()
    initial_state = list()

    dados_entrada = view.definir_estado_inicial()

    initial_state = criar_primeiro_estado(dados_entrada.tabuleiro)
    tabuleiro = cria_tabuleiro(initial_state)
    function = function_map[dados_entrada.algorithm]

    # tabuleiro = iniciando_Tabuleiro(dados_entrada['tabuleiro'])
    # function = function_map[dados_entrada['algorithm']]

    start = timeit.default_timer()

    frontier, data = function(initial_state, tabuleiro)

    stop = timeit.default_timer()

    view.export(frontier, stop - start, data, backtrace(data['node_objetivo'], initial_state))


function_map = {
    'bfs': bfs,
    'dfs': dfs,
    'ast': ast,
}

if __name__ == '__main__':
    main()
