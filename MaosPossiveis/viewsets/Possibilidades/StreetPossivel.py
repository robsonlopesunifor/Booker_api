from collections import Counter
import random
from . import Forca

class StreetPossivel:

    def __init__(self):
        self.board = []
        self.hole_cards = []
        self.cartas = []
        self.forca = Forca.Forca()
        self.flush = False

    def definirBoardHoleCards(self,board,hole_cards):
        self.board = board
        self.hole_cards = hole_cards
        self.cartas = self.board + self.hole_cards

    def ocorrenciaForcaStreet(self,flush=False):
        self.flush = flush
        ocorrencia = self.ocorrencia()
        desejados = self.desejado()
        mao_str = 'street' if self.flush == False else 'street_flush'
        forca = self.forca.forcaMediaDoTipoDeMao(mao_str,self.board,desejados,self.hole_cards)
        return {'forca':forca,'ocorrencia':ocorrencia}

    def desejado(self):
        desejados = []
        seguencia = self.gerarSequencia()
        
        for idx in reversed(range(1,len(seguencia)-4)):
            fatia = seguencia[idx:(idx+5)]
            cartas_restantes = self.cartasRestantes(fatia)
            carta_qualquer_1 = cartas_restantes[0]
            carta_qualquer_2 = cartas_restantes[-1]
            gaps = fatia.count(0)
            desejado = []
            naipe = 'n' if self.flush == False else self.naipeMasRecorrente()
            for idx2 in range(len(fatia)):
                if fatia[idx2] == 0:
                    desejado.append(''.join([self.tranformarNumeroEmFigura(idx+idx2),naipe]))
            if gaps == 2:
                desejados.append(desejado)
            elif gaps == 1:
                desejado.append(carta_qualquer_1)
                desejados.append(desejado)
            elif gaps == 0:
                desejado.append(carta_qualquer_1)
                desejado.append(carta_qualquer_2)
                desejados.append(desejado)
        return desejados

    def ocorrencia(self):
        ocorrencia = 0
        seguencia = self.gerarSequencia()
        
        for idx in reversed(range(1,len(seguencia)-4)):
            fatia = seguencia[idx:(idx+5)]
            gaps = fatia.count(0)
            quantidade_naipes = 4 if self.flush == False else 1
            if gaps == 2:
                ocorrencia += 2 * quantidade_naipes * quantidade_naipes
            elif gaps == 1:
                ocorrencia += 2 * quantidade_naipes * (52 - 5 -1)
            elif gaps == 0:
                ocorrencia = 2 * (52 - 5) * (52 - 5 -1)
                break
        return ocorrencia

    def retornarNumero(self):
        numero = []
        for carta in self.cartas:
            if self.flush == False:
                numero.append(self.tranformarFiguraEmNumero(carta[0]))
                if carta[0] == 'A':
                    numero.append(1)
            else:
                naipe = self.naipeMasRecorrente()
                if carta[1] == naipe:
                    numero.append(self.tranformarFiguraEmNumero(carta[0]))
                    if carta[0] == 'A' and carta[1] == naipe:
                        numero.append(1)
                
        return numero
        
    def gerarSequencia(self,desejados=False):
        numeros = self.retornarNumero()
        sequencia = []
        for i in range(0,15):
            valor = i if i in numeros else 0    
            sequencia.append(valor)
        return sequencia

    def cartasRestantes(self,numeros_de_fora):
        cartas_restantes = []
        numeros = self.retornarNumero() + numeros_de_fora
        for i in range(2,15):
            if i not in numeros:
                figura = self.tranformarNumeroEmFigura(i)
                cartas_restantes.append(''.join([figura,'n']))
        return cartas_restantes

    def tranformarFiguraEmNumero(self,figura):
        figuras = { '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                    '8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
        return figuras[figura]

    def tranformarNumeroEmFigura(self,figura):
        figuras = { 1:'A',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
                    8:'8',9:'9',10:'T',11:'J', 12:'Q',13:'K',14:'A'}
        return figuras[figura]

    def naipeMasRecorrente(self):
        lista_naipes = self.pegarNaipes()
        repeticao_napes = dict(Counter(lista_naipes).items())
        maior_repeticao = 0
        niape = 'n'
        for chave,valor in repeticao_napes.items():
            if valor > maior_repeticao:
                maior_repeticao = valor
                niape = chave
        return niape if maior_repeticao >= 3 else 'n'

    def pegarNaipes(self):
        return [carta[1] for carta in self.cartas]



    