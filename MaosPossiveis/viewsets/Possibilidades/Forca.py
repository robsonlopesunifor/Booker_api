import math
from . import Codigo

class Forca:

    def __init__(self):
        self.lista_de_maos = self.listaDeMaos()
        self.codificar = Codigo.Codigo()

    def forcaMediaDoTipoDeMao(self,tipo,board,desejados,hole_cards):
        forca = 0
        for desejado in desejados:
            board_desejado = board + desejado
            forca += self.forcaDoTipoDeMao(tipo,board_desejado,hole_cards)
        forca_media = forca / len(desejados) if len(desejados) > 0 else 0
        return round(forca_media,5)

    #============================= Metodos Privados =================================

    def forcaDoTipoDeMao(self,tipo,board=[],hole_cards=None):
        forca = 0
        mao_codificada = self.codificar.maoListada(board,hole_cards)
        if tipo == 'par':
            forca = self.forcaDoPar(mao_codificada)
        elif tipo == 'dois_pares':
            forca = self.forcaDoDoisPar(mao_codificada)
        elif tipo == 'trinca':
            forca = self.forcaDoTrinca(mao_codificada)
        elif tipo == 'street':
            forca = self.forcaDoStreet(mao_codificada)
        elif tipo == 'flush':
            forca = self.forcaDoFlush(mao_codificada)
        elif tipo == 'full_house':
            forca = self.forcaDoFullHouse(mao_codificada)
        elif tipo == 'quadra':
            forca = self.forcaDoQuadra(mao_codificada)
        elif tipo == 'street_flush':
            forca = self.forcaDoStreetFlush(mao_codificada)
        return forca

    def forcaDoPar(self,mao_codificada):
        carta1 = mao_codificada['repeticao'][0] # par normal
        carta2 = mao_codificada['repeticao'][1] # par normal
        carta4 = mao_codificada['repeticao'][3] # par do full house
        carta5 = mao_codificada['repeticao'][4] # par do full house
        if carta4 == carta5 and carta1 < carta4: # forca do par em caso de full house
            carta1 = mao_codificada['repeticao'][0]
            carta2 = mao_codificada['repeticao'][1]
            carta3 = mao_codificada['repeticao'][2]
            forca_residual = self.forcaResidual([carta1,carta2,carta3])
            return self.lista_de_maos.index([carta4,carta5]) + 1 + forca_residual
        if [carta1,carta2] in self.lista_de_maos and carta1 == carta2: # forca do par normal 
            carta3 = mao_codificada['repeticao'][2]
            carta4 = mao_codificada['repeticao'][3]
            carta5 = mao_codificada['repeticao'][4]
            forca_residual = self.forcaResidual([carta3,carta4,carta5])
            return self.lista_de_maos.index([carta1,carta2]) + 1 + forca_residual
        else:
            return 0

    def forcaDoDoisPar(self,mao_codificada):
        carta1 = mao_codificada['repeticao'][0]
        carta2 = mao_codificada['repeticao'][1]
        carta3 = mao_codificada['repeticao'][2]
        carta4 = mao_codificada['repeticao'][3]
        carta5 = mao_codificada['repeticao'][4]
        if [carta1,carta2,carta3,carta4] in self.lista_de_maos and carta1 == carta2 and carta3 == carta4:
            carta5 = mao_codificada['repeticao'][4]
            forca_residual = self.forcaResidual([carta5])
            return self.lista_de_maos.index([carta1,carta2,carta3,carta4]) + 1 + forca_residual
        elif carta1 == carta2 and carta4 == carta5:
            lista = [carta1,carta2,carta4,carta5]
            lista.sort(reverse = True)
            forca_residual = self.forcaResidual([carta3])
            return self.lista_de_maos.index(lista) + 1 + forca_residual
        else:
            return 0

    def forcaDoTrinca(self,mao_codificada):
        carta1 = mao_codificada['repeticao'][0]
        carta2 = mao_codificada['repeticao'][1]
        carta3 = mao_codificada['repeticao'][2]
        if [carta1,carta2,carta3] in self.lista_de_maos and carta1 == carta2 == carta3:
            carta4 = mao_codificada['repeticao'][3]
            carta5 = mao_codificada['repeticao'][4]
            forca_residual = self.forcaResidual([carta4,carta5])
            return self.lista_de_maos.index([carta1,carta2,carta3]) + 1 + forca_residual
        else:
            return 0

    def forcaDoStreet(self,mao_codificada):
        if mao_codificada['street'] in self.lista_de_maos:
            return self.lista_de_maos.index(mao_codificada['street']) + 1
        else:
            return 0

    def forcaDoFlush(self,mao_codificada):
        if mao_codificada['flush'] != None:
            carta1 = mao_codificada['flush'][0]
            carta2 = mao_codificada['flush'][1]
            carta3 = mao_codificada['flush'][2]
            carta4 = mao_codificada['flush'][3]
            carta5 = mao_codificada['flush'][4]
            forca_residual = self.forcaResidual([carta1,carta2,carta3,carta4,carta5])
            return self.lista_de_maos.index('flush') + 1 + forca_residual
        else:
            return 0

    def forcaDoFullHouse(self,mao_codificada):
        carta1 = mao_codificada['repeticao'][0]
        carta2 = mao_codificada['repeticao'][1]
        carta3 = mao_codificada['repeticao'][2]
        carta4 = mao_codificada['repeticao'][3]
        carta5 = mao_codificada['repeticao'][4]
        if [carta1,carta2,carta3,carta4,carta5] in self.lista_de_maos:
            return self.lista_de_maos.index([carta1,carta2,carta3,carta4,carta5]) + 1
        else:
            return 0

    def forcaDoQuadra(self,mao_codificada):
        carta1 = mao_codificada['repeticao'][0]
        carta2 = mao_codificada['repeticao'][1]
        carta3 = mao_codificada['repeticao'][2]
        carta4 = mao_codificada['repeticao'][3]
        if [carta1,carta2,carta3,carta4] in self.lista_de_maos and carta1 == carta2 == carta3 == carta4:
            carta5 = mao_codificada['repeticao'][4]
            forca_residual = self.forcaResidual([carta5])
            return self.lista_de_maos.index([carta1,carta2,carta3,carta4]) + 1 + forca_residual
        else:
            return 0

    def forcaDoStreetFlush(self,mao_codificada):
        street_flush = mao_codificada['street_flush']
        if street_flush != None:
            street_flush.append('sf')
            return self.lista_de_maos.index(street_flush) + 1
        return 0

    def forcaResidual(self,lista):
        forca = 0
        tamanho = len(lista) - 1
        for idx in range(len(lista)):
            forca += math.pow(14,idx)*lista[(tamanho-idx)]
        forca = math.pow(10,(-1*len(str(int(forca)))))*int(forca)
        return forca

    def listaDeMaos(self):
        lista_de_maos = []
        lista_de_maos += self.listaDePar()
        lista_de_maos += self.listaDeDoisPar()
        lista_de_maos += self.listaDeTrinca()
        lista_de_maos += self.listaDeStreet()
        lista_de_maos += self.listaDeFlush()
        lista_de_maos += self.listaDeFullHouse()
        lista_de_maos += self.listaDeQuadra()
        lista_de_maos += self.listaDeStreetFlush()
        return lista_de_maos

    def listaDePar(self):
        par = []
        for numero in range(2,15):
            par.append([numero,numero])
        return par

    def listaDeDoisPar(self):
        dois_pares = []
        for numero1 in range(2,15):
            for numero2 in range(2,15):
                if numero1 > numero2:
                    dois_pares.append([numero1,numero1,numero2,numero2])
        return dois_pares

    def listaDeTrinca(self):
        trica = []
        for numero in range(2,15):
            trica.append([numero,numero,numero])
        return trica

    def listaDeStreet(self):
        street = []
        for numero in range(5,15):
            lista = [valor for valor in reversed(range(numero-4,numero+1))]
            street.append(lista)
        return street

    def listaDeFlush(self):
        flush = []
        flush.append('flush')
        return flush

    def listaDeFullHouse(self):
        full_house = []
        for numero1 in range(2,15):
            for numero2 in range(2,15):
                full_house.append([numero1,numero1,numero1,numero2,numero2])
        return full_house

    def listaDeQuadra(self):
        quadra = []
        for numero in range(2,15):
            quadra.append([numero,numero,numero,numero])
        return quadra

    def listaDeStreetFlush(self):
        street_flush = []
        for numero in range(5,15):
            lista = [valor for valor in reversed(range(numero-4,numero+1))]
            lista.append('sf')
            street_flush.append(lista)
        return street_flush
