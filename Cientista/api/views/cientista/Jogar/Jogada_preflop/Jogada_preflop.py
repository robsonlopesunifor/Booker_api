from __future__ import unicode_literals, absolute_import, division

from poker.hand import Range, Combo
import unittest
import numpy as np
import pandas as pd


class Jogada_preflop:

    def __init__(self,csv):
        self.dataframe = pd.DataFrame()
        self.combo = None
        self.heroi = None
        self.vilao = None
        self.bet = None
        self.numeros = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        self.df_da_estrategia = pd.read_csv(csv,sep=';')

    def iniciar(self,dataframe):
        self.dataframe = dataframe
        self.dataframe['jogada_movimento'] = np.nan
        self.dataframe['jogada_valor'] = np.nan
        self.dataframe['jogada_ragne'] = np.nan

    
    def jogar(self,index):
        self.combo = 'KsKc' #self.dataframe.loc[index,('combo_heroi')]
        self.heroi = 'UTG' #self.dataframe.loc[index,('nome_heroi')]
        self.vilao = self.dataframe.loc[index,('nome_vilao')]
        self.bet = self.dataframe.loc[index,('nome_utima_bet')]
        self.dataframe.loc[index,('jogada_valor')] = self.retornar_valor_da_jogada()

    def retornar_valor_da_jogada(self):
        if self.bet == 'BB':
            self.vilao = self.heroi
        call = self.__combo_esta_no_renge_de_call()
        reise = self.__combo_esta_no_renge_de_reise()
        linha = self.df_da_estrategia[(self.df_da_estrategia['HEROI'] == self.heroi) & (self.df_da_estrategia['VILAO'] == self.vilao)]
        
        if call:
            bet = "".join(['CALL_',self.bet,'_VALOR'])
            return linha[bet].values[0]
        elif reise:
            bet = "".join(['REISE_',self.bet,'_VALOR'])
            return linha[bet].values[0]
        return 0

    def __combo_esta_no_renge_de_call(self):
        range_de_call = self.__retornar_range_de_call()
        return Combo(self.combo) in Range(range_de_call)

    def __combo_esta_no_renge_de_reise(self):
        range_de_reise = self.__retornar_range_de_reise()
        return Combo(self.combo) in Range(range_de_reise)

    def __retornar_range_de_call(self):
        bet = "".join(['CALL_',self.bet,'_RANGE'])
        range_ = self.df_da_estrategia[(self.df_da_estrategia['HEROI'] == self.heroi) & (self.df_da_estrategia['VILAO'] == self.vilao)][bet].values[0]
        return self.__corrigir(range_)

    def __retornar_range_de_reise(self):
        bet = "".join(['REISE_',self.bet,'_RANGE'])
        range_ = self.df_da_estrategia[(self.df_da_estrategia['HEROI'] == self.heroi) & (self.df_da_estrategia['VILAO'] == self.vilao)][bet].values[0]
        return self.__corrigir(range_)

    def __corrigir(self,range_):
        range_ = self.__corrigir_uppercase(range_)
        range_ = self.__reorganizar_range(range_)
        return range_

    def __reorganizar_range(self,range_):
        hands = range_.split(' ')
        for idx,hand in enumerate(hands):
            if hands[idx].find('-') > 0:
                hands[idx] = self.__range_vertical_nao_par(hands[idx])
        return ' '.join(hands)

    def __range_vertical_nao_par(self,range_):
        pontas = range_.split('-')
        hand = []
        if pontas[0][0] != pontas[1][0] and pontas[0][0] != pontas[0][1]:
            hand.append(pontas[0])
            hand_0 = pontas[0][0]
            hand_1 = pontas[0][1]
            contador = 1
            while True:
                hand_0 = self.__proxima_numero(hand_0)
                hand_1 = self.__proxima_numero(hand_1)
                suted = pontas[0][2]
                hand.append("".join([hand_0,hand_1,suted]))
                if pontas[1] == hand[contador]:
                    break
                if hand[contador] == "".join(['AA',suted]):
                    return 'erro'
                contador += 1
        else:
            return range_
        return ' '.join(hand)

    def __proxima_numero(self,numero):
        if numero != 'A':
            for idx,num in enumerate(self.numeros):
                if self.numeros[idx] == numero:
                    return self.numeros[idx+1]
        return numero

    def __corrigir_uppercase(self,range_):
        range_ = range_.upper()
        range_ = range_.replace('S','s')
        range_ = range_.replace('O','o')
        return range_


