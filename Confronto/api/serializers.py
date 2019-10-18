from rest_framework_mongoengine import serializers
from Confronto.models import Tabela, Confronto

class ConfrontoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Confronto
        fields = '__all__'

