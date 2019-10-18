import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Analizar_nome(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe):
        self.dataframe = dataframe
        self.dataframe['nome_acao'] = np.nan
        self.dataframe['nome_bet'] = np.nan
        self.dataframe['nome_jogada'] = np.nan
        self.dataframe['nome_vilao'] = np.nan
        self.dataframe['nome_utima_bet'] = np.nan
        
    def analizar(self,index):
        self.__nome_acao(index)
        self.__nome_bet(index)
        self.__nome_jogada(index)
        self.__nome_vilao(index)
        self.__nome_ultima_bet(index)
        
    def __nome_acao(self,index):
        self.dataframe.loc[index,('nome_acao')] = 'null'
        letra = self.dataframe.loc[index,('ultimo_jogador_letra')]
        if letra != 'null':
            size_bet_vilao = self.dataframe.loc[index,('size_bet_vilao')]
            hole_cards_str = "".join(['hole_cards_',letra])
            hole_cards = self.dataframe.loc[index,(hole_cards_str)]
            if size_bet_vilao == 0 and hole_cards == True:
                self.dataframe.loc[index,('nome_acao')] = 'FOLD'
            elif size_bet_vilao == 0 and hole_cards == False:
                self.dataframe.loc[index,('nome_acao')] = 'CHECK'
            elif size_bet_vilao == 1:
                self.dataframe.loc[index,('nome_acao')] = 'CALL'
            elif size_bet_vilao > 1:
                self.dataframe.loc[index,('nome_acao')] = 'RAISE'
            

    def __nome_bet(self,index):
        self.dataframe.loc[index,('nome_bet')] = 'null'
        nome_acao = self.dataframe.loc[index,('nome_acao')]
        if nome_acao != 'null':
            quantidade_de_reise = self.__quantidade_de_reise(index)

            if quantidade_de_reise == 1 and nome_acao == 'RAISE':
                self.dataframe.loc[index,('nome_bet')] = 'OR'
            elif quantidade_de_reise == 2 and nome_acao == 'RAISE':
                self.dataframe.loc[index,('nome_bet')] = '3BET'
            elif quantidade_de_reise == 3 and nome_acao == 'RAISE':
                self.dataframe.loc[index,('nome_bet')] = '4BET'
            elif quantidade_de_reise == 4 and nome_acao == 'RAISE':
                self.dataframe.loc[index,('nome_bet')] = '5BET'
        

    def __nome_jogada(self,index):
        self.dataframe.loc[index,('nome_jogada')] = 'null'
        nome_acao = self.dataframe.loc[index,('nome_acao')]
        if nome_acao != 'null':
            size_bet_fichas = self.dataframe.loc[index,('size_bet_fichas')]
            if size_bet_fichas == 1:
                self.dataframe.loc[index,('nome_jogada')] = 'ALL IN'

    def __nome_ultima_bet(self,index):
        index_ultima_bet = self.__index_da_ultima_bet(index)
        bet = self.dataframe.loc[index_ultima_bet,('nome_bet')]
        quantidade_de_reise = self.__quantidade_de_reise(index)
        if quantidade_de_reise == 0:
            bet = 'BB'
        self.dataframe.loc[index,('nome_utima_bet')] = bet

    def __nome_vilao(self,index):
        index_ultima_bet = self.__index_da_ultima_bet(index)
        vilao = self.dataframe.loc[index_ultima_bet,('ultimo_jogador_posicao')]
        quantidade_de_reise = self.__quantidade_de_reise(index)
        if quantidade_de_reise == 0:
            vilao = ''
        self.dataframe.loc[index,('nome_vilao')] = vilao

    def __index_da_ultima_bet(self,index):
        index_ = index
        while True:
            if self.tem_mais_de_um(index_):
                if self.dataframe.loc[index_,('nome_bet')] != 'null':
                    return index_
            else:
                return index_
            index_ = self.index_anterior_da_mesma_tela(index_)

    def __quantidade_de_reise(self,index):
        nome_acao = 'RAISE'
        tela = self.dataframe.loc[index, ('tela')]
        mao = self.dataframe.loc[index,('mao')]
        bord_etapa = self.dataframe.loc[index,('bord_etapa')]
        quantidade_de_reise = len(self.dataframe[(self.dataframe['tela'] == tela) &
                                                 (self.dataframe['mao'] == mao) &
                                                 (self.dataframe['bord_etapa'] == bord_etapa) &
                                                 (self.dataframe['nome_acao'] == nome_acao)])
        return quantidade_de_reise
