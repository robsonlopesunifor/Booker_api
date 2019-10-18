import numpy as np
import pandas as pd

class Reparar_vencedor:

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['vencedor'] = np.nan

    def reparar(self,index):
        self.__repara_utima_linha_valida(index)

    def __repara_utima_linha_valida(self,index):
        letra = self.__achar_vencedor(index)
        if letra != 'null':
            self.dataframe['vencedor'] = letra


    #TODO: acho que seria interesante comparar com o anterior. Se o atual for maior que o anterior e pq ele ganhou.
    def __achar_vencedor(self,index):
        for letra in self.lista_letras:
            aposta = "".join(['aposta_',letra])
            aposta_atual = self.dataframe.loc[index,(aposta)]
            if aposta_atual < 0:
                self.dataframe.loc[index,(aposta)] = aposta_atual*(-1)
                return letra
        return 'null'
