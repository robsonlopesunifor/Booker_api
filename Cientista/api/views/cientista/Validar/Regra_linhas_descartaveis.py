import unittest
import numpy as np
import pandas as pd

class Regra_linhas_descartaveis:

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
        if self.__linha_de_hole_cards_inativos(index) and self.__tem_mais_de_um(index):
            if self.__hole_cards_anteriores_ativos_ou_difere_de_river(index) != True:
                valor = 'descartavel'
        self.dataframe.loc[index,('linha')] = valor

    def __primeira_linha_com_jogadores_inativos(self,index):
        if self.__tem_mais_de_um(index) == False:
            valor = self.__linha_de_hole_cards_inativos(index)
        else:
            valor = False
        return valor

    def __hole_cards_anteriores_ativos_ou_difere_de_river(self,index):
        if self.__linha_de_hole_cards_inativos(index - 1) != True or self.__diferente_de_river(index - 1):
            return True
        else:
            return False

    def __diferente_de_river(self,index):
        if self.dataframe.loc[index,('bord_etapa')] == 'RIVER':
            return False
        else:
            return True

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

class Regra_linhas_descartaveis_test(unittest.TestCase):

    def test_validar(self):
        print('------------ validar -----------------')
        regra_linhas_descartaveis = Regra_linhas_descartaveis()
        dataframe = pd.DataFrame()
        regra_linhas_descartaveis.iniciar(dataframe,['A','B','C','D','E','F'])
        for x in range(0,6):
            dataframe.loc[x] = False
            novo_ficheiro = self.gerador_de_ficheiros(x)
            for chave in novo_ficheiro:
                dataframe.loc[x,(chave)] = novo_ficheiro[chave]
            regra_linhas_descartaveis.validar(x)
        print(regra_linhas_descartaveis.dataframe)

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
    print('Teste da classe lisnhas descartavel')
    unittest.main()
