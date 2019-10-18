import unittest
import numpy as np
import pandas as pd

class Regra_adicionar_linha:

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = np.nan

    def validar(self,index):
        if self.__vez_da_aposta_aterior_ao_fold(index)
        

    def __vez_da_aposta_aterior_ao_fold(self,index):
        for letra in self.lista_letras:
            hole_cards = "".join(['hole_cards_',letra])
            vez = "".join(['vez_',letra])
            hole_cards_atual = self.dataframe.loc[index,(hole_cards)]
            vez_aterior = self.dataframe.loc[index - 1,(vez)]
            if hole_cards_atual == True and vez_aterior == False:
                print letra, index
            

    def __tem_mais_de_um(self,index):
        tamanho = len(self.dataframe[self.dataframe['mao'] == self.dataframe.loc[index,('mao')]])
        if tamanho > 1:
            return True
        else:
            return False
            
            

    def apostas_zeradas_quando_pote_iqual_pote_rodada(self,index):
        pote_rodada = self.dataframe.loc[index,('pote_rodada')]
        pote = self.dataframe.loc[index,('pote')]
        if pote_rodada == pote:
            for letra in self.lista_letras:
                aposta = "".join(['aposta_',letra])
                if self.dataframe.loc[index,(aposta)] != 0.0:
                    return False
        return True


class Regra_apostas_para_o_pote_test(unittest.TestCase):

    def test_repara(self):
        print '------------ validar -----------------'
        regra_apostas_para_o_pote = Regra_apostas_para_o_pote()
        dataframe = pd.DataFrame()
        regra_apostas_para_o_pote.iniciar(dataframe,['A','B','C','D','E','F'])
        index = 0
        for x in range(0,4):
            dataframe.loc[index] = False
            novo_ficheiro = self.gerador_de_ficheiros(x)
            for chave in novo_ficheiro:
                dataframe.loc[index,(chave)] = novo_ficheiro[chave]
            regra_apostas_para_o_pote.validar(index)
            index = len(dataframe)
        print regra_apostas_para_o_pote.dataframe
        

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote':2.23,'pote_rodada':1.00,'valido_pote_rodada':True,'mao':1,
                        'aposta_A':1,'aposta_B':1,'aposta_C':1,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        elif novo_ficheiro == 1:
            ficheiro = {'pote':2.23,'pote_rodada':2.23,'valido_pote_rodada':True,'mao':1,
                        'aposta_A':0,'aposta_B':0,'aposta_C':0,'aposta_D':0,'aposta_E':0,'aposta_F':0}
        elif novo_ficheiro == 2:
            ficheiro = {'pote':5.83,'pote_rodada':3.00,'valido_pote_rodada':False,'mao':1,
                        'aposta_A':1.20,'aposta_B':1.20,'aposta_C':1.20,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        elif novo_ficheiro == 3:
            ficheiro = {'pote':5.83,'pote_rodada':5.83,'valido_pote_rodada':True,'mao':1,
                        'aposta_A':1,'aposta_B':1,'aposta_C':1,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra pote rodada')
    unittest.main()
