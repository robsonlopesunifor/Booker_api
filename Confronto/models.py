from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields

class Tabela(EmbeddedDocument):
    carta = fields.StringField(required=True)
    acoes = fields.DynamicField(required=True)

class Confronto(Document):
    estilo_oponente = fields.StringField(required=True)
    posicao_heroi = fields.StringField(required=True)
    posicao_vilao = fields.StringField(required=True)
    protagonista = fields.StringField(required=True)
    tabela = fields.ListField(fields.EmbeddedDocumentField(Tabela))
