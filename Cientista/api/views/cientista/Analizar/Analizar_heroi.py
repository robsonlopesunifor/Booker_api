import unittest
import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar

class Analizar_heroi(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['heroi_letra'] = np.nan
        self.dataframe['heroi_posicao'] = np.nan
        self.dataframe['heroi_combo'] = np.nan

    def analizar(self,index):
        self.__diferenciar_herois_dos_viloes(index)

    def __diferenciar_herois_dos_viloes(self,index):
        self.dataframe.loc[index,('heroi_letra')] = ''
        self.dataframe.loc[index,('heroi_posicao')] = ''
        self.dataframe.loc[index,('heroi_combo')] = ''
        if self.__quantidade_de_combos(index) > 1:
            self.dataframe.loc[index,('heroi_letra')] = self.dataframe.loc[index-1,('heroi_letra')]
            self.dataframe.loc[index,('heroi_posicao')] = self.dataframe.loc[index-1,('heroi_posicao')]
            self.dataframe.loc[index,('heroi_combo')] = self.dataframe.loc[index-1,('heroi_combo')]
        else:
            letra = self.__pegar_heroi(index)
            self.dataframe.loc[index,('heroi_letra')] = letra
            self.dataframe.loc[index,('heroi_posicao')] = self.posicao_por_letra(letra,index)
            self.dataframe.loc[index,('heroi_combo')] = self.__pegar_combo(letra,index)

    def __quantidade_de_combos(self,index):
        quantidade_de_combos = 0
        for idx,letra in enumerate(self.lista_letras):
            combo_str = "".join(['combo_',letra,'_1'])
            if self.dataframe.loc[index,(combo_str)] != '':
                quantidade_de_combos += 1
        return quantidade_de_combos
            

    def __pegar_heroi(self,index):
        for idx,letra in enumerate(self.lista_letras):
            combo_str = "".join(['combo_',letra,'_1'])
            if self.dataframe.loc[index,(combo_str)] != '':
                return letra
        return ''

    def __pegar_combo(self,letra,index):
        combo = ''
        if(letra != ''):
            combo_str_1 = "".join(['combo_',letra,'_1'])
            combo_str_2 = "".join(['combo_',letra,'_2'])
            combo_1 = self.dataframe.loc[index,(combo_str_1)]
            combo_2 = self.dataframe.loc[index,(combo_str_2)]
            combo = "".join([combo_1,'-',combo_2])
        return combo
    

class Analizar_heroi_test(unittest.TestCase):

    def test_analizar(self):
        analizar_heroi = Analizar_heroi()
        dataframe = pd.DataFrame()
        analizar_heroi.iniciar(dataframe,['A','B','C','D','E','F'])

        self.incrementar_dataframe(dataframe,0)
        analizar_heroi.analizar(0)

        self.incrementar_dataframe(dataframe,1)
        analizar_heroi.analizar(1)

        self.incrementar_dataframe(dataframe,2)
        analizar_heroi.analizar(2)

        self.incrementar_dataframe(dataframe,3)
        analizar_heroi.analizar(3)

        self.incrementar_dataframe(dataframe,4)
        analizar_heroi.analizar(4)

        self.incrementar_dataframe(dataframe,5)
        analizar_heroi.analizar(5)

        self.incrementar_dataframe(dataframe,6)
        analizar_heroi.analizar(6)

        self.incrementar_dataframe(dataframe,7)
        analizar_heroi.analizar(7)
        
        print(analizar_heroi.dataframe)

    def incrementar_dataframe(self,dataframe,index):
        dataframe.loc[index] = False
        novo_ficheiro = self.gerador_de_ficheiros(index)
        for chave in novo_ficheiro:
            dataframe.loc[index,(chave)] = novo_ficheiro[chave]
        return dataframe

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'mao':1,'combo_A_1':'','combo_B_1':'9s9c','combo_C_1':'','combo_D_1':'','combo_E_1':'','combo_F_1':''}
        elif novo_ficheiro == 1:
            ficheiro = {'mao':1,'combo_A_1':'','combo_B_1':'9s9c','combo_C_1':'','combo_D_1':'','combo_E_1':'','combo_F_1':''}
        elif novo_ficheiro == 2:
            ficheiro = {'mao':1,'combo_A_1':'','combo_B_1':'9s9c','combo_C_1':'','combo_D_1':'','combo_E_1':'','combo_F_1':''}
        elif novo_ficheiro == 3:
            ficheiro = {'mao':1,'combo_A_1':'9s9c','combo_B_1':'9s9c','combo_C_1':'','combo_D_1':'9s9c','combo_E_1':'','combo_F':''}
        elif novo_ficheiro == 4:
            ficheiro = {'mao':2,'combo_A_1':'','combo_B_1':'','combo_C_1':'','combo_D_1':'','combo_E_1':'','combo_F_1':''}
        elif novo_ficheiro == 5:
            ficheiro = {'mao':2,'combo_A_1':'9s9c','combo_B_1':'','combo_C_1':'','combo_D_1':'','combo_E_1':'','combo_F_1':''}
        elif novo_ficheiro == 6:
            ficheiro = {'mao':2,'combo_A_1':'9s9c','combo_B_1':'','combo_C_1':'','combo_D_1':'','combo_E_1':'','combo_F_1':''}
        elif novo_ficheiro == 7:
            ficheiro = {'mao':2,'combo_A_1':'9s9c','combo_B_1':'','combo_C_1':'9s9c','combo_D_1':'','combo_E_1':'','combo_F_1':''}

        return ficheiro


if __name__ == "__main__":
    print('____Teste da classe Analista_heroi')
    unittest.main()
