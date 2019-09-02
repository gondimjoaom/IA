import queue
import classeEstado as node

def isSolution (state):
    if (state.tab[0] == [1, 2, 3]):
        if (state.tab[1] == [4, 5, 6]):
            if (state.tab[2] == [7, 8, 9]):
                return True
    return False

def heuristica (state):

        

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
no = node.State(tab = estado)
frontier.insert(no)

if (isSolution(no)):
    print(no.tab)

explore = []

while True:
    if len(frontier) == 0:
        break
    estado = frontier.pop()
    if isSolution(estado):
        break
