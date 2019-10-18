from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields, QuerySet

class CenaManager(models.Manager):

    def primeiro_cientista_pendente(self):
        return self.get_queryset() #.filter(cientista_processado=True).order_by('data').last()


class CenaQuerySet(QuerySet):

    def primeiro_cientista_pendente(self):
        return self.filter(cientista_processado=False).order_by('data')[0]

    def quantidade_cientista_pendente(self):
        return self.filter(cientista_processado=False).count()

    def cientista_processado(self):
        queryset = self.filter(cientista_processado=False).order_by('data')[0]
        queryset.update(set__cientista_processado=True)
        queryset.reload()
        return queryset


class Combo(EmbeddedDocument):
    A_1 = fields.StringField(default="", null=True)
    A_2 = fields.StringField(default="", null=True)
    B_1 = fields.StringField(default="", null=True)
    B_2 = fields.StringField(default="", null=True)
    C_1 = fields.StringField(default="", null=True)
    C_2 = fields.StringField(default="", null=True)
    D_1 = fields.StringField(default="", null=True)
    D_2 = fields.StringField(default="", null=True)
    E_1 = fields.StringField(default="", null=True)
    E_2 = fields.StringField(default="", null=True)
    F_1 = fields.StringField(default="", null=True)
    F_2 = fields.StringField(default="", null=True)

class Bord(EmbeddedDocument):
    FLOP_1 = fields.StringField(default="", null=True)
    FLOP_2 = fields.StringField(default="", null=True)
    FLOP_3 = fields.StringField(default="", null=True)
    TURN = fields.StringField(default="", null=True)
    RIVER = fields.StringField(default="", null=True)

class max_1_data(EmbeddedDocument):
    A = fields.DateTimeField(required=True)

class max_1_float(EmbeddedDocument):
    A = fields.FloatField(default=0.0, null=True)

class max_1_int(EmbeddedDocument):
    A = fields.IntField(default=0, null=True)

class max_6_float(EmbeddedDocument):
    A = fields.FloatField(default=0.0, null=True)
    B = fields.FloatField(default=0.0, null=True)
    C = fields.FloatField(default=0.0, null=True)
    D = fields.FloatField(default=0.0, null=True)
    E = fields.FloatField(default=0.0, null=True)
    F = fields.FloatField(default=0.0, null=True)

class max_6_boolean(EmbeddedDocument):
    A = fields.BooleanField()
    B = fields.BooleanField()
    C = fields.BooleanField()
    D = fields.BooleanField()
    E = fields.BooleanField()
    F = fields.BooleanField()


class Ficheiro(EmbeddedDocument):
    pote = fields.EmbeddedDocumentField(max_1_float)
    pote_rodada = fields.EmbeddedDocumentField(max_1_float)
    bord = fields.EmbeddedDocumentField(Bord)
    combo = fields.EmbeddedDocumentField(Combo)
    fichas = fields.EmbeddedDocumentField(max_6_float)
    aposta = fields.EmbeddedDocumentField(max_6_float)
    hole_cards = fields.EmbeddedDocumentField(max_6_boolean)
    vez = fields.EmbeddedDocumentField(max_6_boolean)
    diler = fields.EmbeddedDocumentField(max_6_boolean)
    tela = fields.EmbeddedDocumentField(max_1_int)
    data = fields.EmbeddedDocumentField(max_1_data)


class Cena(Document):

    titulo = fields.StringField(required=True)
    tela = fields.IntField(required=True)
    data = fields.DateTimeField(required=True)
    chave = fields.StringField(required=True)

    foto = fields.StringField(required="",null=True) # propria imagem
    fotografo_processado = fields.BooleanField() # indicador de foto tirada
    endereco_imegem = fields.StringField(required="",null=True) # endereco de onde a foto foi salva
    foto_salva = fields.BooleanField() # Indicador de foto salva

    cena = fields.EmbeddedDocumentField(Ficheiro,required=True) # fichario
    cenografo_processado = fields.BooleanField()  # fichario
    cena_salva = fields.BooleanField() # indicador da cena salva

    cientista_processado = fields.BooleanField()
    cientista_salva = fields.BooleanField()

    nova_carta = fields.BooleanField()
    recorte = fields.ListField(fields.IntField(),default=[0,0,0,0])
    mesa = fields.IntField(default=0)

    meta = {'queryset_class': CenaQuerySet}
