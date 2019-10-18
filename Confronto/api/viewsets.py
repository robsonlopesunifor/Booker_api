from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from Confronto.models import Confronto, Tabela
from Historico.models import Historico
from .serializers import ConfrontoSerializer
from mongoengine.queryset.visitor  import  Q

class ConfrontoViewSet(viewsets.ModelViewSet):
    
    lookup_field = 'id'
    serializer_class = ConfrontoSerializer

    def get_queryset(self):
        return Confronto.objects.all()

    def list(self, request): #GET
        estilo_oponente = self.request.query_params.get('estilo_oponente',None)
        posicao_heroi = self.request.query_params.get('posicao_heroi',None)
        posicao_vilao = self.request.query_params.get('posicao_vilao',None)
        protagonista = self.request.query_params.get('protagonista',None)
        queryset = Confronto.objects(estilo_oponente=str(estilo_oponente),
                                     posicao_heroi=str(posicao_heroi),
                                     posicao_vilao=str(posicao_vilao),
                                     protagonista=str(protagonista))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request): #PATCH
        estilo_oponente = request.data['estilo_oponente']
        posicao_heroi = request.data['posicao_heroi']
        posicao_vilao = request.data['posicao_vilao']
        protagonista = request.data['protagonista']
        carta = request.data['carta']
        acao = request.data['acao']
        
        tabela = Tabela(carta=carta,acoes=acao)
        resposta = Confronto.objects((Q(estilo_oponente=str(estilo_oponente)) &
                                     Q(posicao_heroi=str(posicao_heroi)) &
                                     Q(posicao_vilao=str(posicao_vilao)) &
                                     Q(protagonista=str(protagonista)) &
                                     Q(tabela__carta=str(carta)))).update(set__tabela__S=tabela)
        
        return Response(resposta)

    @action(methods=['post'],detail=False) # detail=False Nao passa a PK
    def criarNovosConfrontos(self,request):
        estilo = request.data['estilo']
        menssagem = 'confrontos com oponentes do estilo "%s" já existe' %(estilo)
        lista_objeto_confronto = []
        quantos_confontos_com_esse_estilo_existe = Confronto.objects(estilo_oponente="padrao").count()
        if quantos_confontos_com_esse_estilo_existe == 0:
            lista_de_novos_confrontos = self.__criarListaDeConfrontos(estilo)
            for novo_confronto in lista_de_novos_confrontos:
                objeto_confronto = Confronto(**novo_confronto)
                lista_objeto_confronto.append(objeto_confronto)
            Confronto.objects.insert(lista_objeto_confronto)
            menssagem = 'Novos confrontos com oponentes do estilo %s forão criados' % (estilo)
        return Response({'Resutado':menssagem})

    @action(methods=['delete'],detail=False) # detail=False Nao passa a PK
    def deletarTodosConfrontosPorEstilo(self,request):
        estilo = request.data['estilo']
        Confronto.objects(estilo_oponente=estilo).delete()
        menssagem = 'Os confrontos com oponentes do estilo %s forão deletados' % (estilo)
        return Response({'Resutado':''})

    def __criarListaDeConfrontos(self,estilo):
        posicoes = ['SB','BB','UTG','MP','CO','BTN']
        protagonistas = ['heroi','vilao']
        confrontos = []
        if estilo:
            for posicao_heroi in posicoes:
                for posicao_vilao in posicoes:
                    for protagonista in protagonistas:
                        confronto = {'estilo_oponente':estilo,
                                     'posicao_heroi':posicao_heroi,
                                     'posicao_vilao':posicao_vilao,
                                     'protagonista':protagonista,
                                     'tabela':self.__gerarTabela()}
                        confrontos.append(confronto)
        return confrontos


    def __gerarTabela(self):
        lista_de_simbulos = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
        tabela = []
        for idx_carta_1,item_carta_1 in enumerate(lista_de_simbulos):
            for idx_carta_2,item_carta_2 in enumerate(lista_de_simbulos):
                if idx_carta_1 < idx_carta_2:
                    hand = ''.join([item_carta_1,item_carta_2,'s'])
                elif idx_carta_1 == idx_carta_2:
                    hand = ''.join([item_carta_1,item_carta_2])
                else:
                    hand = ''.join([item_carta_2,item_carta_1,'o'])
                tabela.append({'carta':hand,'acoes':''})
        return tabela