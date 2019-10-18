import numpy as np
import pandas as pd

class Reparar_vez:

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['nada'] = np.nan

    def reparar(self,index):
        self.__apagar_vez_invalido(index)

    def __apagar_vez_invalido(self,index):
        for letra in self.lista_letras:
            valido_vez = "".join(['valido_vez_',letra])
            vez = "".join(['vez_',letra])
            if self.dataframe.loc[index,(valido_vez)] == False:
                self.dataframe.loc[index,(valido_vez)] = True
                self.dataframe.loc[index,(vez)] = False
