from .models import Test
from rest_framework import serializers

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'
        read_only_fields = ['response','user']