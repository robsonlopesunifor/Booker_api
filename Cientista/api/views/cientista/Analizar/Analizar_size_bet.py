import copy
import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Analizar_size_bet(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []
        self.lista_posicao = ['SB','BB','UTG','UTG+1','CO','BTN']
        self.blinds = 0

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['size_bet_valor'] = np.nan
        self.dataframe['size_bet_blind'] = np.nan
        self.dataframe['size_bet_pote'] = np.nan
        self.dataframe['size_bet_vilao'] = np.nan
        self.dataframe['size_bet_fichas'] = np.nan
        

    def analizar(self,index):
        self.__pegar_blinds(index)
        if self.dataframe.loc[index,('ultimo_jogador_letra')] != 'null':
            self.__size_bet_valor(index)
            self.__size_bet_blind(index)
            self.__size_bet_pote(index)
            self.__size_bet_vilao(index)
            self.__size_bet_fichas(index)
        else:
            self.__size_bet_null(index)
            
    def __size_bet_valor(self,index):
        letra = self.dataframe.loc[index,('ultimo_jogador_letra')]
        linha = self.dataframe.loc[index,('linha')]
        aposta_str = "".join(['aposta_',letra])
        hole_cards_str = "".join(['hole_cards_',letra])
        aposta = self.dataframe.loc[index,(aposta_str)]
        hole_cards = self.dataframe.loc[index,(hole_cards_str)]
        if hole_cards == False and linha != 'descartavel':
            self.dataframe.loc[index,('size_bet_valor')] = round(aposta,2)
        else:
            self.dataframe.loc[index,('size_bet_valor')] = 0

    def __size_bet_blind(self,index):
        valor = self.dataframe.loc[index,('size_bet_valor')]
        self.dataframe.loc[index,('size_bet_blind')] = round((valor/(self.blinds + 0.0001)),2)

    def __size_bet_pote(self,index):
        if self.tem_mais_de_um(index):
            letra = self.dataframe.loc[index,('ultimo_jogador_letra')]
            index_anterior = self.index_anterior_da_mesma_tela(index)
            pote_anterior = self.dataframe.loc[index_anterior,('pote')]
            aposta_str = "".join(['aposta_',letra])
            aposta_atual = self.dataframe.loc[index,(aposta_str)]
            aposta_anterior = self.dataframe.loc[index_anterior,(aposta_str)]
            self.dataframe.loc[index,('size_bet_pote')] = round(((aposta_atual - aposta_anterior)/(pote_anterior+0.00001)),2)

    def __size_bet_vilao(self,index):
        if self.tem_mais_de_um(index):
            valor_anterior = self.__ultimo_valor(index)
            valor_atual = self.dataframe.loc[index,('size_bet_valor')]
            if self.dataframe.loc[index,('linha')] != 'descartavel':
                self.dataframe.loc[index,('size_bet_vilao')] = round((valor_atual/(valor_anterior+0.00001)),2)
            else:
                self.dataframe.loc[index,('size_bet_vilao')] = -1

    def __size_bet_fichas(self,index):
        if self.tem_mais_de_um(index):
            letra = self.dataframe.loc[index,('ultimo_jogador_letra')]
            index_anterior = self.index_anterior_da_mesma_tela(index)
            fichas_str = "".join(['fichas_',letra])
            aposta_str = "".join(['aposta_',letra])
            fichas_anterior = self.dataframe.loc[index_anterior,(fichas_str)]
            aposta_atual    = self.dataframe.loc[index,(aposta_str)]
            aposta_anterior = self.dataframe.loc[index_anterior,(aposta_str)]
            self.dataframe.loc[index,('size_bet_fichas')] = round(((aposta_atual - aposta_anterior)/(fichas_anterior+0.00001)),2)

    def __size_bet_null(self,index):
        self.dataframe.loc[index,('size_bet_valor')] = 0
        self.dataframe.loc[index,('size_bet_blind')] = 0
        self.dataframe.loc[index,('size_bet_pote')] = 0
        self.dataframe.loc[index,('size_bet_vilao')] = 0
        self.dataframe.loc[index,('size_bet_fichas')] = 0

    def __pegar_blinds(self,index):
        if self.tem_mais_de_um(index) == False or self.blinds == 0:
            lista_ordenada = self.ordenar_lista_pelo_diler(index)
            letra = lista_ordenada[1]
            aposta_str = "".join(['aposta_',letra])
            aposta = self.dataframe.loc[index,(aposta_str)]
            self.blinds = aposta


    def __ultimo_valor(self,index):
        index_ = index
        while True:
            index_ = self.index_anterior_da_mesma_tela(index_)
            if index_ >= 0:
                valor = self.dataframe.loc[index_,('size_bet_valor')]
                if valor > 0:
                    return valor
                if self.mesma_etapa(index_) == False:
                    return 0.000001

