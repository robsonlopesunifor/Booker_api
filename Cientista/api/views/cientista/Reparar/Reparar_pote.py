import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Reparar_pote(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = np.nan

    def reparar(self,index):
        self.__somar_apostas_com_pote_rodada(index)

    def __somar_apostas_com_pote_rodada(self,index):
        if self.dataframe.loc[index,('valido_pote')] == False:
            pote_rodada = float(self.dataframe.loc[index,('pote_rodada')])
            soma_das_apostas = self.__somar_apostas(index)
            pote_atualizado = (soma_das_apostas + pote_rodada)
            self.dataframe.loc[index,('pote')] = abs(round(pote_atualizado,2))

    def __somar_apostas(self,index):
        total = 0
        for letra in self.lista_letras:
            aposta = "".join(['aposta_',letra])
            total += float(self.dataframe.loc[index,(aposta)])
        return total
