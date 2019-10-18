
import pandas as pd
from .Regra_diler import Regra_diler
from .Regra_bord import Regra_bord
from .Regra_mao import Regra_mao
from .Regra_pote import Regra_pote
from .Regra_pote_rodada import Regra_pote_rodada
from .Regra_aposta import Regra_aposta
from .Regra_hole_cards import Regra_hole_cards
from .Regra_combo import Regra_combo
#from Regra_linhas_descartaveis import Regra_linhas_descartaveis
from .Regra_descartar_primeira_linha_com_jogadores_inativos import Regra_descartar_primeira_linha_com_jogadores_inativos
from .Regra_descartar_ultimas_linhas_do_showdown import Regra_descartar_ultimas_linhas_do_showdown
from .Regra_descartar_linha_repetida import Regra_descartar_linha_repetida
from .Regra_vez import Regra_vez


class Validador(object):

    def __init__(self):
        self.regra_mao = Regra_mao()
        self.regra_diler = Regra_diler()
        self.regra_bord = Regra_bord()
        self.regra_pote = Regra_pote()
        self.regra_pote_rodada = Regra_pote_rodada()
        self.regra_aposta = Regra_aposta()
        self.regra_hole_cards = Regra_hole_cards()
        self.regra_combo = Regra_combo()
        #self.regra_linhas_descartaveis = Regra_linhas_descartaveis()
        self.regra_descartar_primeira_linha_com_jogadores_inativos = Regra_descartar_primeira_linha_com_jogadores_inativos()
        self.regra_descartar_ultimas_linhas_do_showdown = Regra_descartar_ultimas_linhas_do_showdown()
        self.regra_descartar_linha_repetida = Regra_descartar_linha_repetida()
        self.regra_vez = Regra_vez()
        self.dataframe_valido = pd.DataFrame()

    def iniciar(self,datagrama):
        self.dataframe_valido = datagrama
        self.regra_mao.iniciar(self.dataframe_valido)
        self.regra_diler.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_bord.iniciar(self.dataframe_valido)
        self.regra_pote.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_pote_rodada.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_aposta.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_hole_cards.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_combo.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        #self.regra_linhas_descartaveis.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_descartar_primeira_linha_com_jogadores_inativos.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_descartar_ultimas_linhas_do_showdown.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_descartar_linha_repetida.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])
        self.regra_vez.iniciar(self.dataframe_valido,['A','B','C','D','E','F'])

    def validar(self,index):
        self.regra_mao.definir_mao(index)
        self.regra_bord.validar(index)
        self.regra_diler.validar(index)
        self.regra_pote.validar(index)
        self.regra_pote_rodada.validar(index)
        self.regra_aposta.validar(index)
        self.regra_hole_cards.validar(index)
        self.regra_combo.validar(index)
        #self.regra_linhas_descartaveis.validar(index)
        self.regra_descartar_primeira_linha_com_jogadores_inativos.validar(index)
        self.regra_descartar_ultimas_linhas_do_showdown.validar(index)
        self.regra_descartar_linha_repetida.validar(index)
        self.regra_vez.validar(index)
        



      
