from rest_framework import serializers
from .models import Chat
from message.serializers import MessageSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id','name','created_at','updated_at']
        read_only_fields = ['created_at', 'updated_at']


class ChatDetailsSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True,read_only=True)
    class Meta:
        model = Chat
        fields = ['id','name','created_at','updated_at','messages']
        