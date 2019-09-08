#import classeEstado as node
import heapq
import copy

class State (object):
    def __init__(self, pai, profundidade, custo, f, linha_espaco, coluna_espaco, acao, tab):
        #self.tab = copy.deepcopy(tab)
        table = []
        for l in tab:
            table.append(l[:])
        self.tab = table
        self.pai = pai
        self.profundidade = profundidade
        self.custo = custo #custo do no inicial ate este no
        self.f = f #custo da funcao heuristica
        self.linha_espaco = linha_espaco
        self.coluna_espaco = coluna_espaco
        self.acao = acao

    def addTabela(self, tabela):
        self.tab = tabela

    def changeTile(self, x, y, newX, newY):
        aux1 = self.tab[newY][newX]
        self.tab[newY][newX] = 0
        self.tab[y][x] = aux1

def isSolution (state):
    if (state[0] == [0, 1, 2]):
        if (state[1] == [3, 4, 5]):
            if (state[2] == [6, 7, 8]):
                print('aqui')
                return True
    return False

def printTable(node):
    for y in node.tab:
        print(y)
#MOVIMENTOS
#para cima:

def expandeNode (node):
    y = 0
    for aux in node:
        try:
            x = aux.index(0)
            vazio = [x,y]
            break
        except:
            pass
        y += 1
        #vazio = [x, y]
    if x == 0:
        if y == 0: # dois nos criados
            newNode1 = State('ex1', 1, '1', 0, x, y, '1 no', node)
            newNode2 = State('ex2', 1, '1', 0, x, y, '2 no', node)
            newNode1.changeTile(x, y, x + 1, y)
            newNode2.changeTile(x, y, x, y + 1)
            printTable(newNode1)
            printTable(newNode2)
            frontier.append(newNode1)
            frontier.append(newNode2)

        elif y == 1:
            newNode1 = State('ex1', 1, '1', 0, x, y, '1 no', node)
            newNode2 = State('ex1', 1, '1', 0, x, y, '1 no', node)
            newNode3 = State('ex1', 1, '1', 0, x, y, '1 no', node)

            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x, y + 1)

            frontier.append(newNode1)
            frontier.append(newNode2)
            frontier.append(newNode3)

        elif y == 2:
            print('oi2')
            pass
    elif x == 1:
        pass
    elif x == 2:
        pass

estado = [[0,0,0],[0,0,0],[0,0,0]]
print("Digite a configuracao do estado inicial, linha a linha:")
print(" Digite os valores da primeira linha:")
estado[0][0] = int(input())
estado[0][1] = int(input())
estado[0][2] = int(input())
print(" Digite os valores da segunda linha:")
estado[1][0] = int(input())
estado[1][1] = int(input())
estado[1][2] = int(input())
print(" Digite os valores da terceira linha:")
estado[2][0] = int(input())
estado[2][1] = int(input())
estado[2][2] = int(input())

frontier = []
no = State('raiz', 0, 0, 0, 0, 0, 'criar', estado)
no.addTabela(estado)

frontier.append(no)

explored = []

while True:
    no = frontier.pop()
    estadoAtual = no.tab
    if isSolution(estadoAtual):
        break
    expandeNode(estadoAtual)
    if len(frontier) == 0:
        break
