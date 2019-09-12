import heapq

class State (object): #preferimos colocar a classe estado aqui
    def __init__(self, pai, profundidade, custo, f, linha_espaco, coluna_espaco, acao, tab):
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

    def changeTile(self, x, y, newX, newY): #funcao que faz a troca do espaco vazio por outro numero em outro espaco
        aux1 = self.tab[newY][newX]
        self.tab[newY][newX] = 0
        self.tab[y][x] = aux1
        self.acao = 'Fazer a troca de ' + str(self.tab[y][x]) + ' com 0' #funcao tambem adiciona a acao ao no

    def heuristica (self): #funcao heuristica
        h = 0
        y = 0
        for i in self.tab:
            x = 0
            for j in i: #para cada valor em cada lista da lista maior, o valor de h é incrementado com a distancia de manhattan
                if j == 1:
                    h += abs(x - 1) + abs(y - 0) #distancia calculada com a funcao abs() do python, que retorna o modulo de um numero
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
        if False: #if apenas para debbug, por padrao esta desativado
            print('-------------- analisando função heuristica ---------------')
            print(h)
            print(self.custo)
            printTable(self)
            print('-------------- fim da analise do no -----------------------')
        self.f = self.custo + h
        
    def __lt__(self, other): #essa funcao serve para a comparacao usada no heapq levar em conta o valor da funcao heuristica em primeiro lugar
        if self.f == other.f: #caso o valor da heuristica seja igual, o no com menor custo eh colocado no comeco da fila de prioridade (heapq)
            return self.f - self.custo < other.f - other.custo
        return self.f < other.f

def isSolution (state): #verificando solucao
    if (state[0] == [0, 1, 2]):
        if (state[1] == [3, 4, 5]):
            if (state[2] == [6, 7, 8]):
                return True
    return False

def printTable(node): #funcao para imprimir a tabela de um jeito mais apresentavel
    if node != 'raiz':
        for y in node.tab:
            print(y)
    else:
        print('raiz')        

def checkSolution (estado): #funcao para determinar se o estado inserido tem solucao
    arr = []
    total = 0
    for x in estado:
        for i in x:
            if i != 0:
                arr.append(i) #a funcao pega todos os numeros inseridos, na ordem e menos o zero, e os coloca em uma lista
    for y in arr:
        for t in range(arr.index(y),len(arr)): #dentro dessa lista, para cada numero eh verificado quando numeros menores que ele estao a sua frente
            if y > arr[t]:
                total += 1
    return ( total % 2 ) #se o total de numeros for par, tem solucao, se for ímpar, nao tem

def expandeNode (node): #funcao para expandir cada no
    y = 0
    for aux in node.tab: #encontrando o zero
        try:
            x = aux.index(0)
            break
        except:
            pass
        y += 1
    #ao final do loop acima, x e y formama posicao onde se encontra o espaco vazio
    if x == 0: #para cada valores de x e y, uma quantidade especifica de nos eh criada
        if y == 0:
            #def __init(self, pai, profundidade, custo, f, linha_espaco, coluna_espaco, acao, tab):
            newNode1 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '1 no', node.tab)
            newNode2 = State(node, node.profundidade + 1, node.custo + 1, 0, x, y, '2 no', node.tab)

            newNode1.changeTile(x, y, x + 1, y)
            newNode2.changeTile(x, y, x, y + 1)

            newNode1.heuristica()
            newNode2.heuristica()


            repeated1 = False
            repeated2 = False
            for state in frontier: #verificando se os nos criados ja pertencem a fronteira
                if (newNode1.tab == state.tab):
                    if newNode1.f < state.f: #caso o no ja esteja na fronteira e tenha funcao heuristica menor, o no subistitui o que esta na fronteira
                        state = newNode1
                    repeated1 = True
                if (newNode2.tab == state.tab):
                    if newNode2.f < state.f:
                        state = newNode2
                    repeated2 = True
            for state in explored: #veriricando se os nos criados ja foram explorados
                if newNode1.tab == state.tab:
                    repeated1 = True
                if newNode2.tab == state.tab:
                    repeated2 = True
            if (not repeated1):
                heapq.heappush(frontier, newNode1) #adicionando os nos criados a fila de prioridade implementada com heapq
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
        no = heapq.heappop(frontier) #retirando primeiro no na fila de prioridade
        explored.append(no) #inserindo na lista de explorados
        if isSolution(no.tab): #caso seja solucao, vamos armazenar o pai de cada no em loop ate atingir a raiz
            node = no.pai
            caminho =[]
            while node.pai != 'raiz':
                caminho.insert(0, node)
                node = node.pai
            for i in caminho: #depois de criar o caminho com os pais dos nos, vamo imprimir cada passo
                print('Passo: ' + str(i.profundidade)) #especificamente para este problema, a quantidade de passos vai ser igual a profundidade do no solucao
                print(i.acao)
                printTable(i)
                print('')
            print('Passo: ' + str(no.profundidade))
            print(no.acao)
            printTable(no)
            print('\nFim!')
            break
        elif (type(no.pai) is str):
            print('\nO estado inicial digitado é:\n')
            printTable(no_raiz)
            print('')
        
        expandeNode(no)
        if len(frontier) == 0:
            break

else:
    print('O estado inicial digitado não tem solução!')