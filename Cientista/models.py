from django.db import models

# Create your models here.
from mongoengine import Document, fields, QuerySet
from mongoengine.queryset.visitor import Q

class CientistaQuerySet(QuerySet):

    def jogadasEntreIntervaloData(self,data_inicial,data_final):
        queryset = self.filter(Q(data__gte=data_inicial) & Q(data__lte=data_final)).order_by('data')
        return queryset

    def jogadasEntreIntervaloDataPorTela(self,data_inicial,data_final,tela):
        queryset = self.filter(Q(data__gte=data_inicial) & Q(data__lte=data_final) & Q(tela=tela)).order_by('data')
        return queryset

    def jogadasPorCordenadas(self,data_inicial,data_final,tela,mao,jogada):
        queryset = self.filter( Q(tela=tela) & 
                                Q(data__gte=data_inicial) & 
                                Q(data__lte=data_final) &
                                Q(mao=mao)).order_by('data')
        return queryset[0 : (jogada+1) ] 

    def jogadasPorMao(self,mao):
        queryset = self.filter(Q(mao=mao)).order_by('data')
        return queryset

    def jogadaPorCordenada(self,mao,jogada):
        queryset = self.filter(Q(mao=mao)).order_by('data')
        return queryset[jogada]

    def deletarMao(self,mao):
        queryset = self.filter(Q(mao=mao)).order_by('data')
        queryset.delete()
        return queryset

    def ultima_jogada(self,tela=0):
        return [self.filter(tela=tela).order_by('-data')[0]]

    def ultimaMesa(self,tela=0):
        queryset = self.filter(tela=tela).order_by('-data')[0]
        return self.filter(mao=queryset.mao,tela=tela).order_by('data')

    def jogadasPorMao(self,mao):
        return self.filter(mao=mao).order_by('data')

    def cientista_processado(self):
        queryset = self.filter(cientista_processado=False).order_by('data')[0]
        queryset.update(set__cientista_processado=True)
        queryset.reload()
        return queryset

    

class ValidarFicheiro(Document):

    valido_pote = fields.FloatField(default=0.0, null=True)
    valido_pote_rodada = fields.FloatField(default=0.0, null=True)
    valido_bord = fields.BooleanField()
    valido_combo = fields.BooleanField()
    valido_hole_cards = fields.BooleanField()
    valido_diler = fields.BooleanField()

    valido_vez_A = fields.BooleanField()
    valido_vez_B = fields.BooleanField()
    valido_vez_C = fields.BooleanField()
    valido_vez_D = fields.BooleanField()
    valido_vez_E = fields.BooleanField()
    valido_vez_F = fields.BooleanField()

    valido_fichas_A = fields.BooleanField()
    valido_fichas_B = fields.BooleanField()
    valido_fichas_C = fields.BooleanField()
    valido_fichas_D = fields.BooleanField()
    valido_fichas_E = fields.BooleanField()
    valido_fichas_F = fields.BooleanField()

    valido_aposta_A = fields.BooleanField()
    valido_aposta_B = fields.BooleanField()
    valido_aposta_C = fields.BooleanField()
    valido_aposta_D = fields.BooleanField()
    valido_aposta_E = fields.BooleanField()
    valido_aposta_F = fields.BooleanField()

    meta = {
        'abstract': True,
    }

class Ficheiro(Document):

    pote = fields.FloatField(default=0.0, null=True)

    pote_rodada = fields.FloatField(default=0.0, null=True)

    bord_FLOP_1 = fields.StringField(default="", null=True)
    bord_FLOP_2 = fields.StringField(default="", null=True)
    bord_FLOP_3 = fields.StringField(default="", null=True)
    bord_TURN = fields.StringField(default="", null=True)
    bord_RIVER = fields.StringField(default="", null=True)

    combo_A_1 = fields.StringField(default="", null=True)
    combo_A_2 = fields.StringField(default="", null=True)
    combo_B_1 = fields.StringField(default="", null=True)
    combo_B_2 = fields.StringField(default="", null=True)
    combo_C_1 = fields.StringField(default="", null=True)
    combo_C_2 = fields.StringField(default="", null=True)
    combo_D_1 = fields.StringField(default="", null=True)
    combo_D_2 = fields.StringField(default="", null=True)
    combo_E_1 = fields.StringField(default="", null=True)
    combo_E_2 = fields.StringField(default="", null=True)
    combo_F_1 = fields.StringField(default="", null=True)
    combo_F_2 = fields.StringField(default="", null=True)

    fichas_A = fields.FloatField(default=0.0, null=True)
    fichas_B = fields.FloatField(default=0.0, null=True)
    fichas_C = fields.FloatField(default=0.0, null=True)
    fichas_D = fields.FloatField(default=0.0, null=True)
    fichas_E = fields.FloatField(default=0.0, null=True)
    fichas_F = fields.FloatField(default=0.0, null=True)

    aposta_A = fields.FloatField(default=0.0, null=True)
    aposta_B = fields.FloatField(default=0.0, null=True)
    aposta_C = fields.FloatField(default=0.0, null=True)
    aposta_D = fields.FloatField(default=0.0, null=True)
    aposta_E = fields.FloatField(default=0.0, null=True)
    aposta_F = fields.FloatField(default=0.0, null=True)

    hole_cards_A = fields.BooleanField()
    hole_cards_B = fields.BooleanField()
    hole_cards_C = fields.BooleanField()
    hole_cards_D = fields.BooleanField()
    hole_cards_E = fields.BooleanField()
    hole_cards_F = fields.BooleanField()

    vez_A = fields.BooleanField()
    vez_B = fields.BooleanField()
    vez_C = fields.BooleanField()
    vez_D = fields.BooleanField()
    vez_E = fields.BooleanField()
    vez_F = fields.BooleanField()

    diler_A = fields.BooleanField()
    diler_B = fields.BooleanField()
    diler_C = fields.BooleanField()
    diler_D = fields.BooleanField()
    diler_E = fields.BooleanField()
    diler_F = fields.BooleanField()


    meta = {
        'abstract': True,
    }

class Analista(Document):

    heroi_letra = fields.StringField(default="", null=True)
    heroi_posicao = fields.StringField(default="", null=True)
    heroi_combo = fields.StringField(default="", null=True)

    vencedor = fields.StringField(default="", null=True)
    showdown = fields.BooleanField()

    ultimo_jogador_posicao = fields.StringField(default="", null=True)
    ultimo_jogador_letra = fields.StringField(default="", null=True)

    size_bet_valor = fields.FloatField(default=0.0, null=True)
    size_bet_blind = fields.FloatField(default=0.0, null=True)
    size_bet_pote = fields.FloatField(default=0.0, null=True)
    size_bet_vilao = fields.FloatField(default=0.0, null=True)
    size_bet_fichas = fields.FloatField(default=0.0, null=True)

    nome_acao = fields.StringField(default="", null=True)
    nome_bet = fields.StringField(default="", null=True)
    nome_jogada = fields.StringField(default="", null=True)
    nome_vilao = fields.StringField(default="", null=True)

    nome_utima_bet = fields.StringField(default="", null=True)
    bord_etapa = fields.StringField(default="", null=True)

    meta = {
        'abstract': True,
    }


class Cientista(Ficheiro, ValidarFicheiro, Analista):

    mao = fields.IntField(default=0, null=True)
    tela = fields.IntField(default=0, null=True)
    data = fields.DateTimeField(required=True)
    linha = fields.DynamicField(default="", null=True)
    nada = fields.DynamicField(default="", null=True)

    meta = {'queryset_class': CientistaQuerySet}

