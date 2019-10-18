import numpy as np
import pandas as pd
from ..Auxiliar import Auxiliar


class Regra_hole_cards(Auxiliar):

    def __init__(self):
        Auxiliar.__init__(self)
        self.dataframe = pd.DataFrame()
        self.coluna_hole_cards = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.dataframe['valido_hole_cards'] = np.nan
        for letra in lista_letras:
            hole_cards = "".join(['hole_cards_',letra])
            self.coluna_hole_cards.append(hole_cards)
            self.dataframe[hole_cards] = np.nan

    def validar(self,index):
        self.dataframe.loc[index,('valido_hole_cards')] = False

