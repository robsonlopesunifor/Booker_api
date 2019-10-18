import numpy as np
import pandas as pd

class Reparar_hole_cards:

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.coluna_hole_cards = []
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['nada'] = np.nan

    def reparar(self,index):
        for letra in self.lista_letras:
            hole_cards_str = "".join(['hole_cards_',letra])
            combo_str = "".join(['combo_',letra,'_1'])
            hole_cards = self.dataframe.loc[index,(hole_cards_str)]
            combo = self.dataframe.loc[index,(combo_str)]
            if hole_cards == True and combo != '':
                self.dataframe.loc[index,(hole_cards_str)] = False
