from rest_framework_mongoengine import serializers

class MaosPossiveisSerializer(serializers.DocumentSerializer):
    class Meta:
        fields = ['board','hole_cards']