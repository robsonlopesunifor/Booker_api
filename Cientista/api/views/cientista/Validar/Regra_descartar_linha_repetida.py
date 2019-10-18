import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_descartar_linha_repetida(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = ''

    def validar(self,index):
        index_anterior = self.index_anterior_da_mesma_tela(index)
        if self.tem_mais_de_um(index):
            if self.__todas_as_vez_sao_false(index_anterior):
                if self.__linha_atual_igual_a_anterior(index):
                    self.dataframe.loc[index_anterior,('linha')] = 'descartavel'
                
        
    def __todas_as_vez_sao_false(self,index):
        if self.tem_mais_de_um(index):
            for idx,letra in enumerate(self.lista_letras):
                vez = "".join(['vez_',letra])
                if self.dataframe.loc[index,(vez)] != False:
                    return False
            return True
        else:
            return False
        

    def __linha_atual_igual_a_anterior(self,index):
        if self.tem_mais_de_um(index):
            index_anterior = self.index_anterior_da_mesma_tela(index)
            linha_atual    = self.__retornar_linha(index)
            linha_anterior = self.__retornar_linha(index_anterior)
            for x in range(len(linha_atual)):
                if linha_atual[x] != linha_anterior[x]:
                    return False
            return True
        return False

    def __retornar_linha(self,index):
        colunas = []
        colunas.append('pote')
        colunas.append('pote_rodada')
        colunas.append('bord_FLOP_1')
        colunas.append('bord_FLOP_2')
        colunas.append('bord_FLOP_3')
        colunas.append('bord_TURN')
        colunas.append('bord_RIVER')
        for idx,letra in enumerate(self.lista_letras):
            #colunas.append("".join(['vez_',letra]))
            colunas.append("".join(['aposta_',letra]))
            colunas.append("".join(['fichas_',letra]))
            colunas.append("".join(['hole_cards_',letra]))
        return self.dataframe[colunas].loc[index]


    
