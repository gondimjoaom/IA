'''class State:
    def __init__(self, pai, tab, profundidade, custo, f, linha_espaco, coluna_espaco, acao):
        self.pai = 0
        self.tab = [[0,0,0],[0,0,0],[0,0,0]]
        self.profundidade = 0
        self.custo = 0
        self.f = 0
        self.linha_espaco = 0
        self.coluna_espaco = 0
        self.acao = 'acao' '''
tab = [[0,0,0],[0,0,0],[0,0,0]]
class State:
    def __init__(self, pai = 0, tab = tab, profundidade = 0, custo = 0, f = 0, linha_espaco = 0, coluna_espaco = 0, acao = 'acao'):
        self.pai = pai
        self.tab = tab
        self.profundidade = profundidade
        self.custo = custo
        self.f = f
        self.linha_espaco = linha_espaco
        self.coluna_espaco = coluna_espaco
        self.acao = acao