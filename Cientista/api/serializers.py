from rest_framework_mongoengine import serializers
from rest_framework.serializers import ListSerializer
import pandas as pd
from Cientista.models import Cientista
import copy


class CustomListSerializer(ListSerializer):

    arvore_data = {}
    letra_ordenada_por_posicao = []


    def telasPresentes(self):
        pandas = self.converter_queryset_em_pandas()
        pandas_agrupado = pandas.groupby(['tela'])['tela'].count()
        lista_de_tela = pandas_agrupado.index.tolist()
        return lista_de_tela

    def converterQuerysetEmPandas(self):
        output = pd.DataFrame()
        for linha in self.data:
            output = output.append(linha, ignore_index=True)
        return output

    def confrontoUltimaJogada(self):
        #confronto = {'SB': {'protagonista': 'heroi', 'imagem': 'caller','etapa':'PRE-FLOP', 'vs': 'CO',},
        #        'BB': {'protagonista': 'vilao', 'imagem': 'caller','etapa':'PRE-FLOP', 'vs': 'CO',},
        #        'CO': {'protagonista': 'vilao', 'imagem': 'agressor','etapa':'PRE-FLOP', 'vs': 'BB',}}
        return {'estilo_oponente':'padrao',
                'protagonista':'heroi',
                'posicao_heroi':self.data[0]['heroi_posicao'],
                'posicao_vilao':self.data[0]['nome_vilao']}

    def confrontosUltimaMao(self):
        return [{'SB': {'heroi':True,   'agressor': False,'vs':'CO'},
                 'BB': {'heroi': False, 'agressor': False, 'vs': 'CO'},
                 'CO': {'heroi': False, 'agressor': True, 'vs': 'BB'}},]

    def ultimaJogada(self):
        self.letra_ordenada_por_posicao = self.__ordenarLetraPorPosicao(self.data[0])
        self.arvore_data['dados_constantes'] = self.__dadosConstantes(self.data[0])
        self.arvore_data['dados_variaveis'].append(self.__dadosVariaveis(self.data[0]))
        return self.arvore_data

    def ultimaMao(self):
        self.letra_ordenada_por_posicao = self.__ordenarLetraPorPosicao(self.data[0])
        self.arvore_data = {'board':{}, 
                            'confronto':{},
                            'confronto_pre_flop':{},
                            'historico':{   'SB': {'PRE_FLOP':[],'FLOP':[],'TURN':[],'RIVER':[]},
                                            'BB': {'PRE_FLOP':[],'FLOP':[],'TURN':[],'RIVER':[]},
                                            'UTG':{'PRE_FLOP':[],'FLOP':[],'TURN':[],'RIVER':[]},
                                            'MP': {'PRE_FLOP':[],'FLOP':[],'TURN':[],'RIVER':[]},
                                            'CO': {'PRE_FLOP':[],'FLOP':[],'TURN':[],'RIVER':[]},
                                            'BTN':{'PRE_FLOP':[],'FLOP':[],'TURN':[],'RIVER':[]}}}

        for linha in self.data:
            self.arvore_data['board'] = self.__dadosBoard(linha)
            self.arvore_data['confronto'] = self.__dadosConfronto(linha)
            if(linha['bord_etapa'] == 'PRE_FLOP'):
                self.arvore_data['confronto_pre_flop'] = self.__dadosConfronto(linha)
            self.__dadosHistoricosDeJogadas(linha)
        return self.arvore_data

    def imagemDaJogada(self):
        print(self.data)
        return self.data

    def __dadosBoard(self,linha):
        cartas = ['bord_FLOP_1','bord_FLOP_2','bord_FLOP_3','bord_TURN','bord_RIVER']
        dados_do_bord = {'etapa':linha['bord_etapa'],'cartas':[]}
        for carta in cartas:
            nape_valor = list(linha[carta])
            if len(nape_valor) > 0:
                dados_do_bord['cartas'].append({'nape':nape_valor[0],'valor':nape_valor[1]})
        return dados_do_bord

    def __dadosConfronto(self,linha):
        confronto = {   'heroi':linha['heroi_posicao'],
                        'heroi_combo':linha['heroi_combo'],
                        'agressor':linha['nome_vilao'],
                        'segundo_agressor':linha['nome_vilao'],
                        'vez':self.__dadosVez(linha),
                        'jogadores_ativos':self.__dadosJogadoresAtivos(linha),
                        'board_etapa':linha['bord_etapa'] }
        return confronto

    def __dadosVez(self,linha):
        for posicao_letra in self.letra_ordenada_por_posicao:
            posicao = posicao_letra[0]
            letra = posicao_letra[1]
            if linha['vez_{}'.format(letra)] == True:
                return posicao

    def __dadosJogadoresAtivos(self,linha):
        dados_jogadores_ativos = []
        for posicao_letra in self.letra_ordenada_por_posicao:
            posicao = posicao_letra[0]
            letra = posicao_letra[1]
            ativos = linha['hole_cards_{}'.format(letra)]
            if ativos == False:
                dados_jogadores_ativos.append(posicao)
        return dados_jogadores_ativos

    def __dadosHistoricosDeJogadas(self,linha):
        posicao_jogador = linha['ultimo_jogador_posicao']
        board_etapa = linha['bord_etapa']
        blind = linha['size_bet_blind']
        bet = linha['nome_bet']
        acao = linha['nome_acao']
        pote = linha['pote']

        if posicao_jogador != 'null':
            self.arvore_data['historico'][posicao_jogador][board_etapa].append({'acao':acao,
                                                                                'jogada':bet,
                                                                                'blind':blind,
                                                                                'pote':pote})

    #-----------------------------------------------------------------------------------

    def __dadosConstantes(self,linha):
        dados_constantes = {
            'diler':'','heroi':'','mao':0,'data':'','tela':0,'vencedor':'',
            'jogadores':{} #'A': {'posicao':'','nome':'','carta':'','fichas_iniciais':0.0
        }
        for posicao_letra in self.letra_ordenada_por_posicao:
            posicao = posicao_letra[0]
            letra = posicao_letra[1]
            dados_constantes['heroi'] = linha['heroi_posicao']
            dados_constantes['mao'] = linha['mao']
            dados_constantes['data'] = linha['data']
            dados_constantes['tela'] = linha['tela']
            dados_constantes['vencedor'] = linha['vencedor']
            if linha['diler_{}'.format(letra)] == True:
                dados_constantes['diler'] = letra
            carta_1 = linha['combo_{}_1'.format(letra)]
            carta_2 = linha['combo_{}_2'.format(letra)]
            dados_constantes['jogadores'][posicao] = {'carta':(carta_1,carta_2),'letra':letra}
        return dados_constantes

    def __dadosVariaveis(self,linha):
        dados_variaveis = { 'pote':self.__dadosDoPote(linha),
                            'bord':self.__dadosDoBord(linha),
                            'vez':self.__dadosDaVez(linha),
                            'jogadores_ativos':self.__dadosJogadoresAtivos(linha),
                            'informacoes':self.__dadosAnalisados(linha)
                           }
        return dados_variaveis

    def __dadosDoPote(self,linha):
        dados_do_pote = {'pote':linha['pote'],
                         'pote_rodada':linha['pote_rodada']}
        return dados_do_pote

    def __dadosDoBord(self,linha):
        dados_do_bord = {'etapa':linha['bord_etapa'],
                         'cartas':(linha['bord_FLOP_1'],
                                   linha['bord_FLOP_2'],
                                   linha['bord_FLOP_3'],
                                   linha['bord_TURN'],
                                   linha['bord_RIVER'])}
        return dados_do_bord

    def __dadosDaVez(self,linha):
        vez = {'letra': 'A', 'posicao': 'BTN'}
        for posicao_letra in self.letra_ordenada_por_posicao:
            posicao = posicao_letra[0]
            letra = posicao_letra[1]
            if linha['vez_{}'.format(letra)] == True:
                vez['letra'] = letra
                vez['posicao'] = posicao
                break
        return vez

    def __dadosJogadoresAtivos(self,linha):
        dados_jogadores_ativos = []

        for posicao_letra in self.letra_ordenada_por_posicao:
            posicao = posicao_letra[0]
            letra = posicao_letra[1]
            ativos = linha['hole_cards_{}'.format(letra)]
            if ativos == False:
                dados_jogadores_ativos.append(posicao)
        return dados_jogadores_ativos

    def __dadosAnalisados(self,linha):

        analise_dos_dados = {'ultimo_agressor':self.__dadosAnalisadosUltimoAgressor(linha),
                             'ultima_jogada':{'jogador':self.__dadosAnalisadosUltimaJogador(linha),
                                              'jogada':self.__dadosAnalisadosUltimaJogada(linha),
                                              'fichas':self.__dadosAnalisadosUltimaJogadaFichas(linha),
                                              'size_bet':self.__dadosAnalisadosUltimaJogadaNome(linha),}
                             }
        return analise_dos_dados

    def __dadosAnalisadosUltimoAgressor(self,linha):
        return {'letra':'E','posicao':linha['nome_vilao']}

    def __dadosAnalisadosUltimaJogador(self,linha):
        return {'letra':linha['ultimo_jogador_letra'],
                'posicao':linha['ultimo_jogador_posicao']}

    def __dadosAnalisadosUltimaJogada(self,linha):
        return {'nome':linha['nome_jogada'],
                'bet':linha['nome_bet'],
                'acao':linha['nome_acao']}

    def __dadosAnalisadosUltimaJogadaFichas(self, linha):
        letra = linha['ultimo_jogador_letra']
        stack = linha['fichas_{}'.format(letra)] if letra != "null" else -1
        aposta = linha['aposta_{}'.format(letra)] if letra != "null" else -1
        return {'stack': stack, 'aposta': aposta}

    def __dadosAnalisadosUltimaJogadaNome(self,linha):
        return {'blind': linha['size_bet_blind'],
                'pote': linha['size_bet_pote'],
                'vilao': linha['size_bet_vilao'],
                'fichas': linha['size_bet_fichas']}


    def __ordenarLetraPorPosicao(self,linha):
        letra_ordenada_por_posicao = []
        lista_posicao = ['SB','BB','UTG','MP','CO','BTN']
        lista_letra = ['A','B','C','D','E','F']
        lista_letra_ordenada = copy.deepcopy(lista_letra)
        for idx, letra in enumerate(lista_letra):
            rabo = lista_letra_ordenada.pop(0)
            lista_letra_ordenada.append(rabo)
            if linha['diler_{}'.format(letra)] == True:
                break
        for idx, posicao in enumerate(lista_posicao):
            letra_ordenada_por_posicao.append((posicao,lista_letra_ordenada[idx]))
        return letra_ordenada_por_posicao


class CientistaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Cientista
        fields = '__all__'
        list_serializer_class = CustomListSerializer

    def teste_data(self):
        print('------',self.data)
        return self.data
