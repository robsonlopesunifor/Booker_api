import numpy as np
import pandas as pd

class Analizar_showdown:

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['showdown'] = np.nan

    def analizar(self,index):
        self.__showdown(index)

    def __showdown(self,index):
        if self.__quantidade_de_combos(index) > 1:
            self.dataframe.loc[index,('showdown')] = True
        else:
            self.dataframe.loc[index,('showdown')] = False

    def __quantidade_de_combos(self,index):
        quantidade_de_combos = 0
        for idx,letra in enumerate(self.lista_letras):
            combo_str = "".join(['combo_',letra,'_1'])
            if self.dataframe.loc[index,(combo_str)] != '':
                quantidade_de_combos += 1
        return quantidade_de_combos
