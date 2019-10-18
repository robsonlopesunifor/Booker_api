from rest_framework_mongoengine import serializers
from Historico.models import Historico

class HistoricoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Historico
        fields = '__all__'

