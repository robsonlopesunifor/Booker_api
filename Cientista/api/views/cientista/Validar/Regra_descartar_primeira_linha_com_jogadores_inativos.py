import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_descartar_primeira_linha_com_jogadores_inativos(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = np.nan

    def validar(self,index):
        if self.__primeira_linha_com_jogadores_inativos(index):
            self.dataframe.loc[index,('linha')] = 'descartavel'
        

    def __primeira_linha_com_jogadores_inativos(self,index):
        if self.tem_mais_de_um(index) == False:
            valor = self.__linha_de_hole_cards_inativos(index)
        else:
            valor = False
        return valor

    def __linha_de_hole_cards_inativos(self,index):
        valor = True
        for letra in self.lista_letras:
            hole_cards = "".join(['hole_cards_',letra])
            if self.dataframe.loc[index,(hole_cards)] == False:
                valor = False
        return valor

