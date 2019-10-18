from __future__ import unicode_literals, absolute_import, division, print_function
import unittest
import numpy as np
import pandas as pd

class Estragia_csv:

    def __init__(self,estilo,valores,maximo):
        self.estilo = estilo
        self.valores = valores
        self.maaximo = maximo
        self.posicoes = ['UTG','MP','CO','BTN','BB','SB']
        self.dataframe = pd.DataFrame()
        self.dataframe['HEROI'] = np.nan
        self.dataframe['VILAO'] = np.nan

        self.dataframe['CALL_BB_VALOR'] = np.nan
        self.dataframe['CALL_BB_RANGE'] = np.nan
        self.dataframe['REISE_BB_VALOR'] = np.nan
        self.dataframe['REISE_BB_RANGE'] = np.nan

        self.dataframe['CALL_OR_VALOR'] = np.nan
        self.dataframe['CALL_OR_RANGE'] = np.nan
        self.dataframe['REISE_OR_VALOR'] = np.nan
        self.dataframe['REISE_OR_RANGE'] = np.nan

        self.dataframe['CALL_3BET_VALOR'] = np.nan
        self.dataframe['CALL_3BET_RANGE'] = np.nan
        self.dataframe['REISE_3BET_VALOR'] = np.nan
        self.dataframe['REISE_3BET_RANGE'] = np.nan
        
        self.dataframe['CALL_4BET_VALOR'] = np.nan
        self.dataframe['CALL_4BET_RANGE'] = np.nan
        self.dataframe['REISE_4BET_VALOR'] = np.nan
        self.dataframe['REISE_4BET_RANGE'] = np.nan
        
        self.dataframe['CALL_5BET_VALOR'] = np.nan
        self.dataframe['CALL_5BET_RANGE'] = np.nan
        self.dataframe['REISE_5BET_VALOR'] = np.nan
        self.dataframe['REISE_5BET_RANGE'] = np.nan
        

    def gerar(self):
        index = 0
        for posicao_heroi in self.posicoes:
            for posicao_vilao in self.posicoes:
                self.dataframe.loc[index,('HEROI')] = posicao_heroi
                self.dataframe.loc[index,('VILAO')] = posicao_vilao
            
                self.bet_BB(index,posicao_heroi,posicao_vilao)
                self.bet_OR(index,posicao_heroi,posicao_vilao)
                self.bet_3BET(index,posicao_heroi,posicao_vilao)
                self.bet_4BET(index,posicao_heroi,posicao_vilao)
                self.bet_5BET(index,posicao_heroi,posicao_vilao)
                index += 1

    def bet_BB(self,index,posicao_heroi,posicao_vilao):
        ordem_heroi = self.posicoes.index(posicao_heroi)
        ordem_vilao = self.posicoes.index(posicao_vilao)
        self.dataframe.loc[index,('CALL_BB_RANGE')] = ' '
        self.dataframe.loc[index,('REISE_BB_RANGE')] = ' '
        if ordem_vilao == ordem_heroi:
            self.dataframe.loc[index,('CALL_BB_VALOR')] = 1
            self.dataframe.loc[index,('REISE_BB_VALOR')] = 1
        else:
            self.dataframe.loc[index,('CALL_BB_VALOR')] = -1
            self.dataframe.loc[index,('REISE_BB_VALOR')] = -1

    def bet_OR(self,index,posicao_heroi,posicao_vilao):
        ordem_heroi = self.posicoes.index(posicao_heroi)
        ordem_vilao = self.posicoes.index(posicao_vilao)
        self.dataframe.loc[index,('CALL_OR_RANGE')] = ' '
        self.dataframe.loc[index,('REISE_OR_RANGE')] = ' '
        if ordem_vilao < ordem_heroi:
            self.dataframe.loc[index,('CALL_OR_VALOR')] = 1
            self.dataframe.loc[index,('REISE_OR_VALOR')] = 3
        else:
            self.dataframe.loc[index,('CALL_OR_VALOR')] = -1
            self.dataframe.loc[index,('REISE_OR_VALOR')] = -1

    def bet_3BET(self,index,posicao_heroi,posicao_vilao):
        ordem_heroi = self.posicoes.index(posicao_heroi)
        ordem_vilao = self.posicoes.index(posicao_vilao)
        self.dataframe.loc[index,('CALL_3BET_RANGE')] = ' '
        self.dataframe.loc[index,('REISE_3BET_RANGE')] = ' '
        if ordem_vilao < ordem_heroi:
            self.dataframe.loc[index,('CALL_3BET_VALOR')] = 0
            self.dataframe.loc[index,('REISE_3BET_VALOR')] = 0
        elif ordem_vilao > ordem_heroi:
            self.dataframe.loc[index,('CALL_3BET_VALOR')] = 1
            self.dataframe.loc[index,('REISE_3BET_VALOR')] = 3
        else:
            self.dataframe.loc[index,('CALL_3BET_VALOR')] = -1
            self.dataframe.loc[index,('REISE_3BET_VALOR')] = -1

    def bet_4BET(self,index,posicao_heroi,posicao_vilao):
        ordem_heroi = self.posicoes.index(posicao_heroi)
        ordem_vilao = self.posicoes.index(posicao_vilao)
        self.dataframe.loc[index,('CALL_4BET_RANGE')] = ' '
        self.dataframe.loc[index,('REISE_4BET_RANGE')] = ' '
        if ordem_vilao < ordem_heroi:
            self.dataframe.loc[index,('CALL_4BET_VALOR')] = 0
            self.dataframe.loc[index,('REISE_4BET_VALOR')] = 100
        elif ordem_vilao > ordem_heroi:
            self.dataframe.loc[index,('CALL_4BET_VALOR')] = 0
            self.dataframe.loc[index,('REISE_4BET_VALOR')] = 0
        else:
            self.dataframe.loc[index,('CALL_4BET_VALOR')] = -1
            self.dataframe.loc[index,('REISE_4BET_VALOR')] = -1

    def bet_5BET(self,index,posicao_heroi,posicao_vilao):
        ordem_heroi = self.posicoes.index(posicao_heroi)
        ordem_vilao = self.posicoes.index(posicao_vilao)
        self.dataframe.loc[index,('CALL_5BET_RANGE')] = ' '
        self.dataframe.loc[index,('REISE_5BET_RANGE')] = ' '
        if ordem_vilao < ordem_heroi:
            self.dataframe.loc[index,('CALL_5BET_VALOR')] = 0
            self.dataframe.loc[index,('REISE_5BET_VALOR')] = 0
        elif ordem_vilao > ordem_heroi:
            self.dataframe.loc[index,('CALL_5BET_VALOR')] = 0
            self.dataframe.loc[index,('REISE_5BET_VALOR')] = 100
        else:
            self.dataframe.loc[index,('CALL_5BET_VALOR')] = 0
            self.dataframe.loc[index,('REISE_5BET_VALOR')] = -1

    def salvar(self,file_name):
        self.dataframe.to_csv(file_name, sep=str(u';'), encoding='utf-8')
        

class Estragia_csv_test(unittest.TestCase):

    def test_heroi_vs_vilao(self):
        estrategia = Estragia_csv('case','1-2','6-max')
        estrategia.gerar()
        file_name = 'G:\Meu Drive\DA  Ferramentas\Projetos\Poker\Tarefa\Cenografo\Corretor\Corretor_ficheiro\Analizar\Estrategia\exemplo2.csv'
        estrategia.salvar(file_name)


if __name__ == "__main__":
    print('____Teste da classe Estragia_csv')
    unittest.main()
