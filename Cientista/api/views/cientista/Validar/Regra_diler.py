import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_diler(Auxiliar):

    def __init__(self,):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.coluna_diler = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.dataframe['valido_diler'] = np.nan
        for letra in lista_letras:
            diler = "".join(['diler_',letra])
            self.coluna_diler.append(diler)
            self.dataframe[diler] = np.nan
            
    def validar(self,index):
        contador = 0
        valor = False
        
        for colunas in self.coluna_diler:
            if(self.dataframe.loc[index,(colunas)] == True):
                contador += 1
        if contador == 1:
            valor = True
        self.dataframe.loc[index,('valido_diler')] = valor

