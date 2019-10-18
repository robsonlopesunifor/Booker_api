from rest_framework.views import APIView, Response
from . import Analizador

class CientistaView(APIView):

    def __init__(self):
        self.thread_ativa = False

    def get(self, request, format=None):
        return Response(self.thread_ativa)

    def post(self, request, format=None):
        analizador = Analizador.Analizador()
        analizador.start()
        analizador.join()
        return Response("Some Post Response")

