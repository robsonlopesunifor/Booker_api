import unittest
import copy
import numpy as np
import pandas as pd

class Analizar_metodos:

    def __init__(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        
    def ordenar_lista_pela_letra(self,letra_):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(self.lista_letras):
            rabo = lista_letras.pop(0)
            if letra_ == letra:
                break
            lista_letras.append(rabo)
        return lista_letras

    def ordenar_lista_pelo_diler(self,index):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(self.lista_letras):
            diler = "".join(['diler_',letra])
            rabo = lista_letras.pop(0)
            lista_letras.append(rabo)
            if self.dataframe.loc[index,(diler)] == True:
                break
        return lista_letras

    def mesma_etapa(self,index):
        bord_etapa_atual = self.dataframe.loc[index,('bord_etapa')]
        bord_etapa_anterior = self.dataframe.loc[index - 1,('bord_etapa')]
        if bord_etapa_atual == bord_etapa_anterior:
            return True
        else:
            return False

    def tem_mais_de_um(self,index):
        tamanho = len(self.dataframe[self.dataframe['mao'] == self.dataframe.loc[index,('mao')]])
        if tamanho > 1:
            return True
        else:
            return False


class Analizar_metodos_test(unittest.TestCase):

    def test_tem_mais_de_um(self):
        dataframe = pd.DataFrame()
        dataframe['nada'] = np.nan
        analizar_metodos = Analizar_metodos(dataframe,['A','B','C','D','E','F'])
        
        self.incrementar_dataframe(dataframe,0)
        assert analizar_metodos.tem_mais_de_um(0) == False
        self.incrementar_dataframe(dataframe,1)
        assert analizar_metodos.tem_mais_de_um(1) == True
        self.incrementar_dataframe(dataframe,2)
        assert analizar_metodos.tem_mais_de_um(2) == True

    def test_mesma_etapa(self):
        dataframe = pd.DataFrame()
        dataframe['nada'] = np.nan
        analizar_metodos = Analizar_metodos(dataframe,['A','B','C','D','E','F'])

        self.incrementar_dataframe(dataframe,0)
        self.incrementar_dataframe(dataframe,1)
        assert analizar_metodos.mesma_etapa(1) == True
        self.incrementar_dataframe(dataframe,2)
        assert analizar_metodos.mesma_etapa(2) == False

    def test_ordenar_lista_pelo_diler(self):
        dataframe = pd.DataFrame()
        dataframe['nada'] = np.nan
        analizar_metodos = Analizar_metodos(dataframe,['A','B','C','D','E','F'])

        self.incrementar_dataframe(dataframe,0)
        assert analizar_metodos.ordenar_lista_pelo_diler(0) == ['B','C','D','E','F','A']
        self.incrementar_dataframe(dataframe,1)
        assert analizar_metodos.ordenar_lista_pelo_diler(1) == ['C','D','E','F','A','B']
        
    def test_ordenar_lista_pela_letra(self):
        dataframe = pd.DataFrame()
        dataframe['nada'] = np.nan
        analizar_metodos = Analizar_metodos(dataframe,['A','B','C','D','E','F'])

        assert analizar_metodos.ordenar_lista_pela_letra('B') == ['C','D','E','F','A']
        assert analizar_metodos.ordenar_lista_pela_letra('C') == ['D','E','F','A','B']


    def incrementar_dataframe(self,dataframe,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'bord_etapa':'PRE_FLOP','linha':'normal','mao':1,
                        'diler_A':True,'diler_B':False,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':False,'vez_B':False,'vez_C':False,'vez_D':True,'vez_E':False,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        elif novo_ficheiro == 1:
            ficheiro = {'bord_etapa':'PRE_FLOP','linha':'normal','mao':1,
                        'diler_A':False,'diler_B':True,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':False,'vez_B':False,'vez_C':False,'vez_D':False,'vez_E':True,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        elif novo_ficheiro == 2:
            ficheiro = {'bord_etapa':'FLOP','linha':'normal','mao':1,
                        'diler_A':True,'diler_B':False,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':True,'vez_B':False,'vez_C':False,'vez_D':False,'vez_E':False,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        elif novo_ficheiro == 3:
            ficheiro = {'bord_etapa':'TURN','linha':'normal','mao':1,
                        'diler_A':True,'diler_B':False,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':False,'vez_B':True,'vez_C':False,'vez_D':False,'vez_E':False,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        elif novo_ficheiro == 4:
            ficheiro = {'bord_etapa':'RIVER','linha':'normal','mao':1,
                        'diler_A':True,'diler_B':False,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':False,'vez_B':False,'vez_C':False,'vez_D':False,'vez_E':False,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        elif novo_ficheiro == 5:
            ficheiro = {'bord_etapa':'RIVER','linha':'normal','mao':1,
                        'diler_A':True,'diler_B':False,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':False,'vez_B':False,'vez_C':False,'vez_D':False,'vez_E':False,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        elif novo_ficheiro == 6:
            ficheiro = {'bord_etapa':'RIVER','linha':'normal','mao':1,
                        'diler_A':True,'diler_B':False,'diler_C':False,'diler_D':False,'diler_E':False,'diler_F':False,
                        'vez_A':False,'vez_B':False,'vez_C':False,'vez_D':False,'vez_E':False,'vez_F':False,
                        'hole_cards_A':False,'hole_cards_B':False,'hole_cards_C':False,'hole_cards_D':False,'hole_cards_E':False,'hole_cards_F':False}
        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_ultimo_jogador')
    unittest.main()
