from collections import Counter

class Codigo:

    def __init__(self):
        pass

    def maoListada(self,board,hole_cards): 
        mao_listada = {}
        listar_repeticao = self.listarRepeticao(board,hole_cards)
        listar_flush = self.listarFlush(board,hole_cards)
        listar_street = self.listarStreet(board,hole_cards)
        listar_street_flush = self.listarStreet(board,hole_cards,True)
        mao_listada['repeticao'] = listar_repeticao
        mao_listada['flush'] = listar_flush
        mao_listada['street'] = listar_street
        mao_listada['street_flush'] = listar_street_flush
        return mao_listada

    #============================= Metodos Privados =================================

    def listarFlush(self,board,hole_cards):
        valores = self.separarNumerosDosNapes(board,hole_cards)
        nape = self.napeMaisRecorrente(valores)
        numeros = self.numerosComNape(valores,nape)
        numeros = numeros if valores['napes'].count(nape) >= 5 else None
        return numeros

    def napeMaisRecorrente(self,valores):
        repeticao_napes = dict(Counter(valores['napes']).items())
        maior_repeticao = 0
        nape_mais_repeticao = ''
        for chave,valor in repeticao_napes.items():
            if valor > maior_repeticao:
                maior_repeticao = valor
                nape_mais_repeticao = chave
        return nape_mais_repeticao

    def numerosComNape(self,valores,nape):
        numeros = []
        for idx in range(len(valores['napes'])):
            if valores['napes'][idx] == nape:
                numeros.append(valores['numeros'][idx])
        numeros.sort(reverse = True)
        return numeros

    def listarStreet(self,board,hole_cards,flush=False):
        numero_anterior = 0
        street = []
        valores = self.separarNumerosDosNapes(board,hole_cards)
        numeros = self.numerosComNaipeMaisRecorrente(valores,flush)
        for numero in numeros:
            if (numero_anterior - numero) == 1:
                street.append(numero)
                numero_anterior = numero
                if len(street) == 5:
                    street.sort(reverse = True)
                    return street
            else:
                street = [numero]
                numero_anterior = numero
        return None

    def numerosComNaipeMaisRecorrente(self,valores,flush=False):
        numeros = []
        if flush == True:
            naipe = self.napeMaisRecorrente(valores)
            numeros = self.numerosComNape(valores,naipe)
        else:
            numeros = valores['numeros']
        return self.numerosSemRepeticao(numeros)

    def listarRepeticao(self,board=[],hole_cards=None):
        valores = self.separarNumerosDosNapes(board,hole_cards)
        grupos_repeticao = self.agruparPorRepeticao(valores['numeros'])
        numeros = []
        for i in reversed(range(1,5)):
            numeros += grupos_repeticao[i]
        return numeros[:5]

    def agruparPorRepeticao(self,numeros=[]):
        repeticao_numeros = dict(Counter(numeros).items())
        grupos_repeticao = {1:[],2:[],3:[],4:[]}
        for chave,valor in repeticao_numeros.items():
            for i in range(valor):
                grupos_repeticao[valor].append(chave)
            grupos_repeticao[valor].sort(reverse = True) 
        return grupos_repeticao

    def numerosSemRepeticao(self,numeros):
        numeros_sem_repeticao = []
        repeticao_numeros = dict(Counter(numeros).items())
        for chave,valor in repeticao_numeros.items():
            numeros_sem_repeticao.append(chave)
        if 14 in numeros_sem_repeticao:
            numeros_sem_repeticao.append(1)
        numeros_sem_repeticao.sort(reverse = True)
        return numeros_sem_repeticao


    def separarNumerosDosNapes(self,board,holecads):
        cartas = board + holecads
        valores = {'numeros':[],'napes':[]}
        for carta in cartas:
            valores['numeros'].append(self.tranformarFiguraEmNumero(carta[0]))
            valores['napes'].append(carta[1])
        return valores

    def tranformarFiguraEmNumero(self,figura):
        figuras = { '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                    '8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
        return figuras[figura]

