import queue
import classeEstado as node
import heapq

def isSolution (state):
    if (state.tab[0] == [0, 1, 2]):
        if (state.tab[1] == [3, 4, 5]):
            if (state.tab[2] == [6, 7, 8]):
                return True
    return False

#MOVIMENTOS
#para cima: 

def expandeNode (no):
    for y in no.tab:
        try:
            x = y.index(0)
            vazio = [x,y]
        except:
            pass
        #vazio = [x, y]
    if x == 0:
        if y == 0: # dois nós criados
            newNode1 = node.State()
            newNode2 = node.State()
            aux1 = no.tab[y][x + 1]
            aux2 = no.tab[y + 1][x]
            newNode1.tab = no.tab
            newNode2.tab = no.tab
            #trocando tiles de lugar em cada novo estado
            newNode1.tab[y][x] = aux1
            newNode2.tab[y][x] = aux2
            #colocando vazio nos antigos tiles
            newNode1.tab[y][x + 1] = 0
            newNode2.tab[y + 1][x] = 0
            #ajustando outros parâmetros dos nos criados
            newNode1.pai = no
            newNode1.profundidade = no.profundidade + 1
            newNode1.custo = 0 #mudar com funcao heuristica
            newNode1.f = 0 #colocar funcao heuristica
            newNode1.linha_espaco = y
            newNode1.coluna_espaco = x
            newNode1.acao = 'move ' + aux1 + ' to'
            newNode2.pai = no
            #colocando nos criados na lista
            frontier.append(newNode1)
            frontier.append(newNode2)
        elif y == 1:

        elif y == 2:

estado = [[0,0,0],[0,0,0],[0,0,0]]
print("Digite a configuracao do estado inicial, linha a linha:")
print("Digite os valores da primeira linha:")
estado[0][0] = int(input())     
estado[0][1] = int(input())
estado[0][2] = int(input())
print("Digite os valores da segunda linha:")  
estado[1][0] = int(input())     
estado[1][1] = int(input())
estado[1][2] = int(input())
print("Digite os valores da terceira linha:")  
estado[2][0] = int(input())     
estado[2][1] = int(input())
estado[2][2] = int(input())

frontier = []
no = node.State()
no.tab = estado
frontier.insert(no)

if (isSolution(no)):
    print(no.tab)

explore = []

while True:
    if isSolution(estado):
        break
    if len(frontier) == 0:
        break
    estado = frontier.pop()
