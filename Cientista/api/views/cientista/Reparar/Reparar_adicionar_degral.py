import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Reparar_adicionar_degral(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['nada'] = np.nan
        self.dataframe['linha'] = np.nan

    def reparar(self,index):
        self.lista_letras = self.ordenar_lista_pelo_diler(index)
        self.__criar_caso_precise_de_degral(index)

    def __criar_caso_precise_de_degral(self,index):
        letra = self.__era_para_ter_decral(index)
        if letra != 'null':
            self.dataframe.loc[index + 1] = self.dataframe.loc[index]
            self.__reorganizar_hord_card(index,letra)

    def __reorganizar_hord_card(self,index,letra_):
        for letra in self.lista_letras:
            hord_card = "".join(['hole_cards_',letra])
            vez = "".join(['vez_',letra])
            self.dataframe.loc[index,(vez)] = False
            if self.letra_a_esquerda(letra_) != letra:
                index_anterior = self.index_anterior_da_mesma_tela(index)
                hord_card_anterior = self.dataframe.loc[index_anterior,(hord_card)]
                if hord_card_anterior == False:
                    self.dataframe.loc[index,(hord_card)] = False
        vez = "".join(['vez_',letra_])
        self.dataframe.loc[index,(vez)] = True


    def __era_para_ter_decral(self,index):
        if self.tem_mais_de_um(index):
            if self.mesma_etapa(index) and self.todos_jogadores_inativos(index) == False:
                for idx,letra in enumerate(self.lista_letras):
                    hole_cards = "".join(['hole_cards_',letra])
                    index_anterior = self.index_anterior_da_mesma_tela(index)
                    if self.dataframe.loc[index,(hole_cards)] == True and self.dataframe.loc[index_anterior,(hole_cards)] == False:
                        letra_a_esquerda = self.letra_a_esquerda(letra)
                        hole_cards_a_esquerda = "".join(['hole_cards_',letra_a_esquerda])
                        if self.dataframe.loc[index,(hole_cards_a_esquerda)] == True:
                            if self.dataframe.loc[index_anterior,(hole_cards_a_esquerda)] == False:
                                return letra
        return 'null'


