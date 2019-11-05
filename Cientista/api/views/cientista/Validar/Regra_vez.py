import copy
import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_vez(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras

        self.dataframe['mao'] = np.nan
        for letra in self.lista_letras:
            vez = "".join(['vez_',letra])
            valido_vez = "".join(['valido_vez_',letra])
            self.dataframe[vez] = np.nan
            self.dataframe[valido_vez] = True

    def validar(self,index):
        self.__vez_esta_correto_caso_contrario_compare_com_o_anterior(index)


    def __vez_esta_correto_caso_contrario_compare_com_o_anterior(self,index):
        quantidade = self.__quantidade_de_vez(index)
        index_anterior = self.index_anterior_da_mesma_tela(index)
        if quantidade == 1:
            self.__marcar_vez_correto(index)
        elif quantidade > 1:
            if self.tem_mais_de_um(index):
                letra = self.__retornar_vez_valido(index_anterior)
                proxima_letra = self.__proximo_vez_valido(index,letra)
                self.__marcar_vez_ecesso(index,proxima_letra)
            else:
                self.__marcar_vez_errado(index)
        elif quantidade == 0:
            if self.tem_mais_de_um(index):
                letra = self.__retornar_vez_valido(index_anterior)
                proxima_letra = self.__proximo_vez_valido(index,letra)
                self.__marcar_vez_falta(index,proxima_letra)
            else:
                self.__marcar_vez_errado(index)

    def __marcar_vez_ecesso(self,index,letra_):
        self.__marcar_vez(index,letra_,False)

    def __marcar_vez_falta(self,index,letra_):
        self.__marcar_vez(index,letra_,True)

    def __marcar_vez(self,index,letra_,inverter = False):
        for idx,letra in enumerate(self.lista_letras):
            vez_str = "".join(['vez_',letra])
            valido_vez_str = "".join(['valido_vez_',letra])
            vez = self.dataframe.loc[index,(vez_str)]
            if letra_ != letra:
                self.dataframe.loc[index,(valido_vez_str)] = False if inverter == False else True
            else:
                self.dataframe.loc[index,(valido_vez_str)] = True if inverter == False else False
                
    def __marcar_vez_correto(self,index):
        for idx,letra in enumerate(self.lista_letras):
            valido_vez_str = "".join(['valido_vez_',letra])
            self.dataframe.loc[index,(valido_vez_str)] = True

    def __marcar_vez_errado(self,index):
        for idx,letra in enumerate(self.lista_letras):
            valido_vez_str = "".join(['valido_vez_',letra])
            self.dataframe.loc[index,(valido_vez_str)] = False

    def __proximo_vez_valido(self,index,letra):
        for idx,letra in enumerate(self.__ordenar_lista_pela_letra(letra)):
            hole_cards_str = "".join(['hole_cards_',letra])
            hole_cards = self.dataframe.loc[index,(hole_cards_str)]
            if hole_cards == False:
                return letra
        return 'null'

    def __retornar_vez_valido(self,index):
        for idx,letra in enumerate(self.lista_letras):
            valido_vez_str = "".join(['valido_vez_',letra])
            vez_str = "".join(['vez_',letra])
            valido_vez = self.dataframe.loc[index,(valido_vez_str)]
            vez = self.dataframe.loc[index,(vez_str)]
            if valido_vez == True and vez == True:
                return letra
        return 'null'

    def __quantidade_de_vez(self,index):
        contador = 0
        for idx,letra in enumerate(self.lista_letras):
            vez_str = "".join(['vez_',letra])
            vez = self.dataframe.loc[index,(vez_str)]
            if vez == True:
                contador += 1
        return contador

    def __ordenar_lista_pela_letra(self,letra_):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(self.lista_letras):
            rabo = lista_letras.pop(0)
            lista_letras.append(rabo)
            if letra_ == letra:
                break
        return lista_letras
