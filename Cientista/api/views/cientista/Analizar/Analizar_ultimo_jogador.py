import copy
import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar

class Analizar_ultimo_jogador(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []
        self.lista_posicao = ['SB','BB','UTG','MP','CO','BTN']

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['ultimo_jogador_posicao'] = np.nan
        self.dataframe['ultimo_jogador_letra'] = np.nan
        

    def analizar(self,index):
        self.__ultima_jogador_por_posicao(index)

    def __ultima_jogador_por_posicao(self,index):
        letra = self.__ultima_jogador(index)
        posicao = self.__retornar_posicao_pela_letra(index,letra)
        self.dataframe.loc[index,('ultimo_jogador_posicao')] = posicao
        self.dataframe.loc[index,('ultimo_jogador_letra')] = letra
    
    def __ultima_jogador(self,index):
        if self.tem_mais_de_um(index):
            if self.mesma_etapa(index):
                index_anterior = self.index_anterior_da_mesma_tela(index)
                return self.__retorna_letra_da_vez(index_anterior)
            else:
                return 'null'
        else:
            return self.__letra_do_jogador_ativo_a_esquerda_na_mesma_linha(index)

    def __retornar_posicao_pela_letra(self,index,letra_):
        for idx,letra in enumerate(self.ordenar_lista_pelo_diler(index)):
            if letra_ == letra:
                return self.lista_posicao[idx]
        return 'null'

    def __retorna_letra_da_vez(self,index):
        for idx,letra in enumerate(self.lista_letras):
            vez = "".join(['vez_',letra])
            if self.dataframe.loc[index,(vez)] == True:
                return letra
        return 'null'


    def __letra_do_jogador_ativo_a_esquerda_na_mesma_linha(self,index):
        letra = self.__retorna_letra_da_vez(index)
        for idx,letra in enumerate(self.__ordenar_lista_pela_letra_invertida(letra)):
             hole_cards = "".join(['hole_cards_',letra])
             if self.dataframe.loc[index,(hole_cards)] == False:
                 return letra
        return 'null'

    def __ordenar_lista_pela_letra_invertida(self,letra_):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(self.lista_letras):
            rabo = lista_letras.pop(0)
            if letra_ == letra:
                break
            lista_letras.append(rabo)
        return lista_letras[::-1]

