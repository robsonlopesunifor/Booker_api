import pandas as pd
from .Analizar_heroi import Analizar_heroi
from .Analizar_showdown import Analizar_showdown
from .Analizar_ultimo_jogador import Analizar_ultimo_jogador
from .Analizar_size_bet import Analizar_size_bet
from .Analizar_nome import Analizar_nome

class Analizar(object):

    def __init__(self):
        self.analizar_heroi = Analizar_heroi()
        self.analizar_showdown = Analizar_showdown()
        self.analizar_ultimo_jogador = Analizar_ultimo_jogador()
        self.analizar_size_bet = Analizar_size_bet()
        self.analizar_nome = Analizar_nome()
        self.dataframe_analizar = pd.DataFrame()

    def iniciar(self,dataframe):
        self.dataframe_analizar = dataframe
        self.analizar_heroi.iniciar(self.dataframe_analizar,['A','B','C','D','E','F'])
        self.analizar_showdown.iniciar(self.dataframe_analizar,['A','B','C','D','E','F'])
        self.analizar_ultimo_jogador.iniciar(self.dataframe_analizar,['A','B','C','D','E','F'])
        self.analizar_size_bet.iniciar(self.dataframe_analizar,['A','B','C','D','E','F'])
        self.analizar_nome.iniciar(self.dataframe_analizar)

    def analizar(self,index):
        self.analizar_heroi.analizar(index)
        self.analizar_showdown.analizar(index)
        self.analizar_ultimo_jogador.analizar(index)
        self.analizar_size_bet.analizar(index)
        self.analizar_nome.analizar(index)
