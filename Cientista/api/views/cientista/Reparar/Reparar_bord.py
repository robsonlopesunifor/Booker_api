import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Reparar_bord(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        
    def iniciar(self,dataframe):
        self.dataframe = dataframe
        self.dataframe['nada'] = np.nan
        self.dataframe['bord_etapa'] = np.nan

    def reparar(self,index):
        self.__reparar_bord_atual_com_anterior(index)
        self.__definir_etapa(index)

    def __reparar_bord_atual_com_anterior(self,index):
        tamanho = self.total_de_lisnha(index)
        index_anterior = self.index_anterior_da_mesma_tela(index)
        if tamanho > 1:
            if self.dataframe.loc[index,('valido_bord')] == False:
                self.dataframe.loc[index,('bord_FLOP_1')] = self.dataframe.loc[index_anterior,('bord_FLOP_1')]
                self.dataframe.loc[index,('bord_FLOP_2')] = self.dataframe.loc[index_anterior,('bord_FLOP_2')]
                self.dataframe.loc[index,('bord_FLOP_3')] = self.dataframe.loc[index_anterior,('bord_FLOP_3')]
                self.dataframe.loc[index,('bord_TURN')]   = self.dataframe.loc[index_anterior,('bord_TURN')]
                self.dataframe.loc[index,('bord_RIVER')]  = self.dataframe.loc[index_anterior,('bord_RIVER')]

    def __definir_etapa(self,index):
        linha_bord = self.dataframe.loc[index].copy()
        valor = 'null'
        linha_bord.loc[linha_bord.isnull()] = ''
        bord_FLOP_1 = linha_bord['bord_FLOP_1'] 
        bord_FLOP_2 = linha_bord['bord_FLOP_2']
        bord_FLOP_3 = linha_bord['bord_FLOP_3']
        bord_TURN = linha_bord['bord_TURN']
        bord_RIVER = linha_bord['bord_RIVER']
        
        if (bord_FLOP_1 == '' and bord_FLOP_2 == '' and bord_FLOP_3 == '' and bord_TURN == '' and bord_RIVER == ''):
            valor = 'PRE_FLOP' 
        elif (bord_FLOP_1 != '' and bord_FLOP_2 != '' and bord_FLOP_3 != '' and bord_TURN == '' and bord_RIVER == ''):
            valor = 'FLOP' 
        elif (bord_FLOP_1 != '' and bord_FLOP_2 != '' and bord_FLOP_3 != '' and bord_TURN != '' and bord_RIVER == ''):
            valor = 'TURN'
        elif (bord_FLOP_1 != '' and bord_FLOP_2 != '' and bord_FLOP_3 != '' and bord_TURN != '' and bord_RIVER != ''):
            valor = 'RIVER'
        self.dataframe.loc[index,('bord_etapa')] = valor
