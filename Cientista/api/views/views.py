from rest_framework.views import APIView, Response
from . import Analizador
from Cenografo.models import Cena
from Cientista.models import Cientista

class CientistaView(APIView):

    def __init__(self):
        self.thread_ativa = False

    def get(self, request, format=None):
        return Response(self.thread_ativa)

    def post(self, request, format=None):
        self.__analizarCenas()
        return Response("Cenas analizadas")

    def put(self, request, format=None):
        dados = dict(**request.data)
        for mao in dados['maos']:
            self.__esquecerCientistaProcessado(mao)
            self.__deletarMaoCientista(mao)
        self.__analizarCenas()
        return Response("Cenas reanalizadas")

    def __esquecerCientistaProcessado(self,mao):
        queryset_jogada = Cientista.objects.jogadasPorMao(mao)
        for jogada in queryset_jogada:
            data = jogada['data']
            tela = jogada['tela']
            print(data,tela)
            Cena.objects.esquecer_cientista_processado(tela,data)

    def __deletarMaoCientista(self,mao):
        Cientista.objects.deletarMao(mao)

    def __analizarCenas(self):
        analizador = Analizador.Analizador()
        analizador.start()
        analizador.join()


