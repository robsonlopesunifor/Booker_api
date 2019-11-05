from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from Cenografo.models import Cena
from ..serializers import CenaSerializer
from . import SalvarImagens

class CenografoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = CenaSerializer

    def get_queryset(self):
        return Cena.objects.all()

    # Cenografo/primeiro_cientista_pendente/
    @action(methods=['get'], detail=False)  # detail=False Nao passa a PK
    def primeiro_cientista_pendente(self, request):
        queryset = Cena.objects.primeiro_cientista_pendente()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    # Cenografo/primeiro_cientista_pendente/
    @action(methods=['get'], detail=False)  # detail=False Nao passa a PK
    def quantidade_cientista_pendente(self, request):
        queryset = Cena.objects.quantidade_cientista_pendente()
        return Response(queryset)

    # Cenografo/primeiro_cientista_pendente/
    @action(methods=['get'], detail=False)  # detail=False Nao passa a PK
    def cientista_processado(self, request):
        queryset = Cena.objects.cientista_processado()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)

    @action(methods=['post'], detail=False)  # detail=False Nao passa a PK
    def salvar_imagens_do_redis(self, request):
        salvarImagens = SalvarImagens.SalvarImagens('imagens_pyker','localhost',6379)
        salvarImagens.start()
        salvarImagens.join()
        return Response({'Imagens salvas'})
