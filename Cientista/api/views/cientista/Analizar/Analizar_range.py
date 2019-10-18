from poker import Strategy, Range
from poker.constants import Position
from poker.strategy import _Situation
import unittest
import copy
import numpy as np
import pandas as pd

class Analizar_range:

    def __init__(self):
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe):
        self.dataframe = dataframe
        self.dataframe['nome_acao'] = np.nan
        

class Analizar_range_test(unittest.TestCase):

    def test_analizar(self):
        analizar_range = Analizar_range()
        dataframe = pd.DataFrame()
        analizar_range.iniciar(dataframe)

        self.incrementar_dataframe(dataframe,0)
        analizar_range.analizar(0)
        assert analizar_range.dataframe.loc[0,('nome_acao')] == 'FOLD'        

    def incrementar_dataframe(self,dataframe,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao':1,'bord_etapa':'FLOP','hole_cards_A':True}
        elif novo_ficheiro == 1:
            ficheiro = {'mao':1,'bord_etapa':'FLOP','hole_cards_A':False}
        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_ultimo_jogador')
    unittest.main()

