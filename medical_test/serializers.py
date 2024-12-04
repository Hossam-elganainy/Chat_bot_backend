from rest_framework import serializers
from .models import Medical

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = '__all__'
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)    

