import unittest
import numpy as np
import pandas as pd

class Regra_descartar_primeira_linha_com_jogadores_inativos:

    def __init__(self):
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = np.nan

    def validar(self,index):
        valor = 'normal'
        if self.__primeira_linha_com_jogadores_inativos(index):
            valor = 'descartavel'
        self.dataframe.loc[index,('linha')] = valor

    def __primeira_linha_com_jogadores_inativos(self,index):
        if self.__tem_mais_de_um(index) == False:
            valor = self.__linha_de_hole_cards_inativos(index)
        else:
            valor = False
        return valor

    def __linha_de_hole_cards_inativos(self,index):
        valor = True
        for letra in self.lista_letras:
            hole_cards = "".join(['hole_cards_',letra])
            if self.dataframe.loc[index,(hole_cards)] == False:
                valor = False
        return valor

    def __tem_mais_de_um(self,index):
        tamanho = len(self.dataframe[self.dataframe['mao'] == self.dataframe.loc[index,('mao')]])
        if tamanho > 1:
            return True
        else:
            return False

class Regra_descartar_primeira_linha_com_jogadores_inativos_test(unittest.TestCase):

    def test_validar(self):
        print '------------ validar -----------------'
        regra_descartar_primeira_linha_com_jogadores_inativos = Regra_descartar_primeira_linha_com_jogadores_inativos()
        dataframe = pd.DataFrame()
        regra_descartar_primeira_linha_com_jogadores_inativos.iniciar(dataframe,['A','B','C','D','E','F'])
        for x in range(0,6):
            dataframe.loc[x] = False
            novo_ficheiro = self.gerador_de_ficheiros(x)
            for chave in novo_ficheiro:
                dataframe.loc[x,(chave)] = novo_ficheiro[chave]
            regra_descartar_primeira_linha_com_jogadores_inativos.validar(x)
        print regra_descartar_primeira_linha_com_jogadores_inativos.dataframe

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'bord_etapa':'RIVER','mao':1,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}          
        elif novo_ficheiro == 1:
            ficheiro = {'bord_etapa':'RIVER','mao':1,'hole_cards_A':False,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}          
        elif novo_ficheiro == 2:
            ficheiro = {'bord_etapa':'RIVER','mao':1,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 3:
            ficheiro = {'bord_etapa':'RIVER','mao':2,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 4:
            ficheiro = {'bord_etapa':'RIVER','mao':2,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        elif novo_ficheiro == 5:
            ficheiro = {'bord_etapa':'RIVER','mao':2,'hole_cards_A':True,'hole_cards_B':True,'hole_cards_C':True,'hole_cards_E': True, 'hole_cards_D': True, 'hole_cards_F': True}
        return ficheiro

if __name__ == "__main__":
    print('Teste da classe Regra_descartar_linha_com_jogadores_inativos')
    unittest.main()
