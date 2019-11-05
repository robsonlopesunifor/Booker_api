from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
import pandas as pd
import datetime
from Cientista.models import Cientista
from Cenografo.models import Cena
from .serializers import CientistaSerializer
from Cenografo.serializers import CenaSerializer



class CientistaViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = CientistaSerializer

    def get_queryset(self):
        return Cientista.objects.all()

    @action(methods=['get'], detail=False)
    def quantidadeJogadaPorTelaData(self, request):
        data = request.query_params.get('data',None)
        tela = request.query_params.get('tela',None)

        data_inicial_texto = '{} 00:00:00.0000'.format(data)
        data_final_texto = '{} 23:59:59.9999'.format(data)
        data_inicial = datetime.datetime.strptime(data_inicial_texto, '%Y-%m-%d %H:%M:%S.%f')
        data_final = datetime.datetime.strptime(data_final_texto, '%Y-%m-%d %H:%M:%S.%f')

        queryset = Cientista.objects.jogadasEntreIntervaloDataPorTela(data_inicial,data_final,tela)
        return Response(len(queryset))

    @action(methods=['get'], detail=False)
    def telaPorData(self, request):
        data = request.query_params.get('data',None)

        data_inicial_texto = '{} 00:00:00.0000'.format(data)
        data_final_texto = '{} 23:59:59.9999'.format(data)
        data_inicial = datetime.datetime.strptime(data_inicial_texto, '%Y-%m-%d %H:%M:%S.%f')
        data_final = datetime.datetime.strptime(data_final_texto, '%Y-%m-%d %H:%M:%S.%f')

        queryset = Cientista.objects.jogadasEntreIntervaloData(data_inicial,data_final)
        serializer = self.get_serializer(queryset, many=True)
        pandas = serializer.converterQuerysetEmPandas()

        pandas_agrupado = pandas.groupby(['tela'])['tela'].count()
        lista_de_tela = pandas_agrupado.index.tolist()

        return Response(lista_de_tela)

    @action(methods=['get'], detail=False)
    def jogadasMaosPorDataTela(self, request):
        data = request.query_params.get('data',None)
        tela = request.query_params.get('tela',None)

        data_inicial_texto = '{} 00:00:00.0000'.format(data)
        data_final_texto = '{} 23:59:59.9999'.format(data)
        data_inicial = datetime.datetime.strptime(data_inicial_texto, '%Y-%m-%d %H:%M:%S.%f')
        data_final = datetime.datetime.strptime(data_final_texto, '%Y-%m-%d %H:%M:%S.%f')

        queryset = Cientista.objects.jogadasEntreIntervaloDataPorTela(data_inicial,data_final,tela)
        serializer = self.get_serializer(queryset, many=True)
        pandas = serializer.converterQuerysetEmPandas()
        pandas_agrupado = pandas.groupby(['mao'])['mao'].count()

        #lista_de_jogadas_por_mao = pandas_agrupado.tolist()
        lista_de_jogadas_por_mao = pandas_agrupado.to_dict().items()
        
        return Response(lista_de_jogadas_por_mao)

    @action(methods=['get'], detail=False)
    def jogadasPorMao(self, request):
        mao = request.query_params.get('mao',None)

        queryset = Cientista.objects.jogadasPorMao(mao)
        serializer = self.get_serializer(queryset, many=True)
        
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def jogadasPorCordenadas(self, request):
        data = request.query_params.get('data',None)
        tela = int(request.query_params.get('tela',-1))
        mao = int(request.query_params.get('mao',-1))
        jogada = int(request.query_params.get('jogada',-1))

        data_inicial_texto = '{} 00:00:00.0000'.format(data)
        data_final_texto = '{} 23:59:59.9999'.format(data)
        data_inicial = datetime.datetime.strptime(data_inicial_texto, '%Y-%m-%d %H:%M:%S.%f')
        data_final = datetime.datetime.strptime(data_final_texto, '%Y-%m-%d %H:%M:%S.%f')

        queryset = Cientista.objects.jogadasPorCordenadas(data_inicial,data_final,tela,mao,jogada)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.ultimaMao())

    @action(methods=['get'], detail=False)
    def ultima_jogada(self, request):
        queryset = Cientista.objects.ultima_jogada(0)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.ultima_jogada())

    @action(methods=['get'], detail=False)
    def ultimaMesa(self, request):
        tela = int(request.query_params.get('tela',None))
        queryset = Cientista.objects.ultimaMesa(tela)
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.ultimaMao())

    @action(methods=['get'], detail=False)
    def confronto_ultima_jogada(self, request):
        queryset = Cientista.objects.ultima_jogada(0)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.confronto_ultima_jogada())

    @action(methods=['get'], detail=False)
    def imagemPorCordenada(self, request):
        tela = int(request.query_params.get('tela',-1))
        mao = int(request.query_params.get('mao',-1))
        jogada = int(request.query_params.get('jogada',-1))

        queryset = Cientista.objects.jogadaPorCordenada(mao,jogada)
        data_str = str(queryset.data)
        data_fatiada = data_str.split(" ")
        data_fatiada[1] = data_fatiada[1].replace(':','-')
        data_fatiada[1] = data_fatiada[1].replace('.','-')
        url = "".join(['imagens/',data_fatiada[0],'/',data_fatiada[1],'.jpg'])
        return Response({'url':url})



