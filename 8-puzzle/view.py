import argparse



class View:




    def definir_estado_inicial(self,):
        # parse = ()
        #
        # print("Defina a ordem do puzzle: ")
        # print("Ex: 0,1,2,3,4,5,6,7,8")
        #
        # ordem = input('Entre com a sua ordem: ')
        #
        # print("Escolha o algoritmo a ser executado no problema: ")
        # print(" 1-dfs \n 2-bfs \n 3-A*")
        #
        # escolha = input('Entre com sua escolha: ')
        #
        # if(escolha == str(1)):
        #     parse = [{'algorithm':'dfs', 'tabuleiro':ordem}]
        # elif (escolha == str(2)):
        #     parse = [{'algorithm':'bfs', 'tabuleiro':ordem}]
        # elif (escolha == str(3)):
        #     parse = [{'algorithm':'ast', 'tabuleiro':ordem}]

        parser = argparse.ArgumentParser()

        parser.add_argument('algorithm')
        parser.add_argument('tabuleiro')
        return parser.parse_args()

        # return parse.pop(0)


    def export(self, frontier, time, data, moves):


        print("Resultado: ")
        print("Caminho Objetivo: " + str(moves))
        print("Custo de passagem: " + str(len(moves)))
        print("Estados expandidos: " + str(data['estados_expandidos']))
        print("fringe_size: " + str(len(frontier)))
        print("Profundidade de procura: " + str(data['node_objetivo'].depth))
        print("Profundidade maxima de procura: " + str(data['profundidade_alcancada']))
        print("Tempo de processamento: " + format(time, '.8f'))
        # print("Uso de RAM: " + format(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000.0, '.8f'))