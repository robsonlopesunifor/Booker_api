import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_bord(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        
    def iniciar(self,dataframe):
        self.dataframe = dataframe
        self.dataframe['bord_FLOP_1'] = np.nan
        self.dataframe['bord_FLOP_2'] = np.nan
        self.dataframe['bord_FLOP_3'] = np.nan
        self.dataframe['bord_TURN'] = np.nan
        self.dataframe['bord_RIVER'] = np.nan
        self.dataframe['valido_bord'] = np.nan
        self.dataframe['bord_etapa'] = np.nan


    def validar(self,index):
        
        valor = False
        if(self.regra_etapa_existente(index)):
            if(self.regra_etapa_superior_a_anterior(index)):
                valor = True
        self.dataframe.loc[index,('valido_bord')] = valor

    def regra_etapa_existente(self,index):
        if self.etapa(index) != 0:
            return True
        else:
            return False

    def regra_etapa_superior_a_anterior(self,index):
        valor = False
        etapa_atual = self.etapa(index)
          
        if self.tem_mais_de_um(index):
            etapa_penultima = self.etapa(self.index_anterior_da_mesma_tela(index))
            if etapa_penultima == etapa_atual or etapa_penultima < etapa_atual:
                valor = True
        else:
            valor = True
        return valor
            

    def etapa(self,index):
        linha_bord = self.dataframe.loc[index].copy()
        valor = 0
        bord_etapa = 'null'
        linha_bord.loc[linha_bord.isnull()] = ''
        bord_FLOP_1 = linha_bord['bord_FLOP_1'] 
        bord_FLOP_2 = linha_bord['bord_FLOP_2']
        bord_FLOP_3 = linha_bord['bord_FLOP_3']
        bord_TURN = linha_bord['bord_TURN']
        bord_RIVER = linha_bord['bord_RIVER']
        
        if (bord_FLOP_1 == '' and bord_FLOP_2 == '' and bord_FLOP_3 == '' and bord_TURN == '' and bord_RIVER == ''):
            valor = 1
            bord_etapa = 'PRE_FLOP' 
        elif (bord_FLOP_1 != '' and bord_FLOP_2 != '' and bord_FLOP_3 != '' and bord_TURN == '' and bord_RIVER == ''):
            valor = 2
            bord_etapa = 'FLOP' 
        elif (bord_FLOP_1 != '' and bord_FLOP_2 != '' and bord_FLOP_3 != '' and bord_TURN != '' and bord_RIVER == ''):
            valor = 3
            bord_etapa = 'TURN'
        elif (bord_FLOP_1 != '' and bord_FLOP_2 != '' and bord_FLOP_3 != '' and bord_TURN != '' and bord_RIVER != ''):
            valor = 4
            bord_etapa = 'RIVER'
        self.dataframe.loc[index,('bord_etapa')] = bord_etapa
        return valor


