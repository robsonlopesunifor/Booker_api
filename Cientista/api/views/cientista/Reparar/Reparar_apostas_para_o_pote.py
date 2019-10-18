import unittest
import numpy as np
import pandas as pd

class Reparar_apostas_para_o_pote:

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = np.nan

    def reparar(self,index):
        self.__definir_como_linha_nativa(index)
        self.__zerar_as_apostas_se_pote_for_igual_pote_rodada(index)

    def __definir_como_linha_nativa(self,index):
        self.dataframe.loc[index,('linha')] = 'nativa'

    def __zerar_as_apostas_se_pote_for_igual_pote_rodada(self,index):
        pote_rodada = self.dataframe.loc[index,('pote_rodada')]
        pote = self.dataframe.loc[index,('pote')]
        if pote_rodada == pote:
            self.dataframe.loc[index + 1] = self.dataframe.loc[index]
            self.dataframe.loc[index + 1,('linha')] = 'nova'
            self.dataframe.loc[index,('pote_rodada')] = self.dataframe.loc[index - 1,('pote_rodada')]
            for letra in self.lista_letras:
                aposta = "".join(['aposta_',letra])
                self.dataframe.loc[index + 1,(aposta)] = 0


class Reparar_apostas_para_o_pote_test(unittest.TestCase):

    def test_repara(self):
        print('------------ validar -----------------')
        reparar_apostas_para_o_pote = Reparar_apostas_para_o_pote()
        dataframe = pd.DataFrame()
        reparar_apostas_para_o_pote.iniciar(dataframe,['A','B','C','D','E','F'])
        index = 0
        for x in range(0,4):
            dataframe.loc[index] = False
            novo_ficheiro = self.gerador_de_ficheiros(x)
            for chave in novo_ficheiro:
                dataframe.loc[index,(chave)] = novo_ficheiro[chave]
            reparar_apostas_para_o_pote.reparar(index)
            index = len(dataframe)
        print(reparar_apostas_para_o_pote.dataframe)
        

    def gerador_de_ficheiros(self,novo_ficheiro):
        if novo_ficheiro == 0:
            ficheiro = {'pote':2.23,'pote_rodada':1.00,'valido_pote_rodada':True,'mao':1,
                        'aposta_A':1,'aposta_B':1,'aposta_C':1,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        elif novo_ficheiro == 1:
            ficheiro = {'pote':2.23,'pote_rodada':2.23,'valido_pote_rodada':True,'mao':1,
                        'aposta_A':1.20,'aposta_B':1,'aposta_C':1,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        elif novo_ficheiro == 2:
            ficheiro = {'pote':5.83,'pote_rodada':5.83,'valido_pote_rodada':False,'mao':1,
                        'aposta_A':1.20,'aposta_B':1.20,'aposta_C':1.20,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        elif novo_ficheiro == 3:
            ficheiro = {'pote':5.83,'pote_rodada':5.83,'valido_pote_rodada':True,'mao':1,
                        'aposta_A':1,'aposta_B':1,'aposta_C':1,'aposta_D':1,'aposta_E':1,'aposta_F':1}
        return ficheiro



if __name__ == "__main__":
    print('Teste da classe Regra pote rodada')
    unittest.main()
