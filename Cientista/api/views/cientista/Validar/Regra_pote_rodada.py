import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_pote_rodada(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.coluna_apostas = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.dataframe['valido_pote_rodada'] = np.nan
        self.dataframe['pote'] = np.nan
        self.dataframe['pote_rodada'] = np.nan
        self.dataframe['mao'] = np.nan
        for letra in lista_letras:
            apostas = "".join(['aposta_',letra])
            self.coluna_apostas.append(apostas)

    def validar(self,index): 
        valor = self.__regra_pote_rodada_igual_pote_ou_pote_rodada_anterior(index)
        self.dataframe.loc[index,('valido_pote_rodada')] = valor

    def __regra_pote_rodada_igual_pote_ou_pote_rodada_anterior(self,index):
        if self.tem_mais_de_um(index):
            if self.__e_mesma_etapa(index):
                return self.__pote_rodada_igual_pote_rodada_anterior(index)
            else:
                return self.__regra_pote_rodada_igual_pote(index)
        else:
            return True

    def __regra_pote_rodada_igual_pote(self,index):
        pote = self.dataframe.loc[index,('pote')]
        pote_rodada = self.dataframe.loc[index,('pote_rodada')]
        if pote_rodada == pote:
            return True
        else:
            return False

    def __pote_rodada_igual_pote_rodada_anterior(self,index):
        pote_rodada = self.dataframe.loc[index,('pote_rodada')]
        index_anterio = self.index_anterior_da_mesma_tela(index)
        pote_rodada_anterior = self.dataframe.loc[index_anterio,('pote_rodada')]
        if pote_rodada == pote_rodada_anterior:
            return True
        else:
            return False

    def __e_mesma_etapa(self,index):
        index_anterio = self.index_anterior_da_mesma_tela(index)
        flop_1_anterio = self.dataframe.loc[index_anterio,('bord_FLOP_1')]
        flop_2_anterio = self.dataframe.loc[index_anterio,('bord_FLOP_2')]
        flop_3_anterio = self.dataframe.loc[index_anterio,('bord_FLOP_3')]
        turn_anterio   = self.dataframe.loc[index_anterio,('bord_TURN')]
        river_anterio  = self.dataframe.loc[index_anterio,('bord_RIVER')]
        bord_anterior = "".join([flop_1_anterio,flop_2_anterio,flop_3_anterio,turn_anterio,river_anterio])

        flop_1 = self.dataframe.loc[index,('bord_FLOP_1')]
        flop_2 = self.dataframe.loc[index,('bord_FLOP_2')]
        flop_3 = self.dataframe.loc[index,('bord_FLOP_3')]
        turn   = self.dataframe.loc[index,('bord_TURN')]
        river  = self.dataframe.loc[index,('bord_RIVER')]
        bord = "".join([flop_1,flop_2,flop_3,turn,river])

        if bord_anterior == bord:
            return True
        else:
            return False
