#import classeEstado as node
import heapq

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
        self.acao = 'trocar ' + str(self.tab[y][x]) + ' com o 0'

    def heuristica (self):
        h = 0
        y = 0
        for i in self.tab:
            x = 0
            for j in i:
                if j == 1:
                    h += abs(x - 1) + abs(y - 0)
                elif j == 2:
                    h += abs(x - 2) + abs(y - 0)
                elif j == 3:
                    h += abs(x - 0) + abs(y - 1)
                elif j == 4:
                    h += abs(x - 1) + abs(y - 1)
                elif j == 5:
                    h += abs(x - 2) + abs(y - 1)
                elif j == 6:
                    h += abs(x - 0) + abs(y - 2)
                elif j == 7:
                    h += abs(x - 1) + abs(y - 2)
                elif j == 8:
                    h += abs(x - 2) + abs(y - 2)
                x += 1
            y += 1
                
        #print(h)
        self.f = self.custo + h
        return self.custo + h
        
    def __lt__(self, other):
        return self.f < other.f

def isSolution (state):
    if (state[0] == [0, 1, 2]):
        if (state[1] == [3, 4, 5]):
            if (state[2] == [6, 7, 8]):
                #print('aqui')
                return True
    return False

def printTable(node):
    if node != 'raiz':
        for y in node.tab:
            print(y)
    else:
        print('raiz')        
#MOVIMENTOS
#para cima:

def checkSolution (estado):
    arr = []
    total = 0
    for x in estado:
        for i in x:
            if i != 0:
                arr.append(i)
    for y in arr:
        for t in range(arr.index(y),len(arr)):
            #print('de ' + str(arr.index(y)) + ' a ' + str(len(arr)))
            if y > arr[t]:
                #print(y)
                #print(arr[t])
                total += 1
    #print(total)
    return ( total % 2 )

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
            #def __init(self, pai, profundidade, custo, f, linha_espaco, coluna_espaco, acao, tab):
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)

            newNode1.changeTile(x, y, x + 1, y)
            newNode2.changeTile(x, y, x, y + 1)

            newNode1.heuristica()
            newNode2.heuristica()


            repeated1 = False
            repeated2 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)            

        elif y == 1:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)
            newNode3 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x, y + 1)

            newNode1.heuristica()
            newNode2.heuristica()
            newNode3.heuristica()
            
            repeated1 = False
            repeated2 = False
            repeated3 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)
            if (not repeated3):
                heapq.heappush(frontier, newNode3)

        elif y == 2:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)
            
            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)

            newNode1.heuristica()
            newNode2.heuristica()

            repeated1 = False
            repeated2 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)

    elif x == 1:
        
        if y == 0:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)
            newNode3 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y + 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x - 1, y)

            newNode1.heuristica()
            newNode2.heuristica()
            newNode3.heuristica()

            repeated1 = False
            repeated2 = False
            repeated3 = False
            for state in frontier:
                if (newNode1.tab == state.tab and newNode1.f > state.f): #mudando de branch, isso aqui estava como os outros
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)
            if (not repeated3):
                heapq.heappush(frontier, newNode3)

        elif y == 1:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)
            newNode3 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode4 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y + 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x - 1, y)
            newNode4.changeTile(x, y, x , y - 1)

            newNode1.heuristica()
            newNode2.heuristica()
            newNode3.heuristica()
            newNode4.heuristica()

            repeated1 = False
            repeated2 = False
            repeated3 = False
            repeated4 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
                if newNode4.tab == state.tab:
                    repeated4 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
                if newNode4.tab == state.tab:
                    repeated4 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)
            if (not repeated3):
                heapq.heappush(frontier, newNode3)
            if (not repeated4):
                heapq.heappush(frontier, newNode4)

        elif y == 2:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)
            newNode3 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x + 1, y)
            newNode3.changeTile(x, y, x - 1, y)

            newNode1.heuristica()
            newNode2.heuristica()
            newNode3.heuristica()

            repeated1 = False
            repeated2 = False
            repeated3 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)
            if (not repeated3):
                heapq.heappush(frontier, newNode3)

    elif x == 2:
        if y == 0:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)

            newNode1.changeTile(x, y, x - 1, y)
            newNode2.changeTile(x, y, x, y + 1)

            newNode1.heuristica()
            newNode2.heuristica()

            repeated1 = False
            repeated2 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)
            
        elif y == 1:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)
            newNode3 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)

            newNode1.changeTile(x, y, x, y - 1)
            newNode2.changeTile(x, y, x - 1, y)
            newNode3.changeTile(x, y, x, y + 1)

            newNode1.heuristica()
            newNode2.heuristica()
            newNode3.heuristica()

            repeated1 = False
            repeated2 = False
            repeated3 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
                if newNode3.tab == state.tab:
                    repeated3 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)
            if (not repeated3):
                heapq.heappush(frontier, newNode3)

        elif y == 2:
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)

            newNode1.changeTile(x, y, x - 1, y)
            newNode2.changeTile(x, y, x, y - 1)

            newNode1.heuristica()
            newNode2.heuristica()

            repeated1 = False
            repeated2 = False
            for state in frontier:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            for state in explored:
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1)
            if (not repeated2):
                heapq.heappush(frontier, newNode2)


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

if (checkSolution(estado) == 0 or False):

    frontier = []
    no = State('raiz', 0, 0, 0, 0, 0, 'raiz', estado)
    no.pai = no
    no.addTabela(estado)

    #frontier.append(no)

    heapq.heappush(frontier,no)

    explored = []

    while True:
        #for x in frontier:
        #    printTable(x)
        #    print('')
        #print(len(frontier))
        explored.append(no)
        #printTable(no)
        #print('--------------------------------------------')
        no = heapq.heappop(frontier)
        if isSolution(no.tab):
            print('Passo: ' + str(no.profundidade))
            print(no.acao)
            printTable(no)
            print('Fim!')
            break
        if (type(no.pai) is str):
            print(no.pai)
        else:
            print('Passo: ' + str(no.profundidade))
            print(no.acao)
            printTable(no)
            
        #print(no.f)
        #printTable(no)
        print('')
        
        expandeNode(no)
        if len(frontier) == 0:
            break

else:
    print('Sem solucao!')