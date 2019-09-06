#import classeEstado as node
import heapq

class State (object):
    def __init__(self, pai = 0, profundidade = 0, custo = 0, f = 0, linha_espaco = 0, coluna_espaco = 0, acao = 'acao'):
        self.tab = [[0,0,0],[0,0,0],[0,0,0]]
        self.pai = pai
        self.profundidade = profundidade
        self.custo = custo #custo do no inicial ate este no
        self.f = f #custo da funcao heuristica
        self.linha_espaco = linha_espaco
        self.coluna_espaco = coluna_espaco
        self.acao = acao

def createTable (no):
    tabela = []
    for y in no.tab:
        tabela.append(y)
    return tabela

def isSolution (state):
    if (state.tab[0] == [0, 1, 2]):
        if (state.tab[1] == [3, 4, 5]):
            if (state.tab[2] == [6, 7, 8]):
                return True
    return False

def printTable(node):
    for y in node.tab:
        print(y)
#MOVIMENTOS
#para cima:

def expandeNode (no):
    y = 0
    for aux in no.tab:
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
            newNode1 = State()
            newNode1.tab = createTable(no)

            newNode2 = State()
            #newNode2.tab = createTable(no)

            aux1 = no.tab[y][x + 1]
            print(aux1)
            aux2 = no.tab[y + 1][x]
            print(aux2)
            #trocando tiles de lugar em cada novo estado
            newNode1.tab[y][x] = aux1
            newNode2.tab[y][x] = aux2

            #colocando vazio nos antigos tiles
            newNode1.tab[y][x + 1] = 0
            newNode2.tab[y + 1][x] = 0
            #ajustando outros parametros dos nos criados
            newNode1.pai = no
            #tab ja coloquei
            newNode1.profundidade = no.profundidade + 1
            newNode1.custo = 0 #mudar com funcao heuristica
            newNode1.f = 0 #colocar funcao heuristica
            newNode1.linha_espaco = y
            newNode1.coluna_espaco = x
            newNode1.acao = 'move ' + str(aux1) + ' to [' + str(x) + ', ' + str(y) + ']'

            newNode2.pai = no
            newNode2.profundidade = no.profundidade + 1
            newNode2.custo = 0 #mudar com funcao heuristica
            newNode2.f = 0 #colocar funcao heuristica
            newNode2.linha_espaco = y
            newNode2.coluna_espaco = x
            newNode2.acao = 'move ' + str(aux2) + ' to [' + str(x) + ', ' + str(y) + ']'

            #print(newNode1.tab)
            printTable(newNode1)
            print('')
            printTable(no)

            #colocando nos criados na lista
            #frontier.append(newNode1)
            #frontier.append(newNode2)


        elif y == 1:
            pass
        elif y == 2:
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
no = State()
no.tab = estado

frontier.append(no)

if (isSolution(no)):
    print(no.tab)

explored = []

while True:
    no = frontier.pop()
    if isSolution(no):
        break
    #print(no.tab)
    expandeNode(no)
    if len(frontier) == 0:
        break
