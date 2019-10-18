import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar

class Regra_aposta(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras

        self.dataframe['mao'] = np.nan
        for letra in self.lista_letras:
            valido_aposta = "".join(['valido_aposta_',letra])
            valido_fichas = "".join(['valido_fichas_',letra])
            aposta = "".join(['aposta_',letra])
            fichas = "".join(['fichas_',letra])
            self.dataframe[valido_aposta] = np.nan
            self.dataframe[valido_fichas] = np.nan
            self.dataframe[aposta] = np.nan
            self.dataframe[fichas] = np.nan
            

    def validar(self,index):        
        for letra in self.lista_letras:
            aposta = "".join(['aposta_',letra])
            fichas = "".join(['fichas_',letra])
            valido_aposta = "".join(['valido_aposta_',letra])
            valido_fichas = "".join(['valido_fichas_',letra])
                
            if self.tem_mais_de_um(index):
                if self.__e_mesma_etapa(index):
                    valor = self.__diferenca_das_fichas_mais_aposta_anterior_e_igual_a_aposta_atual(index,aposta,fichas)
                else:
                    valor = True
            else:
                valor = True
                    
            self.dataframe.loc[index,(valido_aposta)] = valor
            self.dataframe.loc[index,(valido_fichas)] = valor

    def __diferenca_das_fichas_mais_aposta_anterior_e_igual_a_aposta_atual(self,index,aposta,fichas):
        index_anterior = self.index_anterior_da_mesma_tela(index)
        aposta_atual = self.dataframe.loc[index,(aposta)]
        aposta_anterior = self.dataframe.loc[index_anterior,(aposta)]
        fichas_atual = self.dataframe.loc[index,(fichas)]
        fichas_anterior = self.dataframe.loc[index_anterior,(fichas)]
        if abs(round((fichas_anterior - fichas_atual) - (aposta_atual - aposta_anterior),2)) == 0.0:
            return True
        else:
            return False

    def __e_mesma_etapa(self,index):
        index_anterior = self.index_anterior_da_mesma_tela(index)
        flop_1_anterio = self.dataframe.loc[index_anterior,('bord_FLOP_1')]
        flop_2_anterio = self.dataframe.loc[index_anterior,('bord_FLOP_2')]
        flop_3_anterio = self.dataframe.loc[index_anterior,('bord_FLOP_3')]
        turn_anterio   = self.dataframe.loc[index_anterior,('bord_TURN')]
        river_anterio  = self.dataframe.loc[index_anterior,('bord_RIVER')]
        bord_anterior = "".join([flop_1_anterio,flop_2_anterio,flop_3_anterio,turn_anterio,river_anterio])

        flop_1 = self.dataframe.loc[index,('bord_FLOP_1')]
        flop_2 = self.dataframe.loc[index,('bord_FLOP_2')]
        flop_3 = self.dataframe.loc[index,('bord_FLOP_3')]
        turn   = self.dataframe.loc[index,('bord_TURN')]
        river  = self.dataframe.loc[index,('bord_RIVER')]
        bord = "".join([flop_1,flop_2,flop_3,turn,river])

        if bord_anterior == bord:
            return True
        else:
            return False

        
