from rest_framework import serializers

from freecoinage.coins.models import Market


class marketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
#        fields = ('title', 'description', 'completed')
