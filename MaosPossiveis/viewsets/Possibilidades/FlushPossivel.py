from collections import Counter
import random
from . import Forca

class FlushPossivel:

    def __init__(self):
        self.board = []
        self.hole_cards = []
        self.cartas = []
        self.naipe_mais_recorrente = {}
        self.forca = Forca.Forca()

    def definirBoardHoleCards(self,board,hole_cards):
        self.board = board
        self.hole_cards = hole_cards
        self.cartas = board + hole_cards
        self.naipe_mais_recorrente = self.naipeMasRecorrente()


    def ocorrenciaForcaFlush(self,naipes=None):
        if naipes: self.mudarNaipeHoleCards(naipes)
        ocorrencia = self.ocorrencia()
        desejados = self.desejado()
        forca = self.forca.forcaMediaDoTipoDeMao('flush',self.board,desejados,self.hole_cards)
        return {'forca':forca,'ocorrencia':ocorrencia} 


    def ocorrencia(self):
        ocorrencia = 0
        naipe_repetido = self.naipe_mais_recorrente['repeticao']
        if naipe_repetido == 3: 
            ocorrencia = 2*(14 - 3)*(14 - 4)
        elif naipe_repetido == 4: 
            ocorrencia = 2*(14 - 4)*(52 - 5 -1) 
        elif naipe_repetido == 5: 
            ocorrencia = 2*(52 - 5)*(52 - 5 -1) 
        return ocorrencia

    def desejado(self):
        naipe_repetido = self.naipe_mais_recorrente['repeticao']
        desejados = []
        cartas_desejadas = self.cartasRestantes(True)
        cartas_restantes = self.cartasRestantes()
        carta_desejada_1 = self.elementoMediano(cartas_desejadas)
        carta_desejada_2 = self.elementoMediano(cartas_desejadas,1)
        carta_qualquer_1 = self.elementoMediano(cartas_restantes)
        carta_qualquer_2 = self.elementoMediano(cartas_restantes,1)

        if naipe_repetido == 3:
            desejados = [[carta_desejada_1,carta_desejada_2]]
        elif naipe_repetido == 4: 
            desejados = [[carta_desejada_1,carta_qualquer_1]]
        elif naipe_repetido == 5: 
            desejados = [[carta_qualquer_1,carta_qualquer_2]]
        return desejados

    def elementoMediano(self,lista,deslocamento=0):
        index = int(len(lista)/2) + deslocamento
        return lista[index]

    def cartasRestantes(self,desejados=False):
        cartas_restantes = []
        naipe_principal = self.naipe_mais_recorrente['naipe']
        for i in range(2,15):
            naipe_ = self.naipeDiferente() if desejados == False else naipe_principal
            if i not in self.pegarNumeros():
                figura = self.tranformarNumeroEmFigura(i)
                cartas_restantes.append(''.join([figura,naipe_]))
        return cartas_restantes

    def pegarNumeros(self):
        numeros = []
        for carta in self.cartas:
            numeros.append(self.tranformarFiguraEmNumero(carta[0]))
        return numeros

    def pegarNaipes(self):
        return [carta[1] for carta in self.cartas]

    def naipeMasRecorrente(self):
        lista_naipes = self.pegarNaipes()
        repeticao_napes = dict(Counter(lista_naipes).items())
        maior_repeticao = 0
        nape_mais_repeticao = {}
        for chave,valor in repeticao_napes.items():
            if valor > maior_repeticao:
                maior_repeticao = valor
                nape_mais_repeticao = {'naipe':chave,'repeticao':valor}
        return nape_mais_repeticao

    def mudarNaipeHoleCards(self,naipes):
        self.cartas = self.board
        naipe_recorrente = self.naipeMasRecorrente()
        self.cards_1 = "".join([self.hole_cards[0][0],naipe_recorrente['naipe']])
        naipe = naipe_recorrente['naipe'] if naipes[1] == 's' else 'n'
        self.cards_2 = "".join([self.hole_cards[1][0],naipe])
        self.hole_cards = [ self.cards_1, self.cards_2 ]
        self.cartas = self.hole_cards + self.board
        self.naipe_mais_recorrente = self.naipeMasRecorrente()

    def naipeDiferente(self):
        naipes = ['c','s','p','o']
        naipe_principal = self.naipe_mais_recorrente['naipe']
        index = naipes.index(naipe_principal)
        index = index + 1 if index == 3 else 0
        return naipes[index]

    def tranformarFiguraEmNumero(self,figura):
        figuras = { '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                    '8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
        return figuras[figura]

    def tranformarNumeroEmFigura(self,figura):
        figuras = { 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
                    8:'8',9:'9',10:'T',11:'J', 12:'Q',13:'K',14:'A'}
        return figuras[figura]

    

