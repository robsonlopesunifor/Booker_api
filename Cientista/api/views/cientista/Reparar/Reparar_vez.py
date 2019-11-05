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
        quantidade = self.__quantidade_de_vez(index)
        if quantidade > 1:
            self.__apagar_vez_invalido(index)
        elif quantidade == 0:
            self.__escrever_vez_valido(index)

    def __apagar_vez_invalido(self,index):
        for letra in self.lista_letras:
            valido_vez = "".join(['valido_vez_',letra])
            vez = "".join(['vez_',letra])
            if  self.dataframe.loc[index,(valido_vez)] == False:
                self.dataframe.loc[index,(vez)] = False
                self.dataframe.loc[index,(valido_vez)] = True

    def __escrever_vez_valido(self,index):
        for letra in self.lista_letras:
            valido_vez = "".join(['valido_vez_',letra])
            vez = "".join(['vez_',letra])
            if  self.dataframe.loc[index,(valido_vez)] == False:
                self.dataframe.loc[index,(vez)] = True
                self.dataframe.loc[index,(valido_vez)] = True

            
    def __quantidade_de_vez(self,index):
        contador = 0
        for idx,letra in enumerate(self.lista_letras):
            vez_str = "".join(['vez_',letra])
            vez = self.dataframe.loc[index,(vez_str)]
            if vez == True:
                contador += 1
        return contador
