import numpy as np
import pandas as pd
from . import Validar
from . import Reparar
from . import Analizar
#from Jogar import Jogada_ficheiro

class Cientista(object):

    def __init__(self,lista_de_cartas=[],dataframe = pd.DataFrame()):
        self.validador = Validar.Validador()
        self.reparador = Reparar.Reparar()
        self.analista = Analizar.Analizar()
        #self.jogador = Jogada_ficheiro.Jogada()
        self.dataframe = dataframe
        self.dataframe['nada'] = np.nan
        self.index = 0
        self.lista_de_cartas = lista_de_cartas
        self.validador.iniciar(self.dataframe)
        self.reparador.iniciar(self.dataframe)
        self.analista.iniciar(self.dataframe)
        #self.jogador.iniciar(self.dataframe)

    def processar(self,carta):
        if carta['cientista_processado'] == False and carta['nova_carta'] == True:
            self.adicionar_corrigir(carta['cena'])


    def adicionar_corrigir(self,ficheiro):
        self.adicionar(ficheiro)
        self.corrigir(self.index)
        self.index += 1
        while True:
            if len(self.dataframe) == self.index:
                break
            else:
                self.corrigir(self.index)
                self.index += 1

    def corrigir(self,index):
        self.validador.validar(index)
        self.reparador.reparar(index)
        self.validador.validar(index)
        self.analista.analizar(index)
        #self.jogador.jogar(index)
                    
    def adicionar(self,ficheiro):
        ficheiro_alinhado = {}
        total_de_linhas = len(self.dataframe)
        self.dataframe.loc[total_de_linhas] = np.nan

        for chave in ficheiro:
            if len(ficheiro[chave]) == 1:
                ficheiro_alinhado.setdefault(chave,ficheiro[chave]['A'])
            else:
                for sub_chave in ficheiro[chave]:
                    ficheiro_alinhado.setdefault("".join([chave,'_',sub_chave]),ficheiro[chave][sub_chave])
        for chave in ficheiro_alinhado:
            self.dataframe.loc[total_de_linhas,(chave)] = ficheiro_alinhado[chave]
            
