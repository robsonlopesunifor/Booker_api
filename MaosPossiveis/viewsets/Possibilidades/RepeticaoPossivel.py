from collections import Counter
from . import Forca



class RepeticaoPossivel:

    def __init__(self):
        self.forca = Forca.Forca()
        self.cartas_utilizadas = []
        self.numeros_utilizados = {}
        self.agrupar_numeros = {}
        self.numeros_codificada = []
        self.numeros_restante = []
    
    def definirBoardHoleCards(self,board,hole_cards):
        self.board = board
        self.hole_cards = hole_cards
        self.cartas_utilizadas = board + hole_cards
        self.numeros_utilizados = self.pegarNumeros(self.cartas_utilizadas)
        self.agrupar_numeros = self.agruparPorRepeticao(self.numeros_utilizados) #self.agruparPorRepeticao(figuras)
        self.numeros_codificada = self.cartasCodificada(self.agrupar_numeros)
        self.numeros_restante = self.numerosRestante(self.numeros_utilizados) #self.cartasRestante(figuras)    

    def ocorrenciaForcaRepeticao(self,tipo):
        soma_ocorrencia = 0
        forca_ponderada = 0
        for conjunto in self.conjuntoDesejado(tipo):
            conjunto1 = conjunto[0]
            conjunto2 = conjunto[1]
            ocorrencia = self.ocorrencia(conjunto1,conjunto2)
            soma_ocorrencia += ocorrencia
            desejados = self.gerarDesejados(conjunto1,conjunto2)
            forca = self.forca.forcaMediaDoTipoDeMao(tipo,self.board,desejados,self.hole_cards)
            forca_ponderada += forca * ocorrencia
        forca_media = round((forca_ponderada / soma_ocorrencia),5) if soma_ocorrencia != 0 else 0
        return {'forca':forca_media,'ocorrencia':soma_ocorrencia}

    #=============================== METODOS PRIVADOS ==========================

    def ocorrencia(self,conjunto1,conjunto2):
        carta_descartada = 1 if conjunto1 != 'X' and conjunto1[0] == conjunto2[0] else 0
        nape_descartada  = 1 if conjunto1 != 'X' and conjunto1 == conjunto2 else 0

        ocorrencia = 2
        if conjunto1[0] == 'X' and conjunto2[0] == 'X':
            ocorrencia *= (52 - len(self.cartas_utilizadas))
            ocorrencia *= (51 - len(self.cartas_utilizadas))
        else:
            ocorrencia *= (len(self.agrupar_numeros[conjunto1[0]]))
            ocorrencia *= (4 - conjunto1[0])
            if conjunto2 == 'X':
                ocorrencia *= 52 - 1 - len(self.cartas_utilizadas)
            else:
                ocorrencia *= (len(self.agrupar_numeros[conjunto2[0]]) - carta_descartada) if nape_descartada == 0 else 1
                ocorrencia *= (4 - conjunto2[0] - nape_descartada)
                ocorrencia /= 2 if nape_descartada == 1 and len(self.agrupar_numeros[conjunto2[0]]) == 1 else 1

        return ocorrencia

    def gerarDesejados(self,conjunto1,conjunto2):
        desejados = []
        if conjunto1[0] == conjunto2[0] == 'X':
            desejados = self.__inrelevantesComInrelevantes(conjunto1,conjunto2)
        elif conjunto1[0] != 'X' and conjunto2[0] == 'X':
            desejados = self.__valorComInrelevantes(conjunto1,conjunto2)
        elif conjunto1 == conjunto2:
            desejados = self.__valoresIguaisComNaipeDiferente(conjunto1,conjunto2)
        elif conjunto1[0] == conjunto2[0]:
            desejados = self.__valoresDiferentesComRepeticoesIguais(conjunto1,conjunto2)
        elif conjunto1 != conjunto2:
            desejados = self.__valoresDiferentes(conjunto1,conjunto2)
        return desejados

    
    def conjuntoDesejado(self,tipo,numeros_codificada=None):
        numeros_codificada = self.numeros_codificada if numeros_codificada == None else numeros_codificada
        conjunto_desejado = []
        if tipo == 'par':
            conjunto_desejado = self.conjuntoDesejadoPar(numeros_codificada)
        elif tipo == 'dois_pares':
            conjunto_desejado = self.conjuntoDesejadoDoisPares(numeros_codificada)
        elif tipo == 'trinca':
            conjunto_desejado = self.conjuntoDesejadoTrinca(numeros_codificada)
        elif tipo == 'full_house':
            conjunto_desejado = self.conjuntoDesejadoFullHouse(numeros_codificada)
        elif tipo == 'quadra':
            conjunto_desejado = self.conjuntoDesejadoQuadra(numeros_codificada)
        return conjunto_desejado


    def __inrelevantesComInrelevantes(self,conjunto1,conjunto2):
        desejados = []
        desejados.append([self.naipar(self.numeroMediano()),self.naipar(self.numeroMediano(1))])
        return desejados

    def __valorComInrelevantes(self,conjunto1,conjunto2):
        desejados = []
        for valor in self.agrupar_numeros[conjunto1[0]]:
            desejados.append([self.naipar(valor),self.naipar(self.numeroMediano())])
        return desejados

    def __valoresIguaisComNaipeDiferente(self,conjunto1,conjunto2):
        desejados = []
        for valor in self.agrupar_numeros[conjunto1[0]]: 
            desejados.append([self.naipar(valor),self.naipar(valor)])
        return desejados

    def __valoresDiferentesComRepeticoesIguais(self,conjunto1,conjunto2):
        desejados = []
        numero_agrupado = self.agrupar_numeros[conjunto1[0]]
        tamanho = len(numero_agrupado)
        tamanho_ = tamanho - 1 if tamanho <= 2 else tamanho # 5,2 => [5,2],[2,5] e errado pois gera a mesma forca
        for idx in range(tamanho_): 
            idx2 = idx + 1 if idx + 1 < tamanho else 0
            desejados.append([self.naipar(numero_agrupado[idx]),self.naipar(numero_agrupado[idx2])])
        return desejados

    def __valoresDiferentes(self,conjunto1,conjunto2):
        desejados = []
        for valor1 in self.agrupar_numeros[conjunto1[0]]:
            for valor2 in self.agrupar_numeros[conjunto2[0]]:
                desejados.append([self.naipar(valor1),self.naipar(valor2)])
        return desejados
            

    def conjuntoDesejadoPar(self,numeros_codificadas):
        if numeros_codificadas == [1,1,1,1,1]:
            return [([1],'X')]
        elif numeros_codificadas == [2,1,1,1]:
            return [('X','X')]
        elif numeros_codificadas == [2,2,1]:
            return [('X','X')]
        elif numeros_codificadas == [3,1,1]:
            return [('X','X')]
        elif numeros_codificadas == [3,2]:
            return [('X','X')]
        elif numeros_codificadas == [4,1]:
            return [('X','X')]
        else:
            return []

    def conjuntoDesejadoDoisPares(self,numeros_codificadas):
        if numeros_codificadas == [1,1,1,1,1]:
            return [([1,1],[1,2])]
        elif numeros_codificadas == [2,1,1,1]:
            return [([1],'X')]
        elif numeros_codificadas == [2,2,1]:
            return [('X','X')]
        elif numeros_codificadas == [3,1,1]:
            return [([1],'X')]
        elif numeros_codificadas == [3,2]:
            return [('X','X')]
        elif numeros_codificadas == [4,1]:
            return []
        else:
            return []

    def conjuntoDesejadoTrinca(self,numeros_codificadas):
        if numeros_codificadas == [1,1,1,1,1]:
            return [([1,1],[1,1])]
        elif numeros_codificadas == [2,1,1,1]:
            return [([2],'X'),([1,1],[1,1])]
        elif numeros_codificadas == [2,2,1]:
            return [([2],'X')]
        elif numeros_codificadas == [3,1,1]:
            return [('X','X')]
        elif numeros_codificadas == [3,2]:
            return [('X','X')]
        elif numeros_codificadas == [4,1]:
            return [('X','X')]
        else:
            return []

    def conjuntoDesejadoFullHouse(self,numeros_codificadas):
        if numeros_codificadas == [1,1,1,1,1]:
            return []
        elif numeros_codificadas == [2,1,1,1]:
            return [([2],[1]),([1,1],[1,1])]
        elif numeros_codificadas == [2,2,1]:
            return [([2],'X')]
        elif numeros_codificadas == [3,1,1]:
            return [([1],'X')]
        elif numeros_codificadas == [3,2]:
            return [('X','X')]
        elif numeros_codificadas == [4,1]:
            return []
        else:
            return []

    def conjuntoDesejadoQuadra(self,numeros_codificadas):
        if numeros_codificadas == [1,1,1,1,1]:
            return []
        elif numeros_codificadas == [2,1,1,1]:
            return [([2,1],[2,1])]
        elif numeros_codificadas == [2,2,1]:
            return [([2,1],[2,1])]
        elif numeros_codificadas == [3,1,1]:
            return [([3],'X')]
        elif numeros_codificadas == [3,2]:
            return [([3],'X'),([2,1],[2,1])]
        elif numeros_codificadas == [4,1]:
            return [('X','X')]
        else:
            return []

    def cartasCodificada(self,grupo):
        lista_chave = []
        lista_repeticao = self.listarRepeticao(grupo)
        grupo = self.agruparPorRepeticao(lista_repeticao)
        lista_repeticao = []
        for i in reversed(range(1,5)):
            for j in range(len(grupo[i])):
                lista_chave.append(i) 
        return lista_chave

    def listarRepeticao(self,grupos):
        numeros = []
        for i in reversed(range(1,5)):
            for valor in grupos[i]:
                for j in range(i):
                    numeros.append(valor)
        return numeros[:5]

    def agruparPorRepeticao(self,numeros):
        repeticao_numeros = dict(Counter(numeros).items())
        grupos_repeticao = {1:[],2:[],3:[],4:[]}
        for chave,valor in repeticao_numeros.items():
            grupos_repeticao[valor].append(chave)
            grupos_repeticao[valor].sort(reverse = True) 
        return grupos_repeticao

    def numerosRestante(self,numero_utilizados):
        numeros_restante = []
        for i in range(2,15):
            if i not in numero_utilizados:
                numeros_restante.append(i)
        return numeros_restante

    def numeroMediano(self,deslocamento=0):
        index = 0 if deslocamento == 0 else int(len(self.numeros_restante) - 1 / deslocamento)
        return self.numeros_restante[index]

    def pegarNumeros(self,cartas=[]):
        numeros_utilizadas = []
        for carta in cartas:
            numero = self.tranformarFiguraEmNumero(carta[0])
            numeros_utilizadas.append(numero)
        return numeros_utilizadas
    
    def tranformarFiguraEmNumero(self,figura):
        figuras = { '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                    '8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
        return figuras[figura]

    def naipar(self,numero):
        return ''.join([self.tranformarNumeroEmFigura(numero),'n'])

    def tranformarNumeroEmFigura(self,figura):
        figuras = { 2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',
                    8:'8',9:'9',10:'T',11:'J', 12:'Q',13:'K',14:'A'}
        return figuras[figura]
