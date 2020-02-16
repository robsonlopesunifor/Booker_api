from collections import Counter
import random
from . import RepeticaoPossivel, StreetPossivel, FlushPossivel

class MaosPossiveis:

    def __init__(self):
        self.possivel = {'rodada':'flop','ocorrencia':self.ocorrenciaFlop(),'maos':{}}
        self.repeticaoPossivel = RepeticaoPossivel.RepeticaoPossivel()
        self.streetPossivel = StreetPossivel.StreetPossivel()
        self.flushPossivel = FlushPossivel.FlushPossivel()

    def definirBoardHoleCards(self,board,hole_cards):
        self.repeticaoPossivel.definirBoardHoleCards(board,hole_cards)
        self.streetPossivel.definirBoardHoleCards(board,hole_cards)
        self.flushPossivel.definirBoardHoleCards(board,hole_cards)

    def ocorrenciaForca(self,board,hole_card):
        self.definirBoardHoleCards(board,hole_card)
        self.possivel['maos']['par'] = self.repeticaoPossivel.ocorrenciaForcaRepeticao('par')
        self.possivel['maos']['dois_pares'] = self.repeticaoPossivel.ocorrenciaForcaRepeticao('dois_pares')
        self.possivel['maos']['trinca'] = self.repeticaoPossivel.ocorrenciaForcaRepeticao('trinca')
        self.possivel['maos']['street'] = self.streetPossivel.ocorrenciaForcaStreet()
        self.possivel['maos']['flush'] = self.flushPossivel.ocorrenciaForcaFlush()
        self.possivel['maos']['flush_ss'] = self.flushPossivel.ocorrenciaForcaFlush('ss')
        self.possivel['maos']['flush_sn'] = self.flushPossivel.ocorrenciaForcaFlush('sn')
        self.possivel['maos']['full_house'] = self.repeticaoPossivel.ocorrenciaForcaRepeticao('full_house')
        self.possivel['maos']['quadra'] = self.repeticaoPossivel.ocorrenciaForcaRepeticao('quadra')
        self.possivel['maos']['street_flush'] = self.streetPossivel.ocorrenciaForcaStreet(True)
        self.porcentagemOcorrenciaForca()

        return self.possivel

    def porcentagemOcorrenciaForca(self):
        for chave in self.possivel['maos']:
            mao = self.possivel['maos'][chave]
            mao['porcentagem'] = round((mao['ocorrencia'] / self.possivel['ocorrencia']) * 100,3)

    def maosPossiveisPorRange(self,board,range=[]):
        maos = {}
        for hole_card in range:
            possivel = self.ocorrenciaForca(board,hole_card)
            for mao in possivel['maos']:
                if mao not in maos: maos[mao] = [] 
                dados_do_hole_cards = {}
                dados_do_hole_cards['forca'] = possivel['maos'][mao]['forca']
                dados_do_hole_cards['porcentagem'] = possivel['maos'][mao]['porcentagem']
                dados_do_hole_cards['texto'] = self.pegarNumeros(hole_card)
                dados_do_hole_cards['naipes'] = [True,True]
                maos[mao].append(dados_do_hole_cards)
        return maos

    def pegarNumeros(self,hole_card):
        return [carta[0] for carta in hole_card]

    def ocorrenciaFlop(self):
        return 2 * (52 - 5) * (52 - 6)

    