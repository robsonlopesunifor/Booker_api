import numpy as np
import pandas as pd
import random 
from ..Auxiliar import Auxiliar


class Regra_mao(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.coluna_mao = ['']

    def iniciar(self,dataframe):
        self.dataframe = dataframe
        self.dataframe['pote'] = np.nan
        self.dataframe['mao'] = 1
        

    def definir_mao(self,index):
        if self.tem_mais_de_um(index):
            mao = self.dataframe.loc[self.index_anterior_da_mesma_tela(index),('mao')]
            if self.__e_nova_mao(index) == True:
                self.dataframe.loc[index,('mao')] = random.randrange(1000000000)
            else:
                self.dataframe.loc[index,('mao')] = mao
        else:
            self.dataframe.loc[index,('mao')] = random.randrange(1000000000)

    def __e_nova_mao(self,index):
        if self.tem_mais_de_um(index):
            if self.__pote_atual_menor_pote_anterior(index) == True:
                if self.__e_preflop(index) == True:
                    return True
        return False

    def __pote_atual_menor_pote_anterior(self,index):
        pote_atual = self.dataframe.loc[index,('pote')]
        pote_anterior = self.dataframe.loc[self.index_anterior_da_mesma_tela(index),('pote')]
        porcentagem_de_crescimento = (pote_atual/(pote_anterior + 0.001))*100 - 100
        if porcentagem_de_crescimento < -50:
            return True
        else:
            return False
        

    def __e_preflop(self,index):
        linha_bord = self.dataframe.loc[index].copy()
        linha_bord.loc[linha_bord.isnull()] = ''
        bord_FLOP_1 = linha_bord['bord_FLOP_1'] 
        bord_FLOP_2 = linha_bord['bord_FLOP_2']
        bord_FLOP_3 = linha_bord['bord_FLOP_3']
        bord_TURN = linha_bord['bord_TURN']
        bord_RIVER = linha_bord['bord_RIVER']
        
        if (bord_FLOP_1 == '' and bord_FLOP_2 == '' and bord_FLOP_3 == '' and bord_TURN == '' and bord_RIVER == ''):
            return True
        else:
            return False

    def tem_mais_de_um(self,index):
        linhas_anteriores = self.dataframe.loc[:index]
        mesmas_tela = linhas_anteriores[linhas_anteriores['tela'] == linhas_anteriores.loc[index, ('tela')]]
        tamanho = len(mesmas_tela)
        if tamanho > 1:
            return True
        else:
            return False

    def index_anterior_da_mesma_tela(self,idx):
        if idx > 0:
            for decremento in range(1, idx + 1):
                idx_reverco = idx - decremento
                anterior = self.dataframe.iloc[idx_reverco]
                atual = self.dataframe.iloc[idx]
                if (atual['tela'] == anterior['tela']):
                    return idx_reverco
        return -1
