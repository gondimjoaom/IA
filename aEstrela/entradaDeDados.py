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
        self.acao = 'Fazer a troca de ' + str(self.tab[y][x]) + ' com 0'

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
        if False:        
            print('-------------- analisando função heuristica ---------------')
            print(h)
            print(self.custo)
            printTable(self)
            print('-------------- fim da analise do no -----------------------')
        self.f = self.custo + h
        return self.custo + h
        
    def __lt__(self, other):
        if self.f == other.f:
            return self.f - self.custo < other.f - other.custo
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
    for aux in node.tab: #encontrando o zero
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
                    repeated2 = True
                if (newNode3.tab == state.tab):
                    if newNode3.f < state.f:
                        state = newNode3
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
                    repeated2 = True
                if (newNode3.tab == state.tab):
                    if newNode3.f < state.f:
                        state = newNode3
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
                    repeated2 = True
                if (newNode3.tab == state.tab):
                    if newNode3.f < state.f:
                        state = newNode3
                    repeated3 = True
                if (newNode4.tab == state.tab):
                    if newNode4.f < state.f:
                        state = newNode4
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
                    repeated2 = True
                if (newNode3.tab == state.tab):
                    if newNode3.f < state.f:
                        state = newNode3
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
                    repeated2 = True
                if (newNode3.tab == state.tab):
                    if newNode3.f < state.f:
                        state = newNode3
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
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f:
                        state = newNode1                    
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
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

no_solucao = State('solucao', 0, 0, 0, 0, 0, 'raiz', [[0,1,2],[3,4,5],[6,7,8]])
estado = [[0,0,0],[0,0,0],[0,0,0]]

print('Bem vindo ao jogo 8-puzzle! \nO estado de aceitação é:\n')
printTable(no_solucao)
print('')
print('================= Vamos começar! ======================\n')

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
    no_raiz = State('raiz', 0, 0, 0, 0, 0, 'raiz', estado)

    heapq.heappush(frontier,no_raiz)

    explored = []
    explored.append(no_raiz)
    while True:
        no = heapq.heappop(frontier)
        explored.append(no)
        if isSolution(no.tab):
            node = no.pai
            caminho =[]
            while node.pai != 'raiz':
                caminho.insert(0, node)
                node = node.pai
            #printTable(no_raiz)
            for i in caminho:
                print('Passo: ' + str(i.profundidade))
                print(i.acao)
                printTable(i)
                print('')
            print('Passo: ' + str(no.profundidade))
            print(no.acao)
            printTable(no)
            print('\nFim!')
            break
        elif (type(no.pai) is str):
            #print(no.pai)
            print('\nO estado inicial digitado é:\n')
            printTable(no_raiz)
            print('')
        
        expandeNode(no)
        if len(frontier) == 0:
            break

else:
    print('O estado inicial digitado não tem solução!')