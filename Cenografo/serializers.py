from rest_framework_mongoengine import serializers
from Cenografo.models import Cena

class CenaSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Cena
        fields = '__all__'

