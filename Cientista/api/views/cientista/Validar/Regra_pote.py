import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_pote(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.coluna_apostas = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.dataframe['valido_pote'] = False
        self.dataframe['pote'] = np.nan
        self.dataframe['pote_rodada'] = np.nan
        self.dataframe['mao'] = np.nan
        self.lista_letras = lista_letras
        

    def validar(self,index):
        valor = True
        if self.__aposta_atual_maior_que_anterior(index):
            if self.__regra_pote_igual_soma_pote_rodada_mais_apostas(index):
                valor = True
            else:
                valor = False
        else:
            valor = False
        self.dataframe.loc[index,('valido_pote')] = valor
        

    def __aposta_atual_maior_que_anterior(self,index):
        if self.tem_mais_de_um(index):
            index_anterior = self.index_anterior_da_mesma_tela(index)
            pote_atual = self.dataframe.loc[index,('pote')]
            pote_anterior = self.dataframe.loc[index_anterior,('pote')]
            porcentagem_de_crescimento = (pote_atual/(pote_anterior + 0.001))*100 - 100
            if porcentagem_de_crescimento > -10:
                return True
            else:
                return False
        else:
            return True

    def __regra_pote_igual_soma_pote_rodada_mais_apostas(self,index):
        pote = round((self.dataframe.loc[index,('pote')]),2)
        acumulado = float(self.dataframe.loc[index,('pote_rodada')])
        for letra in self.lista_letras:
            aposta = "".join(['aposta_',letra])
            acumulado += float(self.dataframe.loc[index,(aposta)])
        acumulado = round(acumulado,2)
        porcentagem_de_crescimento = (acumulado/(pote + 0.001))*100 - 100
        if porcentagem_de_crescimento < 5 and porcentagem_de_crescimento > -5:
            return True
        else:
            return False