class Jogada_preflop_test(unittest.TestCase):

    def heroi_vs_vilao(self):
        csv = 'G:\Meu Drive\DA  Ferramentas\Projetos\Poker\Tarefa\Cenografo\Corretor\Corretor_ficheiro\Jogar\exemplo2.csv'
        jogada_preflop = Jogada_preflop(csv)
        
        estrategia.definir_heroi_vilao_e_bet('UTG','UTG','BB')
        # 22+
        assert estrategia.jogada('2s2c') == 3.6
        assert estrategia.jogada('3s3c') == 3.6
        assert estrategia.jogada('4s4c') == 3.6
        assert estrategia.jogada('5s5c') == 3.6
        assert estrategia.jogada('6s6c') == 3.6
        assert estrategia.jogada('7s7c') == 3.6
        assert estrategia.jogada('8s8c') == 3.6
        assert estrategia.jogada('9s9c') == 3.6
        assert estrategia.jogada('TsTc') == 3.6
        assert estrategia.jogada('JsJc') == 3.6
        assert estrategia.jogada('QsQc') == 3.6
        assert estrategia.jogada('KsKc') == 3.6
        assert estrategia.jogada('AsAc') == 3.6
        # AJo+
        """
        assert estrategia.combo_esta_no_renge_de_reise('AsJc') == True
        assert estrategia.combo_esta_no_renge_de_reise('AsQs') == True
        assert estrategia.combo_esta_no_renge_de_reise('AsKc') == True
        assert estrategia.combo_esta_no_renge_de_reise('AsAc') == True
        # KQo
        assert estrategia.combo_esta_no_renge_de_reise('KsQc') == True
        # AKs-76s
        assert estrategia.combo_esta_no_renge_de_reise('7s6s') == True
        assert estrategia.combo_esta_no_renge_de_reise('8s7s') == True
        assert estrategia.combo_esta_no_renge_de_reise('9s8s') == True
        assert estrategia.combo_esta_no_renge_de_reise('Ts9s') == True
        assert estrategia.combo_esta_no_renge_de_reise('JsTs') == True
        assert estrategia.combo_esta_no_renge_de_reise('QsJs') == True
        assert estrategia.combo_esta_no_renge_de_reise('KsQs') == True
        assert estrategia.combo_esta_no_renge_de_reise('AsKs') == True
        # J9-AQ
        assert estrategia.combo_esta_no_renge_de_reise('Js9s') == True
        assert estrategia.combo_esta_no_renge_de_reise('QsTs') == True
        assert estrategia.combo_esta_no_renge_de_reise('KsJs') == True
        assert estrategia.combo_esta_no_renge_de_reise('AsQs') == True
        # AJ-KT
        assert estrategia.combo_esta_no_renge_de_reise('AsJs') == True
        assert estrategia.combo_esta_no_renge_de_reise('KsTs') == True
        # AT
        assert estrategia.combo_esta_no_renge_de_reise('AsTs') == True
        # A2s-A5s
        assert estrategia.combo_esta_no_renge_de_reise('As2s') == True
        assert estrategia.combo_esta_no_renge_de_reise('As3s') == True
        assert estrategia.combo_esta_no_renge_de_reise('As4s') == True
        assert estrategia.combo_esta_no_renge_de_reise('As5s') == True
        # erros
        assert estrategia.combo_esta_no_renge_de_reise('Ts4s') == False
        assert estrategia.combo_esta_no_renge_de_reise('7s3c') == False
        assert estrategia.combo_esta_no_renge_de_reise('Kc7s') == False
        assert estrategia.combo_esta_no_renge_de_reise('Qs5s') == False
        """
        estrategia.definir_heroi_vilao_e_bet('CO','UTG','OR')
        assert estrategia.jogada('9s9c') == 1

    def test_jogada_pandas(self):
        csv = 'G:\Meu Drive\DA  Ferramentas\Projetos\Poker\Tarefa\Cenografo\Corretor\Corretor_ficheiro\Jogar\Jogada_preflop\exemplo2.csv'
        jogada_preflop = Jogada_preflop(csv)
        dataframe = pd.DataFrame()
        jogada_preflop.iniciar(dataframe)

        self.incrementar_dataframe(dataframe,0)
        jogada_preflop.jogar(0)
        print(jogada_preflop.dataframe.loc[0,('jogada_valor')])
        
        self.incrementar_dataframe(dataframe,1)
        jogada_preflop.jogar(1)
        print(jogada_preflop.dataframe.loc[1,('jogada_valor')])
        
        self.incrementar_dataframe(dataframe,2)
        jogada_preflop.jogar(2)
        print(jogada_preflop.dataframe.loc[2,('jogada_valor')])
        
        self.incrementar_dataframe(dataframe,3)
        jogada_preflop.jogar(3)
        print(jogada_preflop.dataframe.loc[3,('jogada_valor')])

        self.incrementar_dataframe(dataframe,4)
        jogada_preflop.jogar(4)
        print(jogada_preflop.dataframe.loc[4,('jogada_valor')])
        

    def incrementar_dataframe(self,dataframe,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'combo_heroi':'KsKc','nome_heroi':'MP','nome_vilao':'UTG','nome_utima_bet':'OR'}
        elif novo_ficheiro == 1:
            ficheiro = {'combo_heroi':'KsKc','nome_heroi':'MP','nome_vilao':'CO','nome_utima_bet':'OR'}
        elif novo_ficheiro == 2:
            ficheiro = {'combo_heroi':'KsKc','nome_heroi':'MP','nome_vilao':'SB','nome_utima_bet':'3BET'}
        elif novo_ficheiro == 3:
            ficheiro = {'combo_heroi':'KsKc','nome_heroi':'MP','nome_vilao':'SB','nome_utima_bet':'3BET'}
        elif novo_ficheiro == 4:
            ficheiro = {'combo_heroi':'KsKc','nome_heroi':'UTG','nome_vilao':'CO','nome_utima_bet':'BB'}
        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Estragia_csv')
    unittest.main()
