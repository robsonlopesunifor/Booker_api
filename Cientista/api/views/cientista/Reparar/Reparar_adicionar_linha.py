import copy
import pandas as pd
from ..Auxiliar import Auxiliar


class Reparar_adicionar_linha(Auxiliar):

    def __init__(self):
        self.dataframe = pd.DataFrame()
        self.lista_letras = []

    def iniciar(self,dataframe,lista_letras):
        self.dataframe = dataframe
        self.lista_letras = lista_letras
        self.dataframe['linha'] = ''

    def reparar(self,index):
        self.lista_letras = self.__ordenar_lista_pelo_diler(index)
        if self.tem_mais_de_um(index) and self.__mesma_etapa(index) and self.__todos_jogadores_inativos(index) == False:
            self.__foldou_sem_mostra_vez(index)    


    def __foldou_sem_mostra_vez(self,index):
        letra = self.__nao_mostrou_a_vez_antes_do_fold(index)
        if letra != 'null':
            self.__criar_caso_jogador_anterior_esteja_ativo(index,letra)
            #self.__reorganizar_vez_e_hord_card(index,letra)

    def __nao_mostrou_a_vez_antes_do_fold(self,index):
        index_anterior = self.index_anterior_da_mesma_tela(index)
        for letra in self.lista_letras:
            hole_cards = "".join(['hole_cards_',letra])
            vez = "".join(['vez_',letra])
            hole_cards_atual = self.dataframe.loc[index,(hole_cards)]
            hole_cards_anterior = self.dataframe.loc[index_anterior,(hole_cards)]
            vez_aterior = self.dataframe.loc[index_anterior,(vez)]
            if hole_cards_atual == True and hole_cards_anterior == False and vez_aterior == False:
                return letra
        return 'null'

    def __criar_caso_jogador_anterior_esteja_ativo(self,index,letra):
        if self.__jogador_anterior_a_esquerda_esta_ativo(index,letra):
            self.dataframe.loc[index + 1] = self.dataframe.loc[index]
            self.__reorganizar_vez_e_hord_card(index,letra)
            self.__reorganizar_vez_e_hord_card(index+1,self.__letra_a_direita(letra))
            self.dataframe.loc[index + 1,('linha')] = 'nova'
        else:
            self.__reorganizar_vez_e_hord_card(index,letra)

    def __jogador_anterior_a_esquerda_esta_ativo(self,index,letra_):
        index_anterior = self.index_anterior_da_mesma_tela(index)
        letra_a_esuqerda = self.__letra_a_esquerda(letra_)
        hord_card = "".join(['hole_cards_',letra_a_esuqerda])
        vez = "".join(['vez_',letra_a_esuqerda])
        if self.dataframe.loc[index_anterior,(hord_card)] == False:
            if self.dataframe.loc[index_anterior,(vez)] == True:
                return True
        return False

    def __vez_no_topo_e_lateral_direita(self,index,letra_):
        self.__reorganizar_vez_e_hord_card(index,letra_)
        self.__reorganizar_vez_e_hord_card(index+1,self.__letra_a_direita(letra_))

    def __reorganizar_vez_e_hord_card(self,index,letra_):
        for letra in self.lista_letras:
            vez = "".join(['vez_',letra])
            if letra_ == letra:
                self.dataframe.loc[index,(vez)] = True
                self.__limpar_hord_card_posteriores_caso_for_primeira_vez(index,letra)
            else:
                self.dataframe.loc[index,(vez)] = False
                
    def __limpar_hord_card_posteriores_caso_for_primeira_vez(self,index,letra_):
        limpar = False
        if self.tem_mais_de_um(index):
            index_anterior = self.index_anterior_da_mesma_tela(index)
            for letra in self.lista_letras:
                hole_cards = "".join(['hole_cards_',letra])
                if letra_ == letra:
                    limpar = True
                if limpar == True and self.dataframe.loc[index_anterior,(hole_cards)] == False:
                    self.dataframe.loc[index,(hole_cards)] = False


    def __letra_a_esquerda(self,letra_):
        for idx,letra in enumerate(self.lista_letras):
            if letra == letra_:
                if idx == 0:
                    idx_ = (len(self.lista_letras) - 1)
                else:
                    idx_ = idx - 1
        return self.lista_letras[idx_]

    def __letra_a_direita(self,letra_):
        for idx,letra in enumerate(self.lista_letras):
            if letra == letra_:
                if idx == (len(self.lista_letras) - 1):
                    idx_ = 0
                else:
                    idx_ = idx + 1
        return self.lista_letras[idx_]

    def __ordenar_lista_pelo_diler(self,index):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(self.lista_letras):
            diler = "".join(['diler_',letra])
            rabo = lista_letras.pop(0)
            lista_letras.append(rabo)
            if self.dataframe.loc[index,(diler)] == True:
                break
        return lista_letras

    def __todos_jogadores_inativos(self,index):
        for idx,letra in enumerate(self.lista_letras):
            hole_cards = "".join(['hole_cards_',letra])
            if self.dataframe.loc[index,(hole_cards)] == False:
                return False
        return True

    def __mesma_etapa(self,index):
        index_anterior = self.index_anterior_da_mesma_tela(index)
        bord_etapa_atual = self.dataframe.loc[index,('bord_etapa')]
        bord_etapa_anterior = self.dataframe.loc[index_anterior,('bord_etapa')]
        if bord_etapa_atual == bord_etapa_anterior:
            return True
        else:
            return False

