import threading
import pandas as pd
import math
from .. import cientista
from Cenografo.models import Cena
from Cientista.models import Cientista


class Analizador(threading.Thread):

    def __init__(self,espera=1):
        self.espera = espera
        self.lista_de_cartas = []
        self.pandas = pd.DataFrame()
        self.cientista = cientista.Cientista(self.lista_de_cartas, self.pandas)
        threading.Thread.__init__(self)

    def run(self):
        self.registrar()

    def registrar(self):
        index = 0
        while index <= self.espera:
            if Cena.objects.quantidade_cientista_pendente() > 0:
                print(Cena.objects.quantidade_cientista_pendente())
                carta = Cena.objects.primeiro_cientista_pendente()
                self.cientista.processar(carta)
                carta.update(set__cientista_processado=True)
                self.salvar_pandas(carta)
                carta.update(set__cientista_salva=True)
                index = 0
            index += 1
        print('fim da tread: ')

    def salvar_pandas(self,carta):
        df = self.pandas
        data = carta['data']
        tela = carta['tela']
        documentos = df[(df['data'] == data) & (df['tela'] == tela)].to_dict('r')
        if documentos != None:
            for documento in documentos:
                documento_sem_nan = {}
                for chave, valor in documento.items():
                    # Quando o np.nan passa para dicionario ele vira um float('NaN')
                    # Não queremos passar o nan no dicionario
                    if isinstance(valor, float) and math.isnan(valor):
                        pass
                    else:
                        documento_sem_nan[chave] = valor

                Cientista(**documento_sem_nan).save()

