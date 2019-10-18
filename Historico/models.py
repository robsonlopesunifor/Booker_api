from django.db import models

# Create your models here.
from mongoengine import Document, fields

class Historico(Document):
    estilo_oponente = fields.StringField(required=True)
    posicao_heroi = fields.StringField(required=True)
    posicao_vilao = fields.StringField(required=True)
    protagonista = fields.StringField(required=True)
