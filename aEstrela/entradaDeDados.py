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

    def heuristica (self, x, y):
        h = 0
        if self.tab[y][x] == 1:
            h += abs(x - 1) + abs(y - 0)
        elif self.tab[y][x] == 2:
            h += abs(x - 2) + abs(y - 0)
        elif self.tab[y][x] == 3:
            h += abs(x - 0) + abs(y - 1)
        elif self.tab[y][x] == 4:
            h += abs(x - 1) + abs(y - 1)
        elif self.tab[y][x] == 5:
            h += abs(x - 2) + abs(y - 1)
        elif self.tab[y][x] == 6:
            h += abs(x - 0) + abs(y - 2)
        elif self.tab[y][x] == 7:
            h += abs(x - 1) + abs(y - 2)
        elif self.tab[y][x] == 8:
            h += abs(x - 2) + abs(y - 2)
        return self.custo + h
        

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
    for aux in node.tab:
        try:
            x = aux.index(0)
            #vazio = [x,y]
            break
        except:
            pass
        y += 1
        #vazio = [x, y]
    if x == 0:
        if y == 0: # dois nos criados
            f = node.heuristica(x, y)
            newNode1 = State(node, node.profundidade + 1, f, no.custo, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, f, no.custo, x, y, '2 no', node.tab)
            newNode1.changeTile(x, y, x + 1, y)
            newNode2.changeTile(x, y, x, y + 1)
            #printTable(newNode1)
            #printTable(newNode2)
            frontier.append(newNode1)
            frontier.append(newNode2)

        elif y == 1:
            newNode1 = State('ex1', 1, '1', 0, x, y, '1 no', node.tab)
            newNode2 = State('ex1', 1, '1', 0, x, y, '1 no', node.tab)
            newNode3 = State('ex1', 1, '1', 0, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x, y + 1)

            frontier.append(newNode1)
            frontier.append(newNode2)
            frontier.append(newNode3)

        elif y == 2:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            
            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)
            #print('aqui')
            frontier.append(newNode1)
            frontier.append(newNode2)
    elif x == 1:
        if y == 0:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode3 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y + 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x - 1, y)

            frontier.append(newNode1)
            frontier.append(newNode2)
            frontier.append(newNode3)
        elif y == 1:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode3 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode4 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y + 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x - 1, y)
            newNode4.changeTile(x, y, x , y - 1)

            frontier.append(newNode1)
            frontier.append(newNode2)
            frontier.append(newNode3)
            frontier.append(newNode4)
        elif y == 2:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode3 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            #print('aqui2')
            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x - 1, y)

            frontier.append(newNode1)
            frontier.append(newNode2)
            frontier.append(newNode3)
    elif x == 2:
        if y == 0:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex2', 1, '1', no.custo, x, y, '2 no', node.tab)

            newNode1.changeTile(x, y, x - 1, y)
            newNode2.changeTile(x, y, x, y + 1)

            frontier.append(newNode1)
            frontier.append(newNode2)
        elif y == 1:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode3 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x - 1, y)
            newNode3.changeTile(x, y, x, y + 1)

            frontier.append(newNode1)
            frontier.append(newNode2)
            frontier.append(newNode3)
        elif y == 2:
            newNode1 = State('ex1', 1, '1', no.custo, x, y, '1 no', node.tab)
            newNode2 = State('ex2', 1, '1', no.custo, x, y, '2 no', node.tab)

            newNode1.changeTile(x, y, x - 1, y)
            newNode2.changeTile(x, y, x, y - 1)

            frontier.append(newNode1)
            frontier.append(newNode2)

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
    print(estadoAtual)
    if isSolution(estadoAtual):
        break
    
    expandeNode(no)
    if len(frontier) == 0:
        break
