import copy
import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Reparar_aposta(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['nada'] = np.nan

    def reparar(self,index):
        self.__repete_apostas_dos_viloes_e_calcula_aposta_do_heroi(index)

    def __repete_apostas_dos_viloes_e_calcula_aposta_do_heroi(self,index):

        if self.tem_mais_de_um:
            for letra in self.lista_letras:
                valido_aposta = "".join(['valido_aposta_',letra])
                if self.dataframe.loc[index,(valido_aposta)] == False:
                    self.__calcula_quanto_deveria_ser_o_valor_da_aposta_do_heroi(index,letra)
                    #self.__repete_apostas_anteriores_dos_viloes_que_jogaram_antes(index)

    def __repete_apostas_anteriores_dos_viloes_que_jogaram_antes(self,index):
        for letra in self.__ordenar_lista_pelo_diler(index):
            valido_aposta = "".join(['valido_aposta_',letra])
            if self.dataframe.loc[index,(valido_aposta)] == False:
                break
            aposta = "".join(['aposta_',letra])
            index_anterior = self.index_anterior_da_mesma_tela(index)
            aposta_anterior = self.dataframe.loc[index_anterior,(aposta)]
            self.dataframe.loc[index,(aposta)] = aposta_anterior

    def __calcula_quanto_deveria_ser_o_valor_da_aposta_do_heroi(self,index,letra):
        aposta = "".join(['aposta_',letra])
        fichas = "".join(['fichas_',letra])
        index_anterior = self.index_anterior_da_mesma_tela(index)
        fichas_aual = self.dataframe.loc[index,(fichas)]
        fichas_anterior = self.dataframe.loc[index_anterior,(fichas)]
        aposta_anterior = self.dataframe.loc[index_anterior,(aposta)]
        aposta_esperada = (fichas_anterior - fichas_aual + aposta_anterior)
        if aposta_esperada < 0:
            aposta_esperada = aposta_esperada*(-1)
        self.dataframe.loc[index,(aposta)] = abs(round(aposta_esperada,2))

    def __ordenar_lista_pelo_diler(self,index):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(lista_letras):
            diler = "".join(['diler_',letra])
            rabo = self.lista_letras.pop(0)
            self.lista_letras.append(rabo)
            if self.dataframe.loc[index,(diler)] == True:
                break
        return lista_letras
        
