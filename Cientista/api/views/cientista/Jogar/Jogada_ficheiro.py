import unittest
import numpy as np
import pandas as pd
from Jogada_preflop import Jogada_preflop

class Jogada_ficheiro(object):

    def __init__(self):
        csv = 'G:\Meu Drive\DA  Ferramentas\Projetos\Poker\Tarefa\Cenografo\Corretor\Corretor_ficheiro\Jogar\Jogada_preflop\exemplo2.csv'
        self.jogada_preflop = Jogada_preflop(csv)
        self.dataframe_jogar = pd.DataFrame()

    def iniciar(self,dataframe):
        self.dataframe_jogar = dataframe
        self.jogada_preflop.iniciar(self.dataframe_jogar)

    def jogar(self,index):
        self.jogada_preflop.jogar(index)

class Jogada_ficheiro_Test(unittest.TestCase):

    def test_iniciar(self):
        jogada_ficheiro = Jogada_ficheiro()
        dataframe = pd.DataFrame()
        jogada_ficheiro.iniciar(dataframe)

    def test_analizar(self):
        print '------------- adicionar_ficheiro_a_tabela ---------------'
        jogada_ficheiro = Jogada_ficheiro()
        dataframe = pd.read_csv('dataframe.csv',sep=';')
        jogada_ficheiro.iniciar(dataframe)
        for x in range(1,65):
            jogada_ficheiro.jogar(x)
        print(jogada_ficheiro.dataframe_jogar.loc[:,('nome_vilao','nome_utima_bet','jogada_valor')])

if __name__ == "__main__":
    print('____Teste da classe Jogada ficheiro')
    unittest.main()
