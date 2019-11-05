import pandas as pd
from .Reparar_hole_cards import Reparar_hole_cards
from .Reparar_aposta import Reparar_aposta
from .Reparar_vencedor import Reparar_vencedor
from .Reparar_pote_rodada import Reparar_pote_rodada
from .Reparar_bord import Reparar_bord
from .Reparar_pote import Reparar_pote
from .Reparar_adicionar_degral import Reparar_adicionar_degral
from .Reparar_adicionar_linha import Reparar_adicionar_linha
from .Reparar_vez import Reparar_vez

class Reparar(object):

    def __init__(self):
        self.reparar_hole_cards = Reparar_hole_cards()
        self.reparar_bord = Reparar_bord()
        self.reparar_aposta = Reparar_aposta()
        self.reparar_vencedor = Reparar_vencedor() #TODO: ainda precisa melhorar. Nso esta tresendo o vencedor(es)
        self.reparar_pote_rodada = Reparar_pote_rodada()
        self.reparar_pote = Reparar_pote()
        self.reparar_adicionar_degral = Reparar_adicionar_degral()
        self.reparar_adicionar_linha = Reparar_adicionar_linha()
        self.reparar_vez = Reparar_vez()
        self.dataframe_reparado = pd.DataFrame()

    def iniciar(self,datagrama):
        self.dataframe_reparado = datagrama
        self.reparar_hole_cards.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_bord.iniciar(self.dataframe_reparado)
        self.reparar_aposta.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_vencedor.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_pote_rodada.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_pote.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_adicionar_degral.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_adicionar_linha.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        self.reparar_vez.iniciar(self.dataframe_reparado,['A','B','C','D','E','F'])
        
    def reparar(self,index):
        self.reparar_hole_cards.reparar(index)
        self.reparar_bord.reparar(index)
        self.reparar_aposta.reparar(index)
        self.reparar_vencedor.reparar(index)
        self.reparar_pote_rodada.reparar(index)
        self.reparar_pote.reparar(index)
        self.reparar_adicionar_degral.reparar(index)
        self.reparar_adicionar_linha.reparar(index)
        self.reparar_vez.reparar(index)
