import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_combo(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        for letra in lista_letras:
            combo_1 = "".join(['combo_',letra,'_1'])
            combo_2 = "".join(['combo_',letra,'_2'])
            self.dataframe[combo_1] = np.nan
            self.dataframe[combo_2] = np.nan

    def validar(self,index):
        self.dataframe.loc[index,('valido_combo')] = False
