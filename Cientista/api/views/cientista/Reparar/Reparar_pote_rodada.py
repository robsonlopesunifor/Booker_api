import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Reparar_pote_rodada(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = np.nan

    def reparar(self,index):
        self.__reparar_pote_de_acordo_com_a_etapa(index)

    def __reparar_pote_de_acordo_com_a_etapa(self,index):
        
        if self.dataframe.loc[index,('valido_pote_rodada')] == False:
            pote = self.dataframe.loc[index,('pote')]
            index_anterior = self.index_anterior_da_mesma_tela(index)
            pote_rodada_anterior = self.dataframe.loc[index_anterior,('pote_rodada')]
            bord_etapa_atual = self.dataframe.loc[index,('bord_etapa')]
            bord_etapa_anterior = self.dataframe.loc[index_anterior,('bord_etapa')]
            if bord_etapa_atual == bord_etapa_anterior:
                self.dataframe.loc[index,('pote_rodada')] = pote_rodada_anterior
            else:
                self.dataframe.loc[index,('pote_rodada')] = pote

