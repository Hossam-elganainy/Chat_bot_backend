from django.shortcuts import render
from .serializers import MessageSerializer
from rest_framework import generics, permissions
from .models import Message


from django.shortcuts import render
from .serializers import MessageSerializer
from rest_framework import generics, permissions
from .models import Message


def ai_response(question):
    
    return "This response is from AI"


class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        question = serializer.validated_data['question']
        ai_reply = ai_response(question)
        serializer.save(response=ai_reply)
