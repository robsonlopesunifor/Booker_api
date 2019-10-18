from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from Historico.models import Historico
from .serializers import HistoricoSerializer

class HistoricoViewSet(viewsets.ModelViewSet):
    
    lookup_field = 'id'
    serializer_class = HistoricoSerializer

    def get_queryset(self):
        return Historico.objects.all()

    @action(methods=['get'],detail=False) # detail=False Nao passa a PK
    def ultima_jogada(self,request):
        queryset = Historico.objects.all()
        queryset = queryset.order_by('-_id')[0]
        serializer = self.get_serializer(queryset)
        return Response(serializer.data) 


