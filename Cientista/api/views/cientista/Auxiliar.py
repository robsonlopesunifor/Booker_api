import copy


class Auxiliar:

    def __init__(self):
        self.dataframe = None
        self.lista_letras = None

    def letra_a_esquerda(self,letra_):
        for idx,letra in enumerate(self.lista_letras):
            if letra == letra_:
                if idx == 0:
                    idx_ = (len(self.lista_letras) - 1)
                else:
                    idx_ = idx - 1
        return self.lista_letras[idx_]

    def letra_a_direita(self,letra_):
        for idx,letra in enumerate(self.lista_letras):
            if letra == letra_:
                if idx == (len(self.lista_letras) - 1):
                    idx_ = 0
                else:
                    idx_ = idx + 1
        return self.lista_letras[idx_]

    def ordenar_lista_pelo_diler(self,index):
        lista_letras = copy.deepcopy(self.lista_letras)
        for idx,letra in enumerate(self.lista_letras):
            diler = "".join(['diler_',letra])
            rabo = lista_letras.pop(0)
            lista_letras.append(rabo)
            if self.dataframe.loc[index,(diler)] == True:
                break
        return lista_letras

    def todos_jogadores_inativos(self,index):
        for idx,letra in enumerate(self.lista_letras):
            hole_cards = "".join(['hole_cards_',letra])
            if self.dataframe.loc[index,(hole_cards)] == False:
                return False
        return True

    def mesma_etapa(self,index):
        if self.tem_mais_de_um(index):
            index_anterior = self.index_anterior_da_mesma_tela(index)
            bord_etapa_atual = self.dataframe.loc[index,('bord_etapa')]
            bord_etapa_anterior = self.dataframe.loc[index_anterior,('bord_etapa')]
            if bord_etapa_atual == bord_etapa_anterior:
                return True
            else:
                return False
        return False


    def tem_mais_de_um(self, index):
        linhas_anteriores = self.dataframe.loc[:index]
        mesmas_mao = linhas_anteriores[(linhas_anteriores['mao'] == linhas_anteriores.loc[index, ('mao')]) &
                                       (linhas_anteriores['linha'] != 'descartavel') &
                                       (linhas_anteriores['tela'] == linhas_anteriores.loc[index, ('tela')]) ]
        tamanho = len(mesmas_mao)
        if tamanho > 1:
            return True
        else:
            return False

    def index_anterior_da_mesma_tela(self,idx):
        if idx > 0:
            for decremento in range(1, idx + 1):
                idx_reverco = idx - decremento
                anterior = self.dataframe.iloc[idx_reverco]
                atual = self.dataframe.iloc[idx]
                if (atual['tela'] == anterior['tela'] and anterior['linha'] != 'descartavel' and atual['mao'] == anterior['mao']):
                    return idx_reverco
        return -1

    def total_de_lisnha(self,index):
        mao_atual = self.dataframe.loc[index, ('mao')]
        tela_atual = self.dataframe.loc[index, ('tela')]
        linha_atual = 'descartavel'
        tamanho = len(self.dataframe[(self.dataframe['tela'] == tela_atual) & (self.dataframe['mao'] == mao_atual) & (self.dataframe['linha'] != linha_atual)])
        return tamanho

    def posicao_por_letra(self,letra,index):
        lista_letras = self.ordenar_lista_pelo_diler(index)
        lista_posicoes = ['SB','BB','UTG','MP','CO','BTN']
        for idx, valor in enumerate(lista_letras):
            if valor == letra:
                return lista_posicoes[idx]
        return ''

