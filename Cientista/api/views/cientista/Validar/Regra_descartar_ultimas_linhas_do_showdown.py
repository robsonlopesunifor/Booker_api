import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_descartar_ultimas_linhas_do_showdown(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = ''

    def validar(self,index):
        if self.__linha_de_hole_cards_inativos(index) and self.tem_mais_de_um(index):
            if self.__hole_cards_anteriores_inativos_e_igual_a_river(index):
                self.dataframe.loc[index,('linha')] = 'descartavel'

    def __hole_cards_anteriores_inativos_e_igual_a_river(self,index):
        index_anterior  = self.index_anterior_da_mesma_tela(index)
        if self.__linha_de_hole_cards_inativos(index_anterior) == True and self.__igual_a_river(index_anterior):
            return True
        return False

    def __igual_a_river(self,index):
        if self.dataframe.loc[index,('bord_etapa')] == 'RIVER':
            return True
        return True

    def __linha_de_hole_cards_inativos(self,index):
        valor = True
        for letra in self.lista_letras:
            hole_cards = "".join(['hole_cards_',letra])
            if self.dataframe.loc[index,(hole_cards)] == False:
                valor = False
        return valor

