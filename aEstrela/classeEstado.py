class State:
    def _init_(self):
        self.pai = 0
        self.tab = [[0,0,0],[0,0,0],[0,0,0]]
        self.profundidade = 0
        self.custo = 0
        self.acao ="acao"
        self.f = 0
        self.linha_espaco = 0
        self.coluna_espaco = 0