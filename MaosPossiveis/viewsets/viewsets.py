from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import MaosPossiveisSerializer
from .Possibilidades.MaosPossiveis import MaosPossiveis


class MaosPossiveisViewSet(viewsets.ViewSet):
    serializer_class = MaosPossiveisSerializer

    def list(self, request, *args, **kwargs): 
        "recebe o board e o rang de hole_cards, e retorna as maos possiveis "
        #queryset = Cena.objects.primeiro_cientista_pendente()
        #serializer = self.get_serializer(queryset)
        board = request.query_params.getlist('board',[])
        hole_cards = request.query_params.getlist('hole_card',[])
        hole_cards = [[hole_card[0:2],hole_card[2:4]] for hole_card in hole_cards]
        desejado = MaosPossiveis()
        possiveis = desejado.maosPossiveisPorRange(board,hole_cards)
        return Response(possiveis)

